# CR2 to JPG
A simple Python script to convert CR2 photos to JPG and retain timestamps.

## Instructions

1. Clone or download
2. Install required packages with `pip install`
2. Set permissions to execute `chmod +x cr2-to-jpg.py`
3. Run the script and pass source and destination folders, for example: `./cr2-to-jpg.py --source ~/Desktop/raw --destination ~/Desktop/converted`

## Requirements

Script requires the following packages:

- `rawkit` from https://pypi.python.org/pypi/rawkit/0.5.0
- `numpy` from https://pypi.python.org/pypi/numpy
- `PIL` from https://pypi.python.org/pypi/Pillow

These are now set in requirements.txt for easier install.

## Notes

This is just something I put together for my own use after having a look online and on Stack Overflow at CR2 conversion.

I needed it to cut the time of uploading 1,000+ raw CR2 photos to Google Photos.

There are many other ways to do this, including Photoshop actions if you're after a visual/gui based approach. There are also bash scripts that can achieve similar results, but I wanted to tinker and play with Python.

Thanks to @simoncoulton for some suggested tweaks and updates.
