import numpy as np
from gri_util.hyper_util import data_for_wavelength

nodata_value = None


# to add a new vegetation index:
#   1) add acronym to VALID_INDICES
#   2) write a compute_<acronym> method
#
VALID_INDICES = ['NDVI', 'gNDVI', 'NDVI650', 'NDVI673', 'NDVI675', 'NDVI680', 'NDVI705', 'NPCI', 
                 'PRI', 'ND800_700', 'ND800_680', 'mNDVI673', 'mND705', 'DD', 'mSR705', 'PSSRa', 
                 'PSSRb', 'SR445', 'SR487', 'SR680', 'SR700', 'SR705', 'SIPI', 'DATT', 'ChlRI_green', 
                 'ChlRI_red_green', 'CRI_green', 'CRI_red_edge', 'ARI', 'BGBO', 'mARI', 'SAVI']


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

    # Mask the R800 band, don't allow division by zero
    R800 = np.ma.masked_where(R800 + R680 == 0, R800)

    # Do the calculation.
    ND800_680 = (R800 - R680) / (R800 + R680)

    return ND800_680


def calculate_mNDVI673(source_dataset, hdr_dictionary):
    # fetch bands from input
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)
    R673 = data_for_wavelength(source_dataset, hdr_dictionary, 673)
    R445 = data_for_wavelength(source_dataset, hdr_dictionary, 445)

    global nodata_value
    nodata_value = -10000

    # Compute numerator
    numerator = R750 - R673

    # Compute denominator
    denominator = R750 + R673 - (2 * R445)

    # Mask the denominator, don't allow division by zero
    denominator = np.ma.masked_where(denominator == 0, denominator)

    # Do the calculation.
    mNDVI673 = numerator / denominator

    return mNDVI673


def calculate_mND705(source_dataset, hdr_dictionary):
    # fetch bands from input
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)
    R705 = data_for_wavelength(source_dataset, hdr_dictionary, 705)
    R445 = data_for_wavelength(source_dataset, hdr_dictionary, 445)

    global nodata_value
    nodata_value = -10000

    # Compute numerator
    numerator = R750 - R705

    # Compute denominator
    denominator = R750 + R705 - (2 * R445)

    # Mask the denominator, don't allow division by zero
    denominator = np.ma.masked_where(denominator == 0, denominator)

    # Do the calculation.
    mND705 = numerator / denominator

    return mND705


def calculate_DD(source_dataset, hdr_dictionary):
    # fetch bands from input
    R749 = data_for_wavelength(source_dataset, hdr_dictionary, 749)
    R720 = data_for_wavelength(source_dataset, hdr_dictionary, 720)
    R701 = data_for_wavelength(source_dataset, hdr_dictionary, 701)
    R672 = data_for_wavelength(source_dataset, hdr_dictionary, 672)

    global nodata_value
    nodata_value = -99

    # Do the calculation.
    DD = (R749 - R720) - (R701 - R672)

    return DD


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


def calculate_PSSRb(source_dataset, hdr_dictionary):
    # fetch bands from input
    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)
    R635 = data_for_wavelength(source_dataset, hdr_dictionary, 635)

    global nodata_value
    nodata_value = -99

    # Mask the R635 band, don't allow division by zero
    R635 = np.ma.masked_values(R635, 0.0)

    # Do the calculation.
    PSSRb = R800 / R635

    return PSSRb


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


def calculate_SR680(source_dataset, hdr_dictionary):
    # fetch bands from input
    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)
    R680 = data_for_wavelength(source_dataset, hdr_dictionary, 680)

    global nodata_value
    nodata_value = -99

    # Mask the R680 band, don't allow division by zero
    R680 = np.ma.masked_values(R680, 0.0)

    # Do the calculation.
    SR680 = R800 / R680

    return SR680


def calculate_SR700(source_dataset, hdr_dictionary):
    # fetch bands from input
    R675 = data_for_wavelength(source_dataset, hdr_dictionary, 675)
    R700 = data_for_wavelength(source_dataset, hdr_dictionary, 700)

    global nodata_value
    nodata_value = -99

    # Mask the R700 band, don't allow division by zero
    R700 = np.ma.masked_values(R700, 0.0)

    # Do the calculation.
    SR700 = R675 / R700

    return SR700


def calculate_SR705(source_dataset, hdr_dictionary):
    # fetch bands from input
    R750 = data_for_wavelength(source_dataset, hdr_dictionary, 750)
    R705 = data_for_wavelength(source_dataset, hdr_dictionary, 705)

    global nodata_value
    nodata_value = -99

    # Mask the R705 band, don't allow division by zero
    R705 = np.ma.masked_values(R705, 0.0)

    # Do the calculation.
    SR705 = R750 / R705

    return SR705


def calculate_SIPI(source_dataset, hdr_dictionary):
    # fetch bands from input
    R445 = data_for_wavelength(source_dataset, hdr_dictionary, 445)
    R680 = data_for_wavelength(source_dataset, hdr_dictionary, 680)
    R800 = data_for_wavelength(source_dataset, hdr_dictionary, 800)

    global nodata_value
    nodata_value = -100000

    # Mask the R800 band, don't allow division by zero
    R800 = np.ma.masked_where(R800 - R680 == 0, R800)

    # Do the calculation.
    SIPI = (R800 - R445) / (R800 - R680)

    return SIPI


def calculate_DATT(source_dataset, hdr_dictionary):
    # fetch bands from input
    R550 = data_for_wavelength(source_dataset, hdr_dictionary, 550)
    R672 = data_for_wavelength(source_dataset, hdr_dictionary, 672)
    R708 = data_for_wavelength(source_dataset, hdr_dictionary, 708)

    global nodata_value
    nodata_value = -100000

    # Mask the R708 band, don't allow division by zero
    R708 = np.ma.masked_where(R708 * R550 == 0, R708)

    # Do the calculation.
    DATT = R672 / (R708 - R550)

    return DATT


def calculate_ChlRI_green(source_dataset, hdr_dictionary):
    
    R450 = data_for_wavelength(source_dataset, hdr_dictionary, 450, tolerance=20)  # wavelength: 430 - 470
    R460 = data_for_wavelength(source_dataset, hdr_dictionary, 460, tolerance=20)  # wavelength: 440 - 480
    R550 = data_for_wavelength(source_dataset, hdr_dictionary, 550, tolerance=30)  # wavelength: 520 - 580
    R775 = data_for_wavelength(source_dataset, hdr_dictionary, 775, tolerance=25)  # wavelength: 750 - 800

    global nodata_value
    nodata_value = -100000

    # Mask the R460 band, don't allow division by zero
    R460 = np.ma.masked_where((R550 - R460) == 0, R460)

    ChlRI_green = ((R775 - R450) / (R550 - R460)) - 1

    return ChlRI_green


def calculate_ChlRI_red_green(source_dataset, hdr_dictionary):
    
    R450 = data_for_wavelength(source_dataset, hdr_dictionary, 450, tolerance=20)  # wavelength: 430 - 470
    R460 = data_for_wavelength(source_dataset, hdr_dictionary, 460, tolerance=20)  # wavelength: 440 - 480
    R717_5 = data_for_wavelength(source_dataset, hdr_dictionary, 717.5, tolerance=22.5)  # wavelength: 695 - 740
    R775 = data_for_wavelength(source_dataset, hdr_dictionary, 775, tolerance=25)  # wavelength: 750 - 800

    global nodata_value
    nodata_value = -10000

    # Mask the R460 band, don't allow division by zero
    R460 = np.ma.masked_where((R717_5 - R460) == 0, R460)

    ChlRI_red_green = ((R775 - R450) / (R717_5 - R460)) - 1

    return ChlRI_red_green


def calculate_CRI_green(source_dataset, hdr_dictionary):
    
    R510 = data_for_wavelength(source_dataset, hdr_dictionary, 510)
    R510 = np.ma.masked_values(R510, 0.0)

    R560 = data_for_wavelength(source_dataset, hdr_dictionary, 560, tolerance=10)  # wavelength: 550 - 570
    R560 = np.ma.masked_values(R560, 0.0)

    R775 = data_for_wavelength(source_dataset, hdr_dictionary, 775, tolerance=25)  # wavelength: 750 - 800

    global nodata_value
    nodata_value = -99

    CRI_green = ((1 / R510) - (1 / R560) * R775)

    return CRI_green


def calculate_CRI_red_edge(source_dataset, hdr_dictionary):
    
    R510 = data_for_wavelength(source_dataset, hdr_dictionary, 510)
    R510 = np.ma.masked_values(R510, 0.0)

    R705 = data_for_wavelength(source_dataset, hdr_dictionary, 705, tolerance=5)  # wavelength: 700 - 710
    R705 = np.ma.masked_values(R705, 0.0)

    R775 = data_for_wavelength(source_dataset, hdr_dictionary, 775, tolerance=25)  # wavelength: 750 - 800

    global nodata_value
    nodata_value = -99

    CRI_red_edge = ((1 / R510) - (1 / R705) * R775)

    return CRI_red_edge


def calculate_ARI(source_dataset, hdr_dictionary):
    
    R560 = data_for_wavelength(source_dataset, hdr_dictionary, 560, tolerance=10)  # wavelength: 550 - 570
    R560 = np.ma.masked_values(R560, 0.0)

    R705 = data_for_wavelength(source_dataset, hdr_dictionary, 705, tolerance=5)  # wavelength: 700 - 710
    R705 = np.ma.masked_values(R705, 0.0)

    R775 = data_for_wavelength(source_dataset, hdr_dictionary, 775, tolerance=25)  # wavelength: 750 - 800

    global nodata_value
    nodata_value = -99

    ARI = ((1 / R560) - (1 / R705) * R775)

    return ARI


def calculate_BGBO(source_dataset, hdr_dictionary):
    
    R495 = data_for_wavelength(source_dataset, hdr_dictionary, 495)

    R554 = data_for_wavelength(source_dataset, hdr_dictionary, 554)
    R554 = np.ma.masked_values(R554, 0.0)

    R635 = data_for_wavelength(source_dataset, hdr_dictionary, 635)
    R635 = np.ma.masked_values(R635, 0.0)

    global nodata_value
    nodata_value = -99

    # Do the calculation.
    BGBO = (R495 / R554) - (R495 / R635)

    return BGBO


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


