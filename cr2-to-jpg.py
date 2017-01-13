#!/usr/bin/env python

# import what we need
import numpy
import os
import glob
import time
import argparse
from PIL import Image
from rawkit.raw import Raw

# params
parser = argparse.ArgumentParser(description='Convert CR2 to JPG')
parser.add_argument('-s', '--source', help='Source folder of CR2 files', required=True)
parser.add_argument('-d', '--destination', help='Destination folder for converted JPG files', required=True)
args = parser.parse_args()

# dirs and files
raw_file_type = ".CR2"
raw_dir = args.source + '/'
converted_dir = args.destination + '/'
raw_images = glob.glob(raw_dir + '*' + raw_file_type)

# converter function which iterates through list of files
def convert_cr2_to_jpg(raw_images):
    for raw_image in raw_images:
        print "Converting the following raw image: " + raw_image + " to JPG"

        # file vars
        file_name = os.path.basename(raw_image)
        file_without_ext = os.path.splitext(file_name)[0]
        file_timestamp = os.path.getmtime(raw_image)

        # parse CR2 image
        raw_image_process = Raw(raw_image)
        buffered_image = numpy.array(raw_image_process.to_buffer())

        # check orientation due to PIL image stretch issue
        if raw_image_process.metadata.orientation == 0:
            jpg_image_height = raw_image_process.metadata.height
            jpg_image_width = raw_image_process.metadata.width
        else:
            jpg_image_height = raw_image_process.metadata.width
            jpg_image_width = raw_image_process.metadata.height

        # prep JPG details
        jpg_image_location = converted_dir + file_without_ext + '.jpg'
        jpg_image = Image.frombytes('RGB', (jpg_image_width, jpg_image_height), buffered_image)
        jpg_image.save(jpg_image_location, format="jpeg")

        # update JPG file timestamp to match CR2
        os.utime(jpg_image_location, (file_timestamp,file_timestamp))

        # close to prevent too many open files error
        jpg_image.close()
        raw_image_process.close()

# call function
convert_cr2_to_jpg(raw_images)
