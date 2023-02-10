from zipfile import ZipFile
from pathlib import Path

# Path('/home/anton/Загрузки/')

with ZipFile('/home/anton/Загрузки/my_arc.zip', 'w') as my_zip:
    for file in Path('/home/anton/Загрузки/first').iterdir():
        print(file)
        my_zip.write(file)

# with ZipFile('/home/anton/Загрузки/dog.zip') as myzip:
#     myzip.extractall('/home/anton/Загрузки/unzip')

