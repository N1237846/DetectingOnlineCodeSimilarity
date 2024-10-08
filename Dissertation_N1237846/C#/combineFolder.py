import os
import shutil

def copy_cpp_scripts(src_folder1, src_folder2, dest_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Function to copy .cpp files from a source folder to the destination folder
    def copy_files(src_folder, suffix=''):
        for filename in os.listdir(src_folder):
            if filename.endswith('.cs'):
                src_file_path = os.path.join(src_folder, filename)
                
                # Check if the file already exists in the destination folder
                if os.path.exists(os.path.join(dest_folder, filename)):
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_{suffix}{ext}"
                    dest_file_path = os.path.join(dest_folder, new_filename)
                else:
                    dest_file_path = os.path.join(dest_folder, filename)
                
                # Copy the file to the destination folder
                shutil.copy(src_file_path, dest_file_path)
                print(f'Copied: {src_file_path} to {dest_file_path}')
    
    # Copy .cpp files from the first source folder without suffix
    copy_files(src_folder1)
    # Copy .cpp files from the second source folder with a suffix
    copy_files(src_folder2, suffix='from_src2')

# Example usage
src_folder1 = 'c#_scripts_dataset'
src_folder2 = 'type02SampleC#'
dest_folder = 'Type02CombineC#Dataset'

copy_cpp_scripts(src_folder1, src_folder2, dest_folder)
