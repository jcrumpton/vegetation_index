import os.path
import sys
from osgeo import gdal


def create_output_filename(input_filename, to_append):
    """
    create output filename by appending a type to the base of inputfilename
    examples: 2B_FL2 + ndvi = 2B_FL2_ndvi.tif
              ./RGB_data/200ft_BREN.tif + ndvi = ./RGB_data/200ft_BREN_ndvi.tif
              
    """
    parts = os.path.splitext(input_filename)
    new_filename = parts[0] + "_" + to_append + ".tif"
    # print(new_filename)
    
    return new_filename


def create_output_file(output_filename, num_bands, dataset, datatype=gdal.GDT_Float32):
    """ 
    create output geotif with same extent as dataset
    """
    driver = gdal.GetDriverByName('GTiff')
    output = driver.Create(
        output_filename, dataset.RasterXSize, dataset.RasterYSize, num_bands, datatype)
    output.SetProjection(dataset.GetProjection())
    output.SetGeoTransform(dataset.GetGeoTransform())
    
    return output


def retrieve_nodata_value(filename):
    """
    open input file and retrieve the nodata value of the first band
    """
    try:
        src_ds = gdal.Open(filename)
    except RuntimeError as e:
        print ('Unable to open input file')
        print (e)
        sys.exit(1)

    srcband = src_ds.GetRasterBand(1)
    nodata_value = srcband.GetNoDataValue()
    return nodata_value
    