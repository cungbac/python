# import packages
import os
import openpyxl
import pathlib

# import excel file
path = '/Users/bactran/Documents/1.Learning/2.Python/5.Boringppl/1.rename_organize_files/organizeVideos/database.xlsx'
workbook = openpyxl.load_workbook(path)

worksheet = workbook['main-genres']

first_column = worksheet['A']
genres = []
for i in range(1,len(first_column)):
    genres.append(first_column[i].value)

genres_dict = {}

path_test = '/Users/bactran/Documents/1.Learning/2.Python/5.Boringppl/1.rename_organize_files/organizeVideos/test'

for i in genres:
    genres_dict[i] = []

for video in os.listdir(path_test):
    for genre, videos in genres_dict.items():
        if genre in video:
            videos.append(video)

def pick_directory(value):
    for genre, videos in genres_dict.items():
        for video in videos:
            if value in video:
                return genre
    return "Others"

# go to test directory
os.chdir(path_test)

for f in os.scandir():
    if f.is_dir():
        continue
    f_from = pathlib.Path(f)
    directory = pick_directory(str(f_from))
    dirPath = pathlib.Path(directory)
    f_to = dirPath.joinpath(f_from)
    print(f_to)

