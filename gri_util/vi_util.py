import numpy as np
from gri_util.hyper_util import data_for_wavelength

nodata_value = None


# to add a new vegetation index:
#   1) add acronym to VALID_INDICES
#   2) write a compute_<acronym> method
#
VALID_INDICES = ['ARI','mARI','NDVI', 'gNDVI']


def calculate_NDVI(source_dataset, hdr_dictionary):
   
    # fetch bands from input
    red = data_for_wavelength(source_dataset, hdr_dictionary, 670)
    nir = data_for_wavelength(source_dataset, hdr_dictionary, 860)
    
    global nodata_value
    nodata_value = -99

    # Mask the red band, don't allow division by zero
    red = np.ma.masked_where(nir + red == 0, red)  

    # Do the calculation.
    NDVI = (nir - red) / (nir + red)

    return NDVI


def calculate_gNDVI(source_dataset, hdr_dictionary):
    # fetch bands from input
    R550 = data_for_wavelength(source_dataset, hdr_dictionary, 550)
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)

    global nodata_value
    nodata_value = -99

    # Mask the R550 band, don't allow division by zero
    R550 = np.ma.masked_where(R550 + R750 == 0, R550)

    # Do the calculation.
    gNDVI = (R750 - R550) / (R750 + R550)

    return gNDVI


def calculate_ARI(source_dataset, hdr_dictionary):
    
    R550 = data_for_wavelength(source_dataset, hdr_dictionary, 550)
    R550 = np.ma.masked_values(R550, 0.0)

    R700 = data_for_wavelength(source_dataset, hdr_dictionary, 700)
    R700 = np.ma.masked_values(R700, 0.0)

    global nodata_value
    nodata_value = -10000

    ARI = (1/R550) - (1/R700)

    return ARI


def calculate_mARI(source_dataset, hdr_dictionary):
    
    R550 = data_for_wavelength(source_dataset, hdr_dictionary, 550)
    R550 = np.ma.masked_values(R550, 0.0)

    R700 = data_for_wavelength(source_dataset, hdr_dictionary, 700)
    R700 = np.ma.masked_values(R700, 0.0)

    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)

    global nodata_value
    nodata_value = -10000

    # Do the calculation.
    mARI = R800 * ((1/R550) - (1/R700))

    return mARI

