import sys
import argparse
import os.path, glob


if __name__ == "__main__":
    
    input_pattern = "./HSI_data/2B_FL*"
    
    no_extensions = True

    # parser = argparse.ArgumentParser(description='Create RGB geotiff from a hyperspectral input file')

    # parser.add_argument('input_filename',
    #                     metavar='input_filename',
    #                     type=str,
    #                     help='the hyperspectral file to use as input')

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

    for each in files_to_process:
        command = f"python3 extract_RGB_from_hyperspectral.py {each}"
        #print(command)
        print(os.popen(command).read())

    input_pattern = input_pattern + "_RGB.tif"

    files_to_process = glob.glob(input_pattern)

    print(files_to_process)

    files_string = " ".join(files_to_process)

    command="gdal_merge.py -o merged_RGB.tif -of gtiff " + files_string
    print(os.popen(command).read())
    