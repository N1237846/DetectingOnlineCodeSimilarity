import os
import shutil

def create_cpp_clones(source_folder, target_folder, clone_prefix="Clone_"):
    """
    Create Type I clones of C++ files from the source folder and place them in the target folder.
    
    :param source_folder: Path to the source folder containing C++ files.
    :param target_folder: Path to the target folder where clones will be saved.
    :param clone_prefix: Prefix to add to cloned file names to differentiate them.
    """
    # Ensure the target directory exists
    os.makedirs(target_folder, exist_ok=True)
    
    # List all C++ files in the source folder (.cpp and .h)
    cpp_files = [f for f in os.listdir(source_folder) if f.endswith('.cpp') or f.endswith('.h')]
    
    if not cpp_files:
        print(f"No C++ files found in the source folder: {source_folder}")
        return
    
    for file_name in cpp_files:
        source_file_path = os.path.join(source_folder, file_name)
        clone_file_name = f"{clone_prefix}{file_name}"
        target_file_path = os.path.join(target_folder, clone_file_name)
        
        # Copy the file from source to target folder
        shutil.copy2(source_file_path, target_file_path)
        print(f"Created clone: {target_file_path}")

    print(f"Cloning complete. Clones are stored in: {target_folder}")

# Usage example
source_folder = 'C++_scripts_dataset'
target_folder = 'type01SampleCPP'

create_cpp_clones(source_folder, target_folder)
