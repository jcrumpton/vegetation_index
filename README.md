Create vegetation index (NDVI, ARI, etc) geotiffs from hyperspectral images. Uses Python and GDAL. See below for information on installing GDAL in [Windows](#Windows) or [Linux](#Linux). 



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
python calculate_vi_and_merge.py K:\users\joec\06-01-2021\FL* ARI
```
This script uses `gdal_merge.py` to merge the separate output files. The path to `gdal_merge.py` is set within `calculate_vi_and_merge.py`:
```
PATH_TO_UTILS = r"venv\Lib\site-packages\osgeo_utils"
```
If you use a Python virtual environment named `venv`, you will not need to change this path.


----------

## Adding new indices


----------

## Installing GDAL

### Windows

You can download a GDAL wheel package from Christoph Gohlke's Unofficial Windows Binaries for Python Extension Packages: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal

The wheel can be installed from `cmd.exe`:
```
pip install GDAL‑3.3.1‑cp38‑cp38‑win_amd64.whl
```

Source: https://gis.stackexchange.com/questions/2276/installing-gdal-with-python-on-windows 

## Linux

```
sudo apt update
sudo apt install libpq-dev
sudo apt install gdal-bin
sudo apt install libgdal-dev
```

Source: https://askubuntu.com/questions/1267844/installing-libgdal-dev-on-ubuntu-20-04/1302161#1302161
