import sys
from pathlib import Path

def get_paths(p):
    """[summary: If directory is passed, add all files to paths list.
        Otherwise, continue with file.

    Returns:
        [paths]: [List of PosixPath or WindowsPath objects]
    """
    file_paths = list()
    if p.is_dir() is False:
        print('The path does not exist')
        sys.exit()
    else:
        for f in p.rglob('*'):   
            if f.is_file(): 
                file_paths.append((f))
    return file_paths
