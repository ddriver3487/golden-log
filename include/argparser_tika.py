import argparse
from pathlib import Path
# Create and add arguments to parser
def arg_parser():
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
    
    return Path(args.Path)