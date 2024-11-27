import os
import sys
import pillow_heif
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_heic_to_image(input_path, output_format='png', output_dir=None):
    """
    Convert HEIC image(s) to specified image format.
    
    :param input_path: Path to HEIC file or directory
    :param output_format: Desired output format (default: png)
    :param output_dir: Directory to save converted images (optional)
    """
    # Initialize pillow-heif
    pillow_heif.register_heif_opener()
    
    # Validate input path
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The path {input_path} does not exist.")
    
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

def interactive_converter():
    """
    Interactive CLI for HEIC conversion with Windows-friendly file selection
    """
    # Create root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Prompt for input file/directory
    messagebox.showinfo("HEIC Converter", "Please select HEIC file(s) or directory")
    input_path = filedialog.askopenfilename(
        title="Select HEIC File(s)",
        filetypes=[("HEIC Files", "*.heic")],
        multiple=False
    ) or filedialog.askdirectory(title="Select HEIC Directory")

    if not input_path:
        print("No file or directory selected. Exiting.")
        sys.exit(1)

    # Supported output formats
    formats = ['png', 'jpg', 'jpeg', 'bmp', 'tiff']
    
    # Prompt for output format
    format_window = tk.Tk()
    format_window.title("Select Output Format")
    format_window.geometry("300x200")

    selected_format = tk.StringVar(value='png')
    
    tk.Label(format_window, text="Choose Output Format:").pack(pady=10)
    
    for fmt in formats:
        tk.Radiobutton(
            format_window, 
            text=fmt.upper(), 
            variable=selected_format, 
            value=fmt
        ).pack(anchor=tk.W, padx=50)
    
    def on_submit():
        format_window.quit()
        format_window.destroy()
    
    tk.Button(format_window, text="Convert", command=on_submit).pack(pady=10)
    
    format_window.mainloop()
    
    output_format = selected_format.get()

    # Prompt for output directory
    messagebox.showinfo("HEIC Converter", "Select output directory for converted images")
    output_dir = filedialog.askdirectory(title="Select Output Directory")

    try:
        # Perform conversion
        converted_files = convert_heic_to_image(
            input_path, 
            output_format=output_format, 
            output_dir=output_dir
        )
        
        # Show completion message
        messagebox.showinfo(
            "Conversion Complete", 
            f"Converted {len(converted_files)} file(s) to {output_format.upper()}"
        )
    
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))

def main():
    interactive_converter()

if __name__ == '__main__':
    main()