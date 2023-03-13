from PIL import Image
from PIL.ExifTags import TAGS
import sys
import requests
from io import BytesIO
import pytesseract
import argparse

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=False, help="URL of the image")
ap.add_argument("-f", "--file", required=False, help="Path to the image file")
ap.add_argument("-o", "--output", required=False, help="Output file path for OCR text")
ap.add_argument("-l", "--language", required=False, default="eng", help="Language for OCR (default='eng')")

# parse the arguments
args = vars(ap.parse_args())

# check if the image path is provided
if not args["url"] and not args["file"]:
    print("Please provide either the image URL or the image file path.")
    sys.exit()

# check if the image path is a URL or a local file
if args["url"]:
    # download the image from the URL
    response = requests.get(args["url"])
    # read the image data from the downloaded bytes
    image = Image.open(BytesIO(response.content))
else:
    # read the image data from the local file
    image = Image.open(args["file"])

# extract other basic metadata
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

print("Basic Image Information:")
for label,value in info_dict.items():
    print(f"{label:25}: {value}")
    
# extract EXIF data
exifdata = image.getexif()

print("\nEXIF Data:")
# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")

# perform OCR on the image
text = pytesseract.image_to_string(image, lang=args["language"])

print("\nOCR Output:")
print(text)

# write OCR output to a file if output path is provided
if args["output"]:
    with open(args["output"], "w") as f:
        f.write(text)
    print(f"OCR output written to {args['output']}.")
