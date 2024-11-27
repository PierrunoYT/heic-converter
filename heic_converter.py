import os
import argparse
import pillow_heif
from PIL import Image

def convert_heic_to_image(input_path, output_format='png', output_dir=None):
    """
    Convert HEIC image(s) to specified image format.
    
    :param input_path: Path to HEIC file or directory
    :param output_format: Desired output format (default: png)
    :param output_dir: Directory to save converted images (optional)
    """
    # Initialize pillow-heif
    pillow_heif.register_heif_opener()
    
    # Determine input files
    if os.path.isdir(input_path):
        heic_files = [f for f in os.listdir(input_path) if f.lower().endswith('.heic')]
    else:
        heic_files = [os.path.basename(input_path)]
        input_path = os.path.dirname(input_path) or '.'
    
    # Create output directory if not specified
    if output_dir is None:
        output_dir = os.path.join(input_path, 'converted')
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert files
    converted_files = []
    for heic_file in heic_files:
        try:
            # Full input path
            full_input_path = os.path.join(input_path, heic_file)
            
            # Open HEIC image
            with Image.open(full_input_path) as img:
                # Generate output filename
                base_name = os.path.splitext(heic_file)[0]
                output_filename = f"{base_name}.{output_format}"
                output_path = os.path.join(output_dir, output_filename)
                
                # Save converted image
                img.save(output_path)
                converted_files.append(output_path)
                print(f"Converted: {heic_file} -> {output_filename}")
        
        except Exception as e:
            print(f"Error converting {heic_file}: {e}")
    
    return converted_files

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert HEIC images to other formats')
    parser.add_argument('input', help='Input HEIC file or directory')
    parser.add_argument('-f', '--format', default='png', 
                        choices=['png', 'jpg', 'jpeg', 'bmp', 'tiff'], 
                        help='Output image format (default: png)')
    parser.add_argument('-o', '--output', 
                        help='Output directory for converted images')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Perform conversion
    converted = convert_heic_to_image(
        args.input, 
        output_format=args.format, 
        output_dir=args.output
    )
    
    # Print summary
    print(f"\nConversion complete. {len(converted)} file(s) converted.")

if __name__ == '__main__':
    main()