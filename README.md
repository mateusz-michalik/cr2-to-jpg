# CR2 to JPG
A simple Python script to convert CR2 photos to JPG and retain timestamps.

## Instructions

1. Clone or download
2. Install required packages with `pip install -r requirements.txt`
3. Set permissions to execute `chmod +x cr2-to-jpg.py`
4. Run the script and pass CR2 files as arguments

## Usage

```bash
# Convert a single file (output goes to same directory)
./cr2-to-jpg.py photo.CR2

# Convert multiple files using shell glob
./cr2-to-jpg.py ~/Desktop/raw/*.CR2

# Output to a specific directory using --prefix
./cr2-to-jpg.py --prefix ~/Desktop/converted/ ~/Desktop/raw/*.CR2

# Add a postfix to output filenames (e.g., photo_web.jpg)
./cr2-to-jpg.py --postfix _web ~/Desktop/raw/*.CR2

# Combine prefix and postfix
./cr2-to-jpg.py --prefix ~/Desktop/converted/ --postfix _small ~/Desktop/raw/*.CR2
```

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
