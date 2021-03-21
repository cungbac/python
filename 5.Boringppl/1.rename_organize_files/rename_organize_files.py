# import packages
import xlrd
import os
import openpyxl

# Pull video IDs and Titles from excel file
path = '/Users/bactran/Documents/1.Learning/2.Python/5.Boringppl/1.rename_organize_files/organizeVideos/database.xlsx'
workbook = openpyxl.load_workbook(path)

sheet_video_test = workbook['video-test']

first_column = sheet_video_test['A']
second_column = sheet_video_test['B']

video_Titles = []
for i in range(1,len(first_column)):
    video_Titles.append(first_column[i].value)

video_IDs = []
for i in range(1,len(second_column)):
    video_IDs.append(str(int(second_column[i].value)))

# Match IDs with Titles

id_dict = {}
for i in range(len(video_IDs)):
    # id_dict[video_IDs[i]] = video_Titles[i]
    id_dict.update({video_IDs[i]:video_Titles[i]})

# Rename files from IDs to Titles

# chdir = change directory (go to directory)
path_test = '/Users/bactran/Documents/1.Learning/2.Python/5.Boringppl/1.rename_organize_files/organizeVideos/test'
os.chdir(path= path_test) 

# get all file names in a directory
for f in os.listdir():
    for ids, titles in id_dict.items():
        video_name, extension = os.path.splitext(f)
        if ids == video_name:
            new_name = f'{titles}{extension}'
            os.rename(f, new_name)

print('Completed rename file ...')