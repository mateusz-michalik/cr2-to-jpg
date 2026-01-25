#!/usr/bin/env python

# import what we need
import numpy
import os
import argparse
from PIL import Image
from rawkit import raw

# params
parser = argparse.ArgumentParser(description='Convert CR2 to JPG')
parser.add_argument('files', metavar='FILE', nargs='+', help='CR2 files to convert')
parser.add_argument('--prefix', default='', help='Output path prefix (e.g., "output/" for output directory)')
parser.add_argument('--postfix', default='', help='Output filename postfix (e.g., "_converted")')
args = parser.parse_args()

# create output directory if prefix specified and doesn't exist
if args.prefix and not os.path.exists(args.prefix):
    os.makedirs(args.prefix)

# converter function which iterates through list of files
def convert_cr2_to_jpg(raw_images, prefix='', postfix=''):
    for raw_image in raw_images:
        print "Converting the following raw image: " + raw_image + " to JPG"

        # file vars
        file_name = os.path.basename(raw_image)
        file_without_ext = os.path.splitext(file_name)[0]
        file_timestamp = os.path.getmtime(raw_image)

        # parse CR2 image
        raw_image_process = raw.Raw(raw_image)
        buffered_image = numpy.array(raw_image_process.to_buffer())

        # check orientation due to PIL image stretch issue
        if raw_image_process.metadata.orientation == 0:
            jpg_image_height = raw_image_process.metadata.height
            jpg_image_width = raw_image_process.metadata.width
        else:
            jpg_image_height = raw_image_process.metadata.width
            jpg_image_width = raw_image_process.metadata.height

        # prep JPG details - use prefix for output dir, or same dir as input
        output_dir = prefix if prefix else os.path.dirname(raw_image)
        if output_dir and not output_dir.endswith(os.sep):
            output_dir += os.sep
        jpg_image_location = output_dir + file_without_ext + postfix + '.jpg'
        jpg_image = Image.frombytes('RGB', (jpg_image_width, jpg_image_height), buffered_image)
        jpg_image.save(jpg_image_location, format="jpeg")

        # update JPG file timestamp to match CR2
        os.utime(jpg_image_location, (file_timestamp,file_timestamp))

        # close to prevent too many open files error
        jpg_image.close()
        raw_image_process.close()

# call function
if __name__ == "__main__":
    convert_cr2_to_jpg(args.files, args.prefix, args.postfix)
