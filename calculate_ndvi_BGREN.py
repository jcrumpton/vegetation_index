import numpy as np
from osgeo import gdal
import sys
import argparse
import os.path

gdal.UseExceptions()  # allow GDAL to throw Python Exceptions

NO_DATA_VALUE = -10000


def create_output_filename(input_filename, to_append):
    """
    create output filename by appending a type to the inputfilename
    examples: 2B_FL2 + ndvi = 2B_FL2_ndvi.tif
              ./RGB_data/200ft_BREN.tif + ndvi = ./RGB_data/200ft_BREN_ndvi.tif
              
    """
    parts = os.path.splitext(input_filename)
    new_filename = parts[0] + "_" + to_append + ".tif"
    # print(new_filename)
    
    return new_filename

def create_output_file(name, num_bands, dataset):
    """ 
    create output geotif with same extent as dataset
    """
    driver = gdal.GetDriverByName('GTiff')

    output = driver.Create(
        name, dataset.RasterXSize, dataset.RasterYSize, num_bands, gdal.GDT_Float32)
    output.SetProjection(dataset.GetProjection())
    output.SetGeoTransform(dataset.GetGeoTransform())
   
    return output


def calculate_ndvi():
    # fetch bands from input: BGREN
    red_band = 3
    red = src_ds.GetRasterBand(red_band).ReadAsArray().astype(np.float)
    nir_band = 5
    nir = src_ds.GetRasterBand(nir_band).ReadAsArray()

    # Mask the red band 
    red = np.ma.masked_values(red, NO_DATA_VALUE)
    red = np.ma.masked_where(nir + red == 0, red)
    
    # Do the calculation.
    ndvi = (nir - red) / (nir + red)

    # Fill the empty cells.
    ndvi = ndvi.filled(NO_DATA_VALUE)

    return ndvi


if __name__ == "__main__":
    
    input_filename = "./RGB_data/2021-05-21_USDA_NACA_200ft_BGREN.tif"
    
    # parser = argparse.ArgumentParser(description='Calculate ndvi from a BGREN geotif')

    # parser.add_argument('input_filename',
    #                     metavar='input',
    #                     type=str,
    #                     help='the BGREN geotif file to use as input')

    # args = parser.parse_args()

    # input_filename = args.input_filename
    
    output_filename = create_output_filename(input_filename, "ndvi")

    try:
        src_ds = gdal.Open(input_filename)
    except RuntimeError as e:
        print ('Unable to open input tif')
        print (e)
        sys.exit(1)


    # create new dataset with same extent as source dataset
    out_ds = create_output_file(output_filename, 1, src_ds)

    calculated_band = calculate_ndvi()

    # write calculated band
    out_band = out_ds.GetRasterBand(1)
    
    out_band.SetNoDataValue(NO_DATA_VALUE)
    out_band.WriteArray(calculated_band)
    out_band.FlushCache()
    out_band.ComputeStatistics(False)

    # write output file
    del out_ds


