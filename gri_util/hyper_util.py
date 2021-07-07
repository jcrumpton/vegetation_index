import pathlib
import numpy as np
from osgeo import gdal

def read_hdr_file(headername):
    # adapted from
    # https://github.com/danforthcenter/plantcv/blob/master/plantcv/plantcv/hyperspectral/read_data.py
    #

    # Initialize dictionary
    header_dict = {}

    with open(headername, "r") as f:
        # Replace characters for easier parsing
        hdata = f.read()
        hdata = hdata.replace(",\n", ",")
        hdata = hdata.replace("\n,", ",")
        hdata = hdata.replace("{\n", "{")
        hdata = hdata.replace("\n}", "}")
        hdata = hdata.replace(" \n ", "")
        hdata = hdata.replace(";", "")
    hdata = hdata.split("\n")

    # Loop through and create a dictionary from the header file
    for i, string in enumerate(hdata):
        if ' = ' in string:
            header_data = string.split(" = ")
            header_dict.update({header_data[0].rstrip(): header_data[1].rstrip()})
        elif ' : ' in string:
            header_data = string.split(" : ")
            header_dict.update({header_data[0].rstrip(): header_data[1].rstrip()})

    # Reformat wavelengths
    header_dict["wavelength"] = header_dict["wavelength"].replace("{", "")
    header_dict["wavelength"] = header_dict["wavelength"].replace("}", "")
    header_dict["wavelength"] = header_dict["wavelength"].replace(" ", "")
    header_dict["wavelength"] = header_dict["wavelength"].split(",")

    # Create dictionary of wavelengths
    wavelength_dict = {}
    for j, wavelength in enumerate(header_dict["wavelength"]):
        #wavelength_dict.update({float(wavelength): float(j)})
        wavelength_dict.update({float(wavelength): (j+1)})
    header_dict["wavelength_dict"] = wavelength_dict

    # Replace datatype ID number with the numpy datatype
    dtype_dict = {"1": np.uint8, "2": np.int16, "3": np.int32, "4": np.float32, "5": np.float64, "6": np.complex64,
                  "9": np.complex128, "12": np.uint16, "13": np.uint32, "14": np.uint64, "15": np.uint64}
    header_dict["data type"] = dtype_dict[header_dict["data type"]]

    return header_dict
    

def hdr_filename_from_base_filename(filename):

    path = pathlib.Path(filename)
    hdr_filename = (path.parent).joinpath(path.stem + '.hdr')
    # print(hdr_filename)

    return hdr_filename


def wavelengths_as_np_array(header_dictionary):
    wavelengths_as_strings = header_dictionary["wavelength"]
    wavelengths_as_floats = []
    for each in wavelengths_as_strings:
        wavelengths_as_floats.append(float(each))
    return np.array(wavelengths_as_floats)


def closest_wavelength(header_dictionary, target, tolerance=10):
    wavelengths = wavelengths_as_np_array(header_dictionary)
    min_index = np.argmin(np.abs(wavelengths - target))
    closest = wavelengths[min_index]
    if abs(target-closest) > tolerance:
        raise Exception(f"closest wavelength ({closest}) to target ({target}) is not within specified tolerance ({tolerance})")
    
    return closest


def band_for_wavelength(header_dictionary, wavelength):
    return (header_dictionary["wavelength_dict"])[wavelength]


def extract_band(band, dataset):
    """ 
    fetch the named band from the hyperspectral file
    band: integer
    """

    raster_band = dataset.GetRasterBand(band)
    metadata = raster_band.GetMetadata_Dict()
    new_metadata = {}
    new_metadata['wavelength'] = metadata['wavelength']
    new_metadata['wavelength_units'] = metadata['wavelength_units']

    data = raster_band.ReadAsArray()
    data = np.ma.masked_values(data, 0.0)
        
    return data, new_metadata


def data_for_wavelength(source_dataset, hdr_dictionary, wavelength):
    closest_freq = closest_wavelength(hdr_dictionary, wavelength)
    band_number = band_for_wavelength(hdr_dictionary, closest_freq)
    data, _ = extract_band(band_number, source_dataset)

    return data


# hdr_filename = hdr_filename_from_base_filename(r"K:\users\joec\06-01-2021\Deliverables_2B\FL1")
# hdr_dictionary = read_hdr_file(hdr_filename)
# b = closest_wavelength(hdr_dictionary, 1012)
# print(b)
# print(band_for_wavelength(hdr_dictionary,b))