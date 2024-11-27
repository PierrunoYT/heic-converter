# HEIC Converter

## Overview
A user-friendly Python application to convert HEIC (High Efficiency Image File Format) images to other common image formats with a Windows-friendly GUI.

## Features
- Interactive file/directory selection
- Support for converting single or multiple HEIC files
- Choose from multiple output formats (PNG, JPEG, BMP, TIFF)
- Windows-friendly file dialogs
- Simple, intuitive interface

## Prerequisites
- Python 3.7+
- Windows operating system recommended

## Installation
1. Clone the repository
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Simply run the script:
```
python heic_converter.py
```

### Conversion Process
1. A file dialog will open to select HEIC file(s) or a directory
2. Choose the desired output format
3. Select an output directory
4. Converted images will be saved to the chosen directory

## Output
- Converted images are saved in the selected output directory
- Original file names are preserved with new extensions

## Supported Formats
- Input: HEIC
- Output: PNG, JPEG, BMP, TIFF

## Troubleshooting
- Ensure you have the latest version of Python
- Check that all dependencies are installed
- Verify file and directory permissions

## License
MIT License - See LICENSE file for details

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.