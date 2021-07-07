import numpy as np
from gri_util.hyper_util import closest_wavelength, band_for_wavelength, extract_band

nodata_value = None


# to add a new vegetation index:
#   1) add acronym to VALID_INDICES
#   2) write a compute_<acronym> method
#
VALID_INDICES = ['ARI','mARI','NDVI', 'gNDVI']


def calculate_NDVI(source_dataset, hdr_dictionary):
   
    # fetch bands from input
    red_freq = closest_wavelength(hdr_dictionary, 670)
    red_band_number = band_for_wavelength(hdr_dictionary, red_freq)
    red, _ = extract_band(red_band_number, source_dataset)
    
    nir_freq = closest_wavelength(hdr_dictionary, 860)
    nir_band_number = band_for_wavelength(hdr_dictionary, nir_freq)
    nir, _ = extract_band(nir_band_number, source_dataset)

    global nodata_value
    nodata_value = -99

    # Mask the bands
    red = np.ma.masked_where(nir + red == 0, red)  # Don't allow division by zero

    # Do the calculation.
    NDVI = (nir - red) / (nir + red)

    return NDVI


# def calculate_gNDVI():
#     # fetch bands from input
#     R550_band = band_by_frequency[550]
#     R550 = src_ds.GetRasterBand(R550_band).ReadAsArray()
#     R750_band = band_by_frequency[750]
#     R750 = src_ds.GetRasterBand(R750_band).ReadAsArray()

#     global nodata_value
#     nodata_value = -99

#     # Mask the R550 band.
#     R550 = np.ma.masked_where(R550 + R750 == 0, R550)

#     # Do the calculation.
#     gNDVI = (R750 - R550) / (R750 + R550)

#     return gNDVI


# def calculate_ARI():
#     # fetch bands from input
#     R550_band = band_by_frequency[550]
#     R550 = src_ds.GetRasterBand(R550_band).ReadAsArray()
#     R550 = np.ma.masked_values(R550, 0.0)

#     R700_band = band_by_frequency[700]
#     R700 = src_ds.GetRasterBand(R700_band).ReadAsArray()
#     R700 = np.ma.masked_values(R700, 0.0)

#     global nodata_value
#     nodata_value = -99

#     # Do the calculation.
#     ARI = (1/R550) - (1/R700)

#     return ARI


# def calculate_mARI():
#     # fetch bands from input
#     R550_band = band_by_frequency[550]
#     R550 = src_ds.GetRasterBand(R550_band).ReadAsArray()
#     R550 = np.ma.masked_values(R550, 0.0)

#     R700_band = band_by_frequency[700]
#     R700 = src_ds.GetRasterBand(R700_band).ReadAsArray()
#     R700 = np.ma.masked_values(R700, 0.0)

#     R800_band = band_by_frequency[799]
#     R800 = src_ds.GetRasterBand(R800_band).ReadAsArray()

#     global nodata_value
#     nodata_value = -99

#     # Do the calculation.
#     mARI = R800 * ((1/R550) - (1/R700))

#     return mARI