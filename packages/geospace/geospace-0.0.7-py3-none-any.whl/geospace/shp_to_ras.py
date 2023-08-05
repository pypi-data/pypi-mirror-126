import os
import numpy as np
from osgeo import gdal, ogr, osr
from geospace.utils import imagexy2geo, ds_name
from geospace.shape import proj_shapefile
from geospace._const import CREATION, CONFIG


def rasterize(shp, attr, out_path, ds_eg, tem_path, **kwargs):
    # create out put name
    out_file = os.path.join(out_path, os.path.splitext(
        os.path.basename(shp))[0] + '.tif')
    if os.path.exists(out_file):
        return
    tem_file = os.path.join(tem_path, os.path.splitext(
        os.path.basename(shp))[0] + '.tif')

    # extent warp options
    ds_ex = gdal.Translate('/vsimem/_extent.tif', ds_eg, bandList=[1])
    t = ds_eg.GetGeoTransform()
    temp_option = gdal.WarpOptions(multithread=True, options=CONFIG,
                                   creationOptions=CREATION, **kwargs,
                                   xRes=t[1] / 10, yRes=t[5] / 10,
                                   outputType=gdal.GDT_Float64)

    ds_tem = gdal.Warp(tem_file, ds_ex, options=temp_option)
    band = ds_tem.GetRasterBand(1)
    option = gdal.WarpOptions(multithread=True, options=CONFIG,
                              creationOptions=CREATION, **kwargs,
                              xRes=t[1], yRes=t[5], resampleAlg=gdal.GRA_Average,
                              outputType=gdal.GDT_Float64)

    driver = ogr.GetDriverByName('ESRI Shapefile')
    shp_factor = driver.Open(shp)
    layer = shp_factor.GetLayer()

    # create and use RasterizeLayer
    band.Fill(band.GetNoDataValue())
    gdal.RasterizeLayer(ds_tem, [1], layer,
                        options=["ATTRIBUTE=%s" % attr, 'ALL_TOUCHED=TRUE'])
    gdal.Warp(out_file, ds_tem, options=option)

    band = None
    ds_tem = None
    shp_factor = None
    layer = None


def download_tiles(shp, tile_pixel):
    # create the output layer
    driver = ogr.GetDriverByName("ESRI Shapefile")
    out_shp = '/vsimem/outline_wgs84.shp'
    proj_shapefile(shp, out_shp)
    outDataSet = driver.Open(out_shp)
    outLayer = outDataSet.GetLayer()

    # Create the destination data source
    x_res = int(360 / tile_pixel)
    y_res = int(180 / tile_pixel)
    target_ds = gdal.GetDriverByName('GTiff').Create(
        '/vsimem/_tile.tif', x_res, y_res, 1, gdal.GDT_Byte)
    target_ds.SetGeoTransform((-180, tile_pixel, 0, 90, 0, -tile_pixel))
    target_srs = osr.SpatialReference()
    target_srs.ImportFromProj4(
        '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    target_ds.SetProjection(target_srs.ExportToWkt())
    band = target_ds.GetRasterBand(1)
    band.SetNoDataValue(0)

    # Rasterize
    gdal.RasterizeLayer(target_ds, [1], outLayer, burn_values=[
                        1], options=['ALL_TOUCHED=TRUE'])
    burn_tiles = target_ds.GetRasterBand(1).ReadAsArray()
    rows, cols = np.where(burn_tiles == 1)
    if rows.shape == 0:
        return None
    lon, lat = np.int_(imagexy2geo(target_ds, rows - 0.5, cols - 0.5))
    return lon, lat


def masked_outside(shp, ds):
    try:
        import psutil
    except Exception:
        print('psutil must be installed first')

    ds, ras = ds_name(ds)
    ds = gdal.Open(ras, gdal.GA_Update)
    trans = ds.GetGeoTransform()
    ratio = int(ds.RasterYSize * ds.RasterXSize /
                (psutil.virtual_memory().available * 0.5 /
                 (2 + ds.ReadAsArray(0, 0, 1, 1).dtype.itemsize)) + 1)

    # create the output layer
    driver = ogr.GetDriverByName("ESRI Shapefile")
    out_shp = '/vsimem/outline_wgs84.shp'
    out_srs = osr.SpatialReference(wkt=ds.GetProjection())
    proj_shapefile(shp, out_shp, out_srs=out_srs)
    outDataSet = driver.Open(out_shp)
    outLayer = outDataSet.GetLayer()

    band = ds.GetRasterBand(1)
    b_xsize, b_ysize = band.GetBlockSize()
    xsize = max(ds.RasterXSize // ratio + 1, b_xsize)
    ysize = max(ds.RasterYSize // ratio + 1, b_ysize)
    xoffs = range(0, ds.RasterXSize, xsize)
    yoffs = range(0, ds.RasterYSize, ysize)
    for i in range(ds.RasterCount):
        band = ds.GetRasterBand(i + 1)
        for xoff in xoffs:
            for yoff in yoffs:
                win_xsize = min(xsize, ds.RasterXSize - xoff)
                win_ysize = min(ysize, ds.RasterYSize - yoff)

                # Create the destination data source
                target_ds = gdal.GetDriverByName('GTiff').Create(
                    '/vsimem/_outside.tif', win_xsize, win_ysize, 1, gdal.GDT_Byte)
                left_up_lon, left_up_lat = imagexy2geo(ds, yoff - 0.5, xoff - 0.5)
                target_ds.SetGeoTransform((left_up_lon, trans[1], 0, left_up_lat, 0, trans[5]))
                target_ds.SetProjection(ds.GetProjection())
                target_band = target_ds.GetRasterBand(1)
                target_band.SetNoDataValue(0)

                # Rasterize
                gdal.RasterizeLayer(target_ds, [1], outLayer, burn_values=[1],
                                    options=['ALL_TOUCHED=TRUE'])
                outside = np.logical_not(target_ds.GetRasterBand(1).ReadAsArray())
                target_band = None
                target_ds = None

                if outside.any():
                    arr = ds.ReadAsArray(xoff=xoff, yoff=yoff,
                                         xsize=win_xsize, ysize=win_ysize)
                    arr[outside] = band.GetNoDataValue()
                    band.WriteArray(arr, xoff=xoff, yoff=yoff)
                    del arr
                del outside
        band = None
