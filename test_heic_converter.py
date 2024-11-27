import os
import unittest
import tempfile
import shutil
from heic_converter import convert_heic_to_image

class TestHeicConverter(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        
        # Create a mock HEIC file (in a real scenario, you'd use an actual HEIC file)
        self.mock_heic_path = os.path.join(self.test_dir, 'mock.heic')
        with open(self.mock_heic_path, 'wb') as f:
            # Write a minimal file header to simulate a HEIC file
            f.write(b'ftypheic')
    
    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)
    
    def test_convert_single_file(self):
        # Test converting a single file
        output_dir = os.path.join(self.test_dir, 'output')
        converted_files = convert_heic_to_image(
            self.mock_heic_path, 
            output_format='png', 
            output_dir=output_dir
        )
        
        # Check if output directory was created
        self.assertTrue(os.path.exists(output_dir))
        
        # Check if conversion produced a file
        self.assertEqual(len(converted_files), 1)
        self.assertTrue(os.path.exists(converted_files[0]))
        
        # Verify output filename
        expected_output = os.path.join(output_dir, 'mock.png')
        self.assertEqual(converted_files[0], expected_output)
    
    def test_convert_directory(self):
        # Create multiple mock HEIC files
        for i in range(3):
            with open(os.path.join(self.test_dir, f'mock{i}.heic'), 'wb') as f:
                f.write(b'ftypheic')
        
        # Test directory conversion
        output_dir = os.path.join(self.test_dir, 'output')
        converted_files = convert_heic_to_image(
            self.test_dir, 
            output_format='jpg', 
            output_dir=output_dir
        )
        
        # Check if output directory was created
        self.assertTrue(os.path.exists(output_dir))
        
        # Check if all files were converted
        self.assertEqual(len(converted_files), 3)
        
        # Verify output filenames
        for i in range(3):
            expected_output = os.path.join(output_dir, f'mock{i}.jpg')
            self.assertTrue(os.path.exists(expected_output))
    
    def test_unsupported_format(self):
        # Test conversion with unsupported format
        output_dir = os.path.join(self.test_dir, 'output')
        
        # This should not raise an exception
        converted_files = convert_heic_to_image(
            self.mock_heic_path, 
            output_format='png', 
            output_dir=output_dir
        )
        
        # Verify conversion still works
        self.assertEqual(len(converted_files), 1)
    
    def test_nonexistent_input(self):
        # Test handling of nonexistent input
        with self.assertRaises(FileNotFoundError):
            convert_heic_to_image('/path/to/nonexistent/file.heic')

if __name__ == '__main__':
    unittest.main()