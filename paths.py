import argparse
from pathlib import Path

# Create and add arguments to parser
parser = argparse.ArgumentParser(prog='paths',
                                    description='Create a list with path(s).')
parser.version = '1.0'
parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='Path to a directory or file.')
parser.add_argument('-a',
                    '--all',
                    action='store_true',
                    help='Return all metadata.')
parser.add_argument('-c',
                    '--content',
                    action='store_true',
                    help='Return content.')
parser.add_argument('-vr',
                    '--version',
                    action='version',
                    help='Return current parser version.')
args = parser.parse_args()

p = Path(args.Path)

def get(p):
    """[summary: If directory is passed, add all files to paths list.
        Otherwise, continue with file.

    Returns:
        [paths]: [List of PosixPath or WindowsPath objects]
    """
    paths = []
    if p.is_dir() is False:
        print('The path does not exist')
        sys.exit()
    else:
        for i in p.rglob('*'):
            if i.is_file():
                paths.append(str(i))


                    # paths.append(training_folder.joinpath(sample_data.name)
                    # sample_data.rename(training_target)
                    # data_list.remove(sample_data)
    for x in enumerate(paths):
        print(x)

get(p)

