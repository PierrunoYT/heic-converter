import os
import sys
import pillow_heif
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

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
        # Recursively find HEIC files in the directory
        heic_files = []
        for root, _, files in os.walk(input_path):
            heic_files.extend([
                os.path.join(root, f) for f in files 
                if f.lower().endswith('.heic')
            ])
    else:
        # Single file input
        heic_files = [input_path]
    
    # Create output directory if not specified
    if output_dir is None:
        output_dir = os.path.join(
            os.path.dirname(input_path) if not os.path.isdir(input_path) else input_path, 
            'converted'
        )
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert files
    converted_files = []
    errors = []
    
    for full_input_path in heic_files:
        try:
            # Open HEIC image
            with Image.open(full_input_path) as img:
                # Generate output filename
                base_name = os.path.splitext(os.path.basename(full_input_path))[0]
                output_filename = f"{base_name}.{output_format}"
                output_path = os.path.join(output_dir, output_filename)
                
                # Save converted image
                img.save(output_path)
                converted_files.append(output_path)
                print(f"Converted: {full_input_path} -> {output_path}")
        
        except Exception as e:
            error_msg = f"Error converting {full_input_path}: {e}"
            errors.append(error_msg)
            print(error_msg)
    
    return converted_files, errors

def interactive_converter():
    """
    Interactive CLI for HEIC conversion with Windows-friendly file selection
    """
    # Create root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Prompt for input selection method
    selection_method = messagebox.askyesno(
        "HEIC Converter", 
        "Do you want to select a folder with HEIC images?\n\n"
        "Yes = Select Folder\nNo = Select Individual HEIC Files"
    )

    # Select input based on user choice
    if selection_method:
        # Folder selection
        input_path = filedialog.askdirectory(title="Select Folder with HEIC Images")
        if not input_path:
            messagebox.showerror("Error", "No folder selected. Exiting.")
            sys.exit(1)
    else:
        # File selection
        input_path = filedialog.askopenfilenames(
            title="Select HEIC File(s)",
            filetypes=[("HEIC Files", "*.heic")]
        )
        if not input_path:
            messagebox.showerror("Error", "No files selected. Exiting.")
            sys.exit(1)
        
        # If multiple files selected, use the directory of the first file
        input_path = input_path[0] if len(input_path) == 1 else os.path.dirname(input_path[0])

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
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        messagebox.showerror("Error", "No output directory selected. Exiting.")
        sys.exit(1)

    try:
        # Perform conversion
        converted_files, errors = convert_heic_to_image(
            input_path, 
            output_format=output_format, 
            output_dir=output_dir
        )
        
        # Prepare result message
        result_msg = f"Conversion Complete:\n"
        result_msg += f"- Converted {len(converted_files)} file(s) to {output_format.upper()}\n"
        
        if errors:
            result_msg += f"- {len(errors)} error(s) occurred\n"
            # Option to view detailed errors
            show_errors = messagebox.askyesno(
                "Conversion Completed", 
                result_msg + "\nDo you want to see error details?"
            )
            
            if show_errors:
                error_details = "\n".join(errors)
                messagebox.showinfo("Conversion Errors", error_details)
        else:
            messagebox.showinfo("Conversion Complete", result_msg)
    
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))

def main():
    interactive_converter()

if __name__ == '__main__':
    main()