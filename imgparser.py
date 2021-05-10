from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def img_parser(image_path):
    """ Extract all possible image metadata.

    Args:
        image_path ([path object]): Pass a path to file or Path like object.
    """
    img = Image.open(image_path)
    raw_exif = img.getexif()
    exif_table = {TAGS[k]: v for k, v in raw_exif.items()}
    for k, v in raw_exif.items():
        if k == 'MakerNote':
            pass
        else:
            print(k,v)
    
        
        