import sys
import argparse
import pathlib
import glob
import os
import gri_util

# path to gdal_merge.py 
# in WinPython: C:\Utilities\WPy64-3890\python-3.8.9.amd64\Lib\site-packages\osgeo_utils
PATH_TO_UTILS = r"venv\Lib\site-packages\osgeo_utils"

if __name__ == "__main__":
    
    # input_filename_pattern = "K:\\users\\joec\\10-30-2020\\HSI_Deliverables\\2B_FL*"
    # vegetation_index = "NDVI"

    parser = argparse.ArgumentParser(description='Create vegetation index geotiff from hyperspectral input files')
    
    parser.add_argument('input_filename_pattern',
                        metavar='input_filename_pattern',
                        type=str,
                        help='the hyperspectral files to use as input')

    parser.add_argument('vegetation_index',
                        metavar='vegetation_index',
                        type=str,
                        help='the vegetation index to calculate')

    parser.add_argument('-o',
                        metavar='output_filename',
                        type=str,
                        required=False,
                        help='output filename')   
    
    args = parser.parse_args()

    vegetation_index = args.vegetation_index
    if vegetation_index not in gri_util.VALID_INDICES:
        print(f'{vegetation_index} is not a valid index to calculate')
        print(f'Choices are: {gri_util.VALID_INDICES}')
        sys.exit(1)

    output_filename = args.o
    if output_filename is None:
        output_filename = f"merged_{vegetation_index}.tif"
    #print(f"output_filename: {output_filename}")
    
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
        command = f"python calculate_vi.py {each} {vegetation_index}"
        print(os.popen(command).read())

    input_filename_pattern = input_filename_pattern + f"_{vegetation_index}.tif"
    files_to_process = glob.glob(input_filename_pattern)
    # print(files_to_process)

    files_string = " ".join(files_to_process)
    gdal_merge = pathlib.Path(PATH_TO_UTILS).joinpath('gdal_merge.py')
    nodata_value = gri_util.retrieve_nodata_value(files_to_process[0])
    if nodata_value:
        command=f"python {gdal_merge} -n {nodata_value} -a_nodata {nodata_value} -o {output_filename} -of gtiff -ot Float32 " + files_string
    else:
        command=f"python {gdal_merge} -o {output_filename} -of gtiff -ot Float32 " + files_string
    print(os.popen(command).read())
    