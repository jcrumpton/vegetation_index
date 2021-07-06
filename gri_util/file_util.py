import os.path
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


def create_output_file(name, num_bands, dataset, datatype=gdal.GDT_Float32):
    """ 
    create output geotif with same extent as dataset
    """
    driver = gdal.GetDriverByName('GTiff')
    output = driver.Create(
        name, dataset.RasterXSize, dataset.RasterYSize, num_bands, datatype)
    output.SetProjection(dataset.GetProjection())
    output.SetGeoTransform(dataset.GetGeoTransform())
    
    return output

