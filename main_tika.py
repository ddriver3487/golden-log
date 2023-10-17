from include import get_paths, get_exif, arg_parser

from pathlib import Path

p = arg_parser()

file_paths = get_paths(p)


for file in file_paths:
    meta = get_exif(file)
    print(meta)

    


