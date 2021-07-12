import numpy as np
from osgeo import gdal
import sys
import argparse
import gri_util

gdal.UseExceptions()  # allow GDAL to throw Python Exceptions


if __name__ == "__main__":
    
    # input_filename = "./HSI_data/2B_FL2.tif"
    
    parser = argparse.ArgumentParser(description='Calculate vegetation index from a hyperspectral input file')

    parser.add_argument('input_filename',
                        metavar='input_filename',
                        type=str,
                        help='the hyperspectral input file to use as input')

    parser.add_argument('vegetation_index',
                        metavar='vegetation_index',
                        type=str,
                        help='the vegetation index to calculate')

    args = parser.parse_args()

    input_filename = args.input_filename

    try:
        src_ds = gdal.Open(input_filename)
    except RuntimeError as e:
        print ('Unable to open input file')
        print (e)
        sys.exit(1)

    vegetation_index = args.vegetation_index
    if vegetation_index not in gri_util.VALID_INDICES:
        print(f'{vegetation_index} is not a valid index to calculate')
        print(f'Choices are: {gri_util.VALID_INDICES}')
        sys.exit(1)

    hdr_filename = gri_util.hdr_filename_from_base_filename(input_filename)
    hdr_dictionary = gri_util.read_hdr_file(hdr_filename)

    output_filename = gri_util.create_output_filename(input_filename, vegetation_index)
    # create new dataset with same extent as source dataset
    out_ds = gri_util.create_output_file(output_filename, 1, src_ds)

    #calculator = locals()["calculate_"+vegetation_index]
    calculator = getattr(gri_util, "calculate_"+vegetation_index)
    calculated_band = calculator(src_ds, hdr_dictionary)

    # write calculated band
    out_band = out_ds.GetRasterBand(1)

    from gri_util.vi_util import nodata_value
    if nodata_value:
        calculated_band = calculated_band.filled(nodata_value)
        out_band.SetNoDataValue(nodata_value)
    
    out_band.WriteArray(calculated_band)
    out_band.FlushCache()
    out_band.ComputeStatistics(False)

    # write output file
    out_ds = None

