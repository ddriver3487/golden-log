import tika
from tika import detector, parser, unpack
from pathlib import Path


file = str(
    r'C:\Users\thexa\Documents\Development\Python\goldenlog\testfiles\test.docx')

parsed_file = parser.from_file(file)
file_type = detector.from_file(file)
# Store content and remove white space
text = str(parsed_file["content"]).strip()

metadata = parsed_file["metadata"]

for k, v in metadata.items():
    print(k, ':', v)
