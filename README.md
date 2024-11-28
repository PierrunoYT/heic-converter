# heic-converter

A modern, dual-interface HEIC image converter that provides both a web interface and a Python CLI application to convert HEIC (High Efficiency Image File Format) images to common formats like PNG, JPEG, BMP, and TIFF.

## Features
- 🌐 Modern web interface for easy drag-and-drop conversion
- 🖥️ Native Python GUI for desktop usage
- 📁 Interactive file/folder selection
- 🔄 Batch conversion support
- 📦 Multiple output formats (PNG, JPEG, BMP, TIFF)
- 🚀 Fast and efficient conversion
- 📝 Detailed error reporting
- 🪟 Windows-friendly file dialogs
- 🎯 Simple, intuitive interface

## Prerequisites
- Python 3.7+
- Modern web browser for web interface
- Windows operating system recommended for desktop GUI

## Installation

### From Source
1. Clone the repository:
```bash
git clone https://github.com/yourusername/heic-converter.git
cd heic-converter
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Interface
1. Start the web server:
```bash
python -m http.server
```
2. Open your browser and navigate to `http://localhost:8000`
3. Use the drag-and-drop interface or file selector to choose HEIC files
4. Select your desired output format
5. Click convert and download your converted images

### Python GUI
Run the desktop application:
```bash
python heic_converter.py
```

#### Conversion Process
1. Choose between:
   - A folder containing HEIC images
   - Individual HEIC files
2. Select the desired output format
3. Choose an output directory
4. Converted images will be saved to the selected directory

## Development Setup
1. Clone the repository
2. Install development dependencies:
```bash
pip install -r requirements.txt
```
3. Run tests:
```bash
python -m pytest test_heic_converter.py
```

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
- Web-based conversion interface
- Drag-and-drop support

## Troubleshooting
- Ensure you have the latest version of Python
- Check that all dependencies are installed
- Verify file and directory permissions
- Review error messages for specific conversion issues
- For web interface issues, ensure your browser is up to date

## Performance
- Efficiently converts multiple images
- Minimal memory footprint
- Fast conversion process
- Optimized for both web and desktop interfaces

## License
MIT License - See [LICENSE](LICENSE) file for details

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

To contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Example Scenarios
1. Convert a single HEIC image through the web interface
2. Batch convert all HEIC images in a folder using the desktop GUI
3. Convert HEIC images from a folder with subfolders
4. Drag and drop multiple HEIC files for conversion

## Known Limitations
- Large image files may take longer to convert
- Extremely complex HEIC files might encounter conversion issues
- Web interface requires a modern browser with JavaScript enabled