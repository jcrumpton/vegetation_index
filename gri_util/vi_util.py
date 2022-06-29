import numpy as np
from gri_util.hyper_util import data_for_wavelength

nodata_value = None


# to add a new vegetation index:
#   1) add acronym to VALID_INDICES
#   2) write a compute_<acronym> method
#
VALID_INDICES = ['NDVI', 'gNDVI', 'NDVI650', 'NDVI673', 'NDVI675', 'NDVI680', 'NDVI705', 'NPCI', 
                 'PRI', 'ND800_700', 'ND800_680', 'mSR705', 'PSSRa', 
                 'SR445', 'SR487', 'ARI', 'mARI', 'SAVI']


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


def calculate_NDVI650(source_dataset, hdr_dictionary):
    # fetch bands from input
    R650 = data_for_wavelength(source_dataset, hdr_dictionary, 650)
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)

    global nodata_value
    nodata_value = -99

    # Mask the R650 band, don't allow division by zero
    R650 = np.ma.masked_where(R650 + R750 == 0, R650)

    # Do the calculation.
    NDVI650 = (R750 - R650) / (R750 + R650)

    return NDVI650


def calculate_NDVI673(source_dataset, hdr_dictionary):
    # fetch bands from input
    R673 = data_for_wavelength(source_dataset, hdr_dictionary, 673)
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)

    global nodata_value
    nodata_value = -99

    # Mask the R673 band, don't allow division by zero
    R673 = np.ma.masked_where(R673 + R750 == 0, R673)

    # Do the calculation.
    NDVI673 = (R750 - R673) / (R750 + R673)

    return NDVI673


def calculate_NDVI675(source_dataset, hdr_dictionary):
    # fetch bands from input
    R675 = data_for_wavelength(source_dataset, hdr_dictionary, 675)
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)

    global nodata_value
    nodata_value = -99

    # Mask the R675 band, don't allow division by zero
    R675 = np.ma.masked_where(R675 + R750 == 0, R675)

    # Do the calculation.
    NDVI675 = (R750 - R675) / (R750 + R675)

    return NDVI675


def calculate_NDVI680(source_dataset, hdr_dictionary):
    # fetch bands from input
    R680 = data_for_wavelength(source_dataset, hdr_dictionary, 680)
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)

    global nodata_value
    nodata_value = -99

    # Mask the R680 band, don't allow division by zero
    R680 = np.ma.masked_where(R680 + R750 == 0, R680)

    # Do the calculation.
    NDVI680 = (R750 - R680) / (R750 + R680)

    return NDVI680


def calculate_NDVI705(source_dataset, hdr_dictionary):
    # fetch bands from input
    R705 = data_for_wavelength(source_dataset, hdr_dictionary, 705)
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)

    global nodata_value
    nodata_value = -99

    # Mask the R705 band, don't allow division by zero
    R705 = np.ma.masked_where(R705 + R750 == 0, R705)

    # Do the calculation.
    NDVI705 = (R750 - R705) / (R750 + R705)

    return NDVI705


def calculate_NPCI(source_dataset, hdr_dictionary):
    # fetch bands from input
    R680 = data_for_wavelength(source_dataset, hdr_dictionary, 680)
    R430 = data_for_wavelength(source_dataset, hdr_dictionary, 430)

    global nodata_value
    nodata_value = -99

    # Mask the R680 band, don't allow division by zero
    R680 = np.ma.masked_where(R680 + R430 == 0, R680)

    # Do the calculation.
    NPCI = (R680 - R430) / (R680 + R430)

    return NPCI


def calculate_PRI(source_dataset, hdr_dictionary):
    # fetch bands from input
    R531 = data_for_wavelength(source_dataset, hdr_dictionary, 531)
    R570 = data_for_wavelength(source_dataset, hdr_dictionary, 570)

    global nodata_value
    nodata_value = -99

    # Mask the R531 band, don't allow division by zero
    R680 = np.ma.masked_where(R531 + R570 == 0, R531)

    # Do the calculation.
    PRI = (R531 - R570) / (R531 + R570)

    return PRI


def calculate_ND800_700(source_dataset, hdr_dictionary):
    # fetch bands from input
    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)
    R700 = data_for_wavelength(source_dataset, hdr_dictionary, 700)

    global nodata_value
    nodata_value = -99

    # Mask the R800 band, don't allow division by zero
    R800 = np.ma.masked_where(R800 + R700 == 0, R800)

    # Do the calculation.
    ND800_700 = (R800 - R700) / (R800 + R700)

    return ND800_700


def calculate_ND800_680(source_dataset, hdr_dictionary):
    # fetch bands from input
    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)
    R680 = data_for_wavelength(source_dataset, hdr_dictionary, 680)

    global nodata_value
    nodata_value = -99

    # Mask the R680 band, don't allow division by zero
    R800 = np.ma.masked_where(R800 + R680 == 0, R800)

    # Do the calculation.
    ND800_680 = (R800 - R680) / (R800 + R680)

    return ND800_680


def calculate_mSR705(source_dataset, hdr_dictionary):
    # fetch bands from input
    R445 = data_for_wavelength(source_dataset, hdr_dictionary, 445)
    R705 = data_for_wavelength(source_dataset, hdr_dictionary, 705)
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)

    global nodata_value
    nodata_value = -99

    # Mask the R445 band, don't allow division by zero
    R445 = np.ma.masked_values(R445, 0.0)

    # Do the calculation.
    mSR705 = (R750 - R445) / (R705 / R445)

    return mSR705


def calculate_PSSRa(source_dataset, hdr_dictionary):
    # fetch bands from input
    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)
    R676 = data_for_wavelength(source_dataset, hdr_dictionary, 676)

    global nodata_value
    nodata_value = -99

    # Mask the R676 band, don't allow division by zero
    R676 = np.ma.masked_values(R676, 0.0)

    # Do the calculation.
    PSSRa = R800 / R676

    return PSSRa


def calculate_SR445(source_dataset, hdr_dictionary):
    
    R445 = data_for_wavelength(source_dataset, hdr_dictionary, 445)
    R445 = np.ma.masked_values(R445, 0.0)

    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)
    
    global nodata_value
    nodata_value = -10000

    SR445 = R800/R445

    return SR445


def calculate_SR487(source_dataset, hdr_dictionary):
    
    R487 = data_for_wavelength(source_dataset, hdr_dictionary, 487)

    R705 = data_for_wavelength(source_dataset, hdr_dictionary, 705)
    R705 = np.ma.masked_values(R705, 0.0)

    global nodata_value
    nodata_value = -10000

    SR487 = R487/R705

    return SR487    


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


def calculate_SAVI(source_dataset, hdr_dictionary):

    L = 0.5
    
    R670 = data_for_wavelength(source_dataset, hdr_dictionary, 670)
    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)

    global nodata_value
    nodata_value = -10000

    # Do the calculation.
    SAVI = (1 + L) * ((R800 - R670) / (R800 + R670 + L))

    return SAVI


