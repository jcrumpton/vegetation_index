import numpy as np
from osgeo import gdal
import sys
import argparse
import os.path

gdal.UseExceptions()  # allow GDAL to throw Python Exceptions

# to add a new vegetation index:
#   1) add acronym to VALID_INDICES
#   2) write a compute_<acronym> method
#
VALID_INDICES = ['ARI','mARI','NDVI']

nodata_value = None

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
        name, dataset.RasterXSize, dataset.RasterYSize, num_bands, gdal.GDT_Float32)
    output.SetProjection(dataset.GetProjection())
    output.SetGeoTransform(dataset.GetGeoTransform())
    return output


def calculate_NDVI():
    # fetch bands from input
    red_band = band_by_frequency[669]
    red = src_ds.GetRasterBand(red_band).ReadAsArray().astype(np.float)
    nir_band = band_by_frequency[860]
    nir = src_ds.GetRasterBand(nir_band).ReadAsArray()

    global nodata_value
    nodata_value = -99

    # Mask the red band.
    red = np.ma.masked_where(nir + red == 0, red)

    # Do the calculation.
    NDVI = (nir - red) / (nir + red)

    return NDVI


def calculate_ARI():
    # fetch bands from input
    R550_band = band_by_frequency[550]
    R550 = src_ds.GetRasterBand(R550_band).ReadAsArray()
    R550 = np.ma.masked_values(R550, 0.0)

    R700_band = band_by_frequency[700]
    R700 = src_ds.GetRasterBand(R700_band).ReadAsArray()
    R700 = np.ma.masked_values(R700, 0.0)

    global nodata_value
    nodata_value = -99

    # Do the calculation.
    ARI = (1/R550) - (1/R700)

    return ARI


def calculate_mARI():
    # fetch bands from input
    R550_band = band_by_frequency[550]
    R550 = src_ds.GetRasterBand(R550_band).ReadAsArray()
    R550 = np.ma.masked_values(R550, 0.0)

    R700_band = band_by_frequency[700]
    R700 = src_ds.GetRasterBand(R700_band).ReadAsArray()
    R700 = np.ma.masked_values(R700, 0.0)

    R800_band = band_by_frequency[799]
    R800 = src_ds.GetRasterBand(R800_band).ReadAsArray()

    global nodata_value
    nodata_value = -99

    # Do the calculation.
    mARI = R800 * ((1/R550) - (1/R700))

    return mARI


if __name__ == "__main__":
    
    # input_filename = "./HSI_data/2B_FL2.tif"
    
    parser = argparse.ArgumentParser(description='Calculate ndvi from a hyperspectral geotif')

    parser.add_argument('input_filename',
                        metavar='input_filename',
                        type=str,
                        help='the hyperspectral geotif file to use as input')

    parser.add_argument('vegetation_index',
                        metavar='vegetation_index',
                        type=str,
                        help='the vegetation index to calculate')

    args = parser.parse_args()

    input_filename = args.input_filename

    try:
        src_ds = gdal.Open(input_filename)
    except RuntimeError as e:
        print ('Unable to open input tif')
        print (e)
        sys.exit(1)

    vegetation_index = args.vegetation_index
    if vegetation_index not in VALID_INDICES:
        print(f'{vegetation_index} is not a valid index to calculate')
        print(f'Choices are: {VALID_INDICES}')
        sys.exit(1)


    output_filename = create_output_filename(input_filename, vegetation_index)

    band_by_frequency = create_band_by_frequency_dict(src_ds)

    # # print frequencies in ascending order
    # frequency_list = list(band_by_frequency.keys())
    # frequency_list.sort()
    # print(frequency_list)

    # create new dataset with same extent as source dataset
    out_ds = create_output_file(output_filename, 1, src_ds)

    calculator = locals()["calculate_"+vegetation_index]
    calculated_band = calculator()

    # write calculated band
    out_band = out_ds.GetRasterBand(1)

    if nodata_value:
        calculated_band = calculated_band.filled(nodata_value)
        out_band.SetNoDataValue(nodata_value)
    
    out_band.WriteArray(calculated_band)
    out_band.FlushCache()
    out_band.ComputeStatistics(False)

    # write output file
    del out_ds


