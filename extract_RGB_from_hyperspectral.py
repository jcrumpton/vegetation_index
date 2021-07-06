import numpy as np
from osgeo import gdal
import sys
import argparse
import gri_util

gdal.UseExceptions()  # allow GDAL to throw Python Exceptions

nodata_value = -99


if __name__ == "__main__":
    
    # input_filename = "./HSI_data/2B_FL12.dat"
    
    parser = argparse.ArgumentParser(description='Create RGB geotiff from a hyperspectral input file')

    parser.add_argument('input_filename',
                        metavar='input_filename',
                        type=str,
                        help='the hyperspectral file to use as input')

    args = parser.parse_args()

    input_filename = args.input_filename

    try:
        src_ds = gdal.Open(input_filename)
    except RuntimeError as e:
        print ('Unable to open input file')
        print (e)
        sys.exit(1)

    
    hdr_filename = gri_util.hdr_filename_from_base_filename(input_filename)
    hdr_dictionary = gri_util.read_hdr_file(hdr_filename)
    output_filename = gri_util.create_output_filename(input_filename, "RGB")
    out_ds = gri_util.create_output_file(output_filename, 3, src_ds)

    output_band_number = 1
    for freq in [660, 550, 480]:
        closest_freq = gri_util.closest_wavelength(hdr_dictionary, freq)
        band = gri_util.band_for_wavelength(hdr_dictionary, closest_freq)
        color_band, metadata = gri_util.extract_band(band, src_ds, nodata_value=nodata_value)
    
        # write calculated band
        out_band = out_ds.GetRasterBand(output_band_number)
        out_band.SetMetadata(metadata)
        descrip_string = metadata['wavelength'] + " " + metadata['wavelength_units']
        out_band.SetDescription(descrip_string)
        
        if nodata_value:
             out_band.SetNoDataValue(nodata_value)
    
        out_band.WriteArray(color_band)
        out_band.ComputeStatistics(False)
        output_band_number += 1

    # write output file
    out_ds.FlushCache()
    out_ds = None


