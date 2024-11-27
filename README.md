# HEIC Converter

## Overview
This Python script provides a simple command-line tool to convert HEIC (High Efficiency Image File Format) images to other common image formats like PNG, JPEG, BMP, and TIFF.

## Features
- Convert single HEIC files or entire directories
- Support for multiple output formats
- Easy-to-use command-line interface
- Error handling for file conversions

## Prerequisites
- Python 3.7+
- pillow-heif library

## Installation
1. Ensure you have Python installed
2. Install required dependencies:
   ```
   pip install pillow-heif
   ```

## Usage

### Basic Usage
Convert a single HEIC file to PNG:
```
python heic_converter.py path/to/image.heic
```

### Advanced Usage
Convert a directory of HEIC files to JPEG:
```
python heic_converter.py path/to/heic/directory -f jpg
```

### Command-line Options
- `input`: Path to HEIC file or directory (required)
- `-f, --format`: Output image format (default: png)
  - Supported formats: png, jpg, jpeg, bmp, tiff
- `-o, --output`: Custom output directory for converted images

## Examples
```
# Convert single file to default PNG
python heic_converter.py image.heic

# Convert directory to JPEG
python heic_converter.py heic_images/ -f jpg

# Specify custom output directory
python heic_converter.py heic_images/ -o converted_images
```

## Troubleshooting
- Ensure you have the latest version of pillow-heif
- Check file permissions
- Verify input file/directory exists

## License
MIT License