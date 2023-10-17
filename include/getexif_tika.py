import requests
from pathlib import Path
import json

def get_exif(image_path):
    """ Extract all possible image metadata calling the tika server.

    Args:
        image_path ([path object]): Pass a path to file or Path like object.
    """
    with open(image_path, 'rb') as f:
        tika_request = requests.put('http://localhost:9998/rmeta/text', f)
        tika_output = json.loads(tika_request.content)
        metadata = tika_output[0]
        
        for tagID, v in metadata.items():
            if tagID == ('X-TIKA:content'):
                v = ('\n\n::BEGIN Content::\n\n' + v.strip() 
                     + '\n\n::END Content::\n\n')
            if v == '':
                 print(tagID, ': ', 'Returned Empty')
            else:
                print(tagID,': ', v)
       

