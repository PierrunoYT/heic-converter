from flask import Flask, request, send_file, jsonify, send_from_directory
from flask_cors import CORS
import os
from heic_converter import convert_heic_to_image
import tempfile
import shutil

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

# Create a temporary directory for storing uploads and converted files
UPLOAD_FOLDER = tempfile.mkdtemp()
CONVERTED_FOLDER = os.path.join(UPLOAD_FOLDER, 'converted')
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    output_format = request.form.get('format', 'jpg')
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.lower().endswith('.heic'):
        return jsonify({'error': 'Invalid file format. Only HEIC files are supported'}), 400
    
    try:
        # Save the uploaded file
        temp_input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(temp_input_path)
        
        # Convert the file
        converted_files, errors = convert_heic_to_image(
            temp_input_path,
            output_format=output_format,
            output_dir=CONVERTED_FOLDER
        )
        
        if errors:
            return jsonify({'error': errors[0]}), 500
        
        if not converted_files:
            return jsonify({'error': 'Conversion failed'}), 500
        
        # Get the converted file path
        converted_file_path = converted_files[0]
        
        # Send the converted file
        return send_file(
            converted_file_path,
            as_attachment=True,
            download_name=os.path.basename(converted_file_path)
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)