import os
import shutil

def copy_python_scripts(src_folder1, src_folder2, dest_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Function to copy .py files from a source folder to the destination folder
    def copy_files(src_folder):
        for filename in os.listdir(src_folder):
            if filename.endswith('.py'):
                src_file_path = os.path.join(src_folder, filename)
                dest_file_path = os.path.join(dest_folder, filename)
                
                # Copy the file to the destination folder
                shutil.copy(src_file_path, dest_file_path)
                print(f'Copied: {src_file_path} to {dest_file_path}')
    
    # Copy .py files from both source folders
    copy_files(src_folder1)
    copy_files(src_folder2)

# Example usage
src_folder1 = 'python_scripts_dataset'
src_folder2 = 'type01SamplePython'
dest_folder = 'PythonDataset'

copy_python_scripts(src_folder1, src_folder2, dest_folder)
