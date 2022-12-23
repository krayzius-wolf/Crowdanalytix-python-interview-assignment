import urllib.request
import os
import base64
import json
import argparse
from urllib.error import HTTPError
from PIL import Image


def load_im(URL):
    '''
    Image is downloaded from given URL.Might not always return due to 403 error(prevents bot requests).
    Url is validated.
    '''

    try:
        path = os.getcwd() + '\\image.jpg'
        f = open(path, 'wb')
        f.write(urllib.request.urlopen(URL).read())
        f.close()
        img = Image.open(path)
        return img
    except HTTPError as e:
        print(e)
        print('Please enter a valid URL')


def val(img):
    '''
    Format is checked. Image is also verified and checked for corruption.
    '''

    if img.format.lower() not in [
        'png',
        'jpg',
        'jpeg',
        'tiff',
        'bmp',
        'gif',
        ]:
        print('Invalid image')
        exit()
    try:
        img.verify()
    except Exception:

        print('Invalid image')


def json_data():
    '''
    Required output is generated. Thumbnail method is used to preserve AR and reduce image to 250*250.
    The base64.b64encode() method is used to encode the thumbnail image as a binary string.
    '''

    path = os.getcwd() + '\\image.jpg'
    img = Image.open(path)
    originial_resolution = img.size
    original_size = os.path.getsize(path) / 1024

    MAX_SIZE = (250, 250)
    img.thumbnail(MAX_SIZE)
    img.save('thumbnail.png')

    thumbnail_path = os.getcwd() + '\\thumbnail.png'
    img1 = Image.open(thumbnail_path)
    thumbnail_resolution = img1.size
    thumbnail_size = os.path.getsize(thumbnail_path) / 1024
    with open('thumbnail.png', 'rb') as img_file:
        thumbnail_base64 = base64.b64encode(img_file.read())
    thumbnail_base64 = str(thumbnail_base64)
    output = {
        'thumbnail_base64': thumbnail_base64,
        'thumbnail_path': thumbnail_path,
        'original_size': original_size,
        'thumbnail_size': thumbnail_size,
        'original_resolution': originial_resolution,
        'thumbnail_resolution': thumbnail_resolution,
        }
    output = json.dumps(output)
    return output


def main():
    '''
    Above created functions are executed with URL input received.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('URL', type=str)
    args = parser.parse_args()
    o = load_im(args.URL)
    val(o)
    print(json_data())


main()
