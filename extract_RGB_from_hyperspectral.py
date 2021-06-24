import numpy as np
from osgeo import gdal
import sys
import argparse
import os.path

gdal.UseExceptions()  # allow GDAL to throw Python Exceptions

nodata_value = -99

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
    

def create_band_by_frequency_dict(dataset):
    """ 
    Creates a dictionary that maps frequency in nm (integer) to band number in geotiff
    """
    frequency_by_band = dataset.GetMetadata_Dict()
    inverse_dict = {}

    # TODO add exception handling for parsing...
    for band_string in frequency_by_band.keys():
        # assumes each band key is formatted as Band_12
        if band_string.startswith('Band') is not True:
            continue
        partitioned = band_string.rpartition('_')
        number_string = partitioned[2]
        number = int(number_string)

        # assumes frequency is formatted as 660.415 nm
        freq_string = frequency_by_band[band_string]
        partitioned = freq_string.partition(' ')
        freq = partitioned[0]
        partitioned = freq.partition('.')
        freq = int(partitioned[0])

        inverse_dict[freq] = number

    return inverse_dict


def create_output_file(name, num_bands, dataset):
    """ 
    create output geotif with same extent as dataset
    """
    driver = gdal.GetDriverByName('GTiff')
    output = driver.Create(
        name, dataset.RasterXSize, dataset.RasterYSize, num_bands, gdal.GDT_Float32, options=["INTERLEAVE=PIXEL"])
    output.SetProjection(dataset.GetProjection())
    output.SetGeoTransform(dataset.GetGeoTransform())
    return output


def get_color_band(wavelength, dataset):
    """ 
    fetch the named wavelength band from the hyperspectral file
    wavelength: integer
    """
    band_number = band_by_frequency[wavelength]
    if band_number:
        raster_band = dataset.GetRasterBand(band_number)
        metadata = raster_band.GetMetadata_Dict()
        new_metadata = {}
        new_metadata['wavelength'] = metadata['wavelength']
        new_metadata['wavelength_units'] = metadata['wavelength_units']

        # print(raster_band.GetMetadata_Dict())

        data = raster_band.ReadAsArray()
        data = np.ma.masked_values(data, 0.0)
        data = data.filled(nodata_value)
        return data, new_metadata

    return None


if __name__ == "__main__":
    
    # input_filename = "./HSI_data/2B_FL12.dat"
    
    parser = argparse.ArgumentParser(description='Create RGB geotiff from a hyperspectral geotif')

    parser.add_argument('input_filename',
                        metavar='input_filename',
                        type=str,
                        help='the hyperspectral geotif file to use as input')

    args = parser.parse_args()

    input_filename = args.input_filename

    try:
        src_ds = gdal.Open(input_filename)
    except RuntimeError as e:
        print ('Unable to open input tif')
        print (e)
        sys.exit(1)

    
    output_filename = create_output_filename(input_filename, "RGB")

    band_by_frequency = create_band_by_frequency_dict(src_ds)

    # # print frequencies in ascending order
    # frequency_list = list(band_by_frequency.keys())
    # frequency_list.sort()
    # print(frequency_list)

    # create new dataset with same extent as source dataset
    out_ds = create_output_file(output_filename, 3, src_ds)
    output_band_number = 1

    for color in [660, 550, 480]:
        color_band, metadata = get_color_band(color, src_ds)
    
        # write calculated band
        out_band = out_ds.GetRasterBand(output_band_number)
        out_band.SetMetadata(metadata)
        descrip_string = metadata['wavelength'] + " " + metadata['wavelength_units']
        out_band.SetDescription(descrip_string)
        

        if nodata_value:
             out_band.SetNoDataValue(nodata_value)
    
        out_band.WriteArray(color_band)
        #out_band.FlushCache()
        out_band.ComputeStatistics(False)
        output_band_number += 1

    # write output file
    out_ds.FlushCache()
    del out_ds


