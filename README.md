# Imageinfo
This is a Python code that allows you to extract information from an image and perform Optical Character Recognition (OCR) on it. Here's how you can use it:

    Install required packages:
    Before using this code, you need to install some required packages. The code uses Pillow, requests, pytesseract, and argparse. You can install these packages by running the following command in your command prompt or terminal:

pip install Pillow requests pytesseract argparse

    Provide the image source:
    The code allows you to provide the image either from a URL or a local file. To provide the image source, you can use the following arguments:

    -u or --url: URL of the image.
    -f or --file: Path to the image file.

If you don't provide the image source, the code will display an error message and exit.

    Optional image processing options:
    The code provides some optional image processing options that you can use to enhance the image before performing OCR. The following options are available:

    -b or --brightness: Adjust the brightness of the image. You can provide a float value between 0.0 and 1.0 to decrease the brightness, or a value greater than 1.0 to increase the brightness.
    -c or --contrast: Adjust the contrast of the image. You can provide a float value between 0.0 and 1.0 to decrease the contrast, or a value greater than 1.0 to increase the contrast.
    -s or --sharpness: Adjust the sharpness of the image. You can provide a float value between 0.0 and 1.0 to decrease the sharpness, or a value greater than 1.0 to increase the sharpness.
    -g or --gray: Convert the image to grayscale.

    Optional OCR language:
    By default, the code uses English as the OCR language. You can change this by using the -l or --language argument and specifying the language code. For example, -l deu will use German as the OCR language.

    Optional output file:
    The code allows you to save the OCR output to a file. You can use the -o or --output argument and specify the output file path. For example, -o output.txt will save the OCR output to a file named "output.txt".

    Run the code:
    After providing the required and optional arguments, you can run the code in your command prompt or terminal by running the following command:

php

python <path_to_file>/image_ocr.py -u <image_url> -b <brightness> -c <contrast> -s <sharpness> -g -l <language> -o <output_file>

Or:

php

python <path_to_file>/image_ocr.py -f <image_file_path> -b <brightness> -c <contrast> -s <sharpness> -g -l <language> -o <output_file>

Note: Replace <path_to_file> with the path to the directory where the file is saved, <image_url> with the URL of the image, <image_file_path> with the path to the image file, <brightness>, <contrast>, and <sharpness> with the desired values for each option, <language> with the language code, and <output_file> with the desired name for the output file.

After running the code, you should see the basic information of the image, the EXIF data, and the OCR output printed on the screen.
