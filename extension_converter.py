import os

#please change the location in which your .jp images are located
my_path = "E:/some_folder_name/main_folder"


#get a list of all files and folders
file_name_list = os.listdir(my_path)

#loop over every file in the main folder
for file_name in file_name_list:
    if file_name.lower().endswith(".jpg"):
        print('Coverting "{}" to png....'.format(file_name))

        #get full path name and change the .jpg to .png

        full_file_name = os.path.join(my_path, file_name)
        new_file_name = full_file_name[0:len(full_file_name)-4] + ".png"
        os.rename(full_file_name, new_file_name)
