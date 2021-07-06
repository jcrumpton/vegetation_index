import glob
import argparse
import pathlib
import os

# path to gdal_merge.py in WinPython
# C:\Utilities\WPy64-3890\python-3.8.9.amd64\Lib\site-packages\osgeo_utils\
PATH_TO_UTILS = "C:\\Utilities\\WPy64-3890\\python-3.8.9.amd64\\Lib\\site-packages\\osgeo_utils\\" 

if __name__ == "__main__":
    
    # input_pattern = "K:\\users\\joec\\10-30-2020\\HSI_Deliverables\\2B_FL*"
    # no_extensions = True

    parser = argparse.ArgumentParser(description='Create RGB geotiff from a hyperspectral input file')

    parser.add_argument('input_filename_pattern',
                        metavar='input_filename_pattern',
                        type=str,
                        help='the hyperspectral files to use as input')

    args = parser.parse_args()

    input_filename_pattern = args.input_filename_pattern
    files_to_process = glob.glob(input_filename_pattern)
    no_extensions = "".__eq__(pathlib.Path(input_filename_pattern).suffix)

    new_list=[]
    if no_extensions:
        for each in files_to_process:
            if not pathlib.Path(each).suffix:
                new_list.append(each)
        files_to_process = new_list
    # print(files_to_process)

    for each in files_to_process:
        command = f"python extract_RGB_from_hyperspectral.py {each}"
        # print(command)
        print(os.popen(command).read())

    input_pattern = input_filename_pattern + "_RGB.tif"

    files_to_process = glob.glob(input_pattern)
    # print(files_to_process)

    files_string = " ".join(files_to_process)

    command=f"python {PATH_TO_UTILS}gdal_merge.py -o merged_RGB.tif -of gtiff " + files_string
    print(os.popen(command).read())
    