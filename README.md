# HEIC Converter

A modern, dual-interface HEIC image converter that provides both a web interface and a Python CLI application to convert HEIC (High Efficiency Image File Format) images to common formats like PNG, JPEG, WebP, and more.

## Features
- 🌐 Modern web interface for easy drag-and-drop conversion
- 🖥️ Native Python GUI for desktop usage
- 📁 Interactive file/folder selection
- 🔄 Batch conversion support
- 📦 Multiple output formats (PNG, JPEG, WebP)
- 🚀 Fast and efficient conversion
- 📝 Detailed error reporting
- 🪟 Windows-friendly file dialogs
- 🎯 Simple, intuitive interface
- 📊 Real-time conversion progress tracking

## Prerequisites
- Python 3.7+
- Modern web browser for web interface
- Windows operating system recommended for desktop GUI

## Installation

### From Source
1. Clone the repository:
```bash
git clone https://github.com/PierrunoYT/heic-converter.git
cd heic-converter
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Interface (Quick Start)
1. Open a terminal/command prompt in the project directory
2. Start the web server:
```bash
python server.py
```
3. Open your web browser and go to: `http://localhost:5000`
   - If the page doesn't load, make sure no other application is using port 5000
   - You should see the HEIC Converter web interface
4. Use the interface to convert images:
   - Click the "Choose Files" button or drag & drop HEIC files directly onto the interface
   - Select your desired output format (PNG, JPEG, or WebP)
   - Click "Convert" and watch the progress bar
   - Download individual files or use "Download All" for batch downloading

#### Web Interface Troubleshooting
- If the server fails to start:
  - Make sure you're in the correct directory (where server.py is located)
  - Verify Python and all dependencies are installed (`pip install -r requirements.txt`)
  - Check if port 5000 is already in use (try closing other applications)
- If the web interface doesn't load:
  - Ensure the server is running (you should see a message in the terminal)
  - Try accessing with different browsers (Chrome, Firefox, or Edge recommended)
  - Check your firewall settings if accessing from another device

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
- Output Formats: PNG, JPEG, WebP
- Error Handling: 
  * Detailed error reporting
  * Option to view conversion errors

## Advanced Features
- Recursive directory scanning
- Preserves original file names
- Supports nested folder structures
- Web-based conversion interface with drag-and-drop
- Real-time conversion progress tracking
- Batch file selection and conversion
- Individual or bulk file downloading

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

Last Updated: December 16, 2024