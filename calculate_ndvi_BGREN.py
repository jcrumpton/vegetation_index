import numpy as np
from osgeo import gdal
import sys
import argparse
import gri_util

gdal.UseExceptions()  # allow GDAL to throw Python Exceptions

NO_DATA_VALUE = -10000

def calculate_ndvi(source_dataset):
    # fetch bands from input: BGREN
    red_band = 3
    red = source_dataset.GetRasterBand(red_band).ReadAsArray().astype(np.float32)
    nir_band = 5
    nir = source_dataset.GetRasterBand(nir_band).ReadAsArray()

    # Mask the red band 
    red = np.ma.masked_values(red, NO_DATA_VALUE)
    red = np.ma.masked_where(nir + red == 0, red)
    
    # Do the calculation.
    ndvi = (nir - red) / (nir + red)

    # Fill the empty cells.
    ndvi = ndvi.filled(NO_DATA_VALUE)

    return ndvi


if __name__ == "__main__":
    
    # input_filename = "K:/users/joec/06-01-2021/2021-06-01_USDA_NACA_400ft_BGREN.tif"
    
    parser = argparse.ArgumentParser(description='Calculate ndvi from a BGREN geotif')

    parser.add_argument('input_filename',
                        metavar='input',
                        type=str,
                        help='the BGREN geotif file to use as input')

    args = parser.parse_args()

    input_filename = args.input_filename
    
    output_filename = gri_util.create_output_filename(input_filename, "ndvi")

    try:
        src_ds = gdal.Open(input_filename)
    except RuntimeError as e:
        print ('Unable to open input file')
        print (e)
        sys.exit(1)


    # create new dataset with same extent as source dataset
    out_ds = gri_util.create_output_file(output_filename, 1, src_ds)

    calculated_band = calculate_ndvi(src_ds)

    # write calculated band
    out_band = out_ds.GetRasterBand(1)
    
    out_band.SetNoDataValue(NO_DATA_VALUE)
    out_band.WriteArray(calculated_band)
    out_band.FlushCache()
    out_band.ComputeStatistics(False)

    # write output file
    out_ds = None

