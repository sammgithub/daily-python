######### SERAJ Mostafa @UMBC #########
###### unzip all files in a dir  ######

import os
import zipfile

location = '\your\path\'
for path, dir_list, file_list in os.walk(location):
    for file_name in file_list:
        if file_name.endswith(".zip"):
            abs_file_path = os.path.join(path, file_name)

            # The following three lines of code are only useful if 
            # a. the zip file is to unzipped in it's parent folder and 
            # b. inside the folder of the same name as the file

            parent_path = os.path.split(location)[0]
            output_folder_name = os.path.splitext('\location\unzipped\')[0]
            output_path = os.path.join(parent_path, output_folder_name)

            zip_obj = zipfile.ZipFile(abs_file_path, 'r')
            zip_obj.extractall(output_path)
            zip_obj.close()
