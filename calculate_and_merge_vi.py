import sys
import argparse
import os.path, glob


if __name__ == "__main__":
    
    input_pattern = "./HSI_data/2B_FL*"
    no_extensions = True
    vi = "NDVI"

    # parser = argparse.ArgumentParser(description='Create RGB geotiff from a hyperspectral geotif')

    # parser.add_argument('input_filename',
    #                     metavar='input_filename',
    #                     type=str,
    #                     help='the hyperspectral geotif file to use as input')

    # args = parser.parse_args()

    # input_filename = args.input_filename

    files_to_process = glob.glob(input_pattern)

    new_list=[]
    if no_extensions:
        for each in files_to_process:
            parts = os.path.splitext(each)
            if parts[1]=='':
                new_list.append(each)
        files_to_process = new_list


    print(files_to_process)

    # for each in files_to_process:
    #     command = f"python3 calculate_vi.py {each} {vi}"
    #     #print(command)
    #     print(os.popen(command).read())

    input_pattern = input_pattern + f"_{vi}.tif"

    files_to_process = glob.glob(input_pattern)

    print(files_to_process)

    files_string = " ".join(files_to_process)

    command=f"gdal_merge.py -n -99 -a_nodata -99 -o merged_{vi}.tif -of gtiff -ot Float32 " + files_string
    print(os.popen(command).read())
    