from getpaths_tika import get_paths
from getexif_tika import get_exif
from argparser_tika import arg_parser
from pathlib import Path


p = arg_parser()

file_paths = get_paths(p)


for file in file_paths:
    meta = get_exif(file)
    print(meta)

    


