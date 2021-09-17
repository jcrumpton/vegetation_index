Create vegetation index (NDVI, ARI, etc.) geotiffs from hyperspectral images. Uses Python along with GDAL and numpy. See below for information on installing GDAL in [Windows](#Windows) or [Linux](#Linux). 


----------

## Usage

### Single Input File

To calculate a vegetation index for a single input file:
```
python calculate_vi.py K:\users\joec\06-01-2021\FL1 ARI
```
where FL1 is the hyperspectral ENVI data file and ARI is the vegetation index to calculate. See the `VALID_INDICES` list in [gri_util/vi_util.py](gri_util/vi_util.py) for the currently supported vegetation indices. The ENVI header file (`FL1.hdr` in this example) is expected to be in the same directory as the data file. The output file (`FL1_ARI.tif`) is saved to the same directory as the input file.


### Multiple Input Files
To calculate a vegetation index for several input files:
```
python calculate_and_merge_vi.py K:\users\joec\06-01-2021\FL* ARI
```

The interim output files are saved in the same directory as the output file. The final, merged output file is stored in the same directory as the script unless the `-o` option is used.

This script uses `gdal_merge.py` to merge the separate output files. The path to `gdal_merge.py` is set within [calculate_and_merge_vi.py](calculate_and_merge_vi.py):
```
PATH_TO_UTILS = r"venv\Lib\site-packages\osgeo_utils"
```
If you use a Python virtual environment named `venv`, you will not need to change this path.


----------

## Adding new Vegetation Indices

New vegetation indices are added in [gri_util/vi_util.py](gri_util/vi_util.py).

1. Add the new index's acronym to the list of valid indices.
2. Write a function to calculate the vegetation index. The name of the function must be calculate_ _acronym_ (without the space after the underscore). Use `calculate_NDVI` as a template.

```python
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
```

----------

## Installing GDAL

### Windows

You can download a GDAL wheel package from Christoph Gohlke's Unofficial Windows Binaries for Python Extension Packages: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal

The wheel can be installed from `cmd.exe`:
```
pip install GDAL‑3.3.1‑cp38‑cp38‑win_amd64.whl
```

Source: https://gis.stackexchange.com/questions/2276/installing-gdal-with-python-on-windows 

### Linux

```
sudo apt update
sudo apt install libpq-dev
sudo apt install gdal-bin
sudo apt install libgdal-dev
```

Source: https://askubuntu.com/questions/1267844/installing-libgdal-dev-on-ubuntu-20-04/1302161#1302161
