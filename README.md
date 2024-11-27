# HEIC Converter

## Overview
A powerful, user-friendly Python application to convert HEIC (High Efficiency Image File Format) images to other common image formats with a Windows-friendly GUI.

## Features
- Interactive file/folder selection
- Convert single or multiple HEIC files
- Batch conversion from entire directories
- Support for multiple output formats (PNG, JPEG, BMP, TIFF)
- Detailed error reporting
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
1. Choose between selecting:
   - A folder containing HEIC images
   - Individual HEIC files
2. Select the desired output format
3. Choose an output directory
4. Converted images will be saved to the selected directory

## Conversion Options
- Input: 
  * Single HEIC files
  * Entire folders with HEIC images (recursive search)
- Output Formats: PNG, JPEG, BMP, TIFF
- Error Handling: 
  * Detailed error reporting
  * Option to view conversion errors

## Advanced Features
- Recursive directory scanning
- Preserves original file names
- Supports nested folder structures

## Troubleshooting
- Ensure you have the latest version of Python
- Check that all dependencies are installed
- Verify file and directory permissions
- Review error messages for specific conversion issues

## Performance
- Efficiently converts multiple images
- Minimal memory footprint
- Fast conversion process

## License
MIT License - See LICENSE file for details

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Example Scenarios
1. Convert a single HEIC image
2. Batch convert all HEIC images in a folder
3. Convert HEIC images from a folder with subfolders

## Known Limitations
- Large image files may take longer to convert
- Extremely complex HEIC files might encounter conversion issues