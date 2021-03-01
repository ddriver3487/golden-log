from pathlib import Path
from string import capwords as cw
import os
import sys
import subkeys
import requests
import json


def goldenlog():
    # Use Path to convert file paths to correct format
    absolute_path = (Path(sys.argv[1]))
    file_name = absolute_path.name
    # change working directory to the files parent folder
    os.chdir(absolute_path.parent)

    # execute cURL to return requests from Tika
    with open(file_name, 'rb') as f:
        tika_request = requests.put(
            'http://localhost:9998/rmeta/text', f)
        tika_output = json.loads(tika_request.content)
        metadata = tika_output[0]

    content = ''
    if ('X-TIKA:content') in metadata:
        content = metadata.pop('X-TIKA:content').strip()

    # remove case sensitivity from the keys in metadata to allow cross reference with sub list of keys
    lower_metadata = dict((k.lower(), v) for k, v in metadata.items())
    sub_key = subkeys.lowerkeys
    # new dictionary created from matched keys from the metadata also found in the subkey list.
    matched_keys = {k: v for k, v in lower_metadata.items() if k in sub_key}

    # Iterate key values so output is easy to read

    if sys.argv[2] == "FULL":
        for k, v in metadata.items():
            if v == '':
                print(k, ':', 'None')
            else:
                print(k, ':', v)
    else:
        for k, v in matched_keys.items():
            if v == '':
                print(cw(k), ':', 'None')
            else:
                print(cw(k), ':', v)

    if content != '':
        print("\n\n Below is the content of the file: ",
              file_name, '\n\n', content)


if __name__ == '__main__':
    goldenlog()
