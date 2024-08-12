import os
import shutil
import subprocess

def clone_repo(repo_url, clone_dir):
    """
    Clone a GitHub repository to a specified directory.
    
    Parameters:
    - repo_url: str, the URL of the GitHub repository
    - clone_dir: str, the directory where the repository should be cloned
    """
    subprocess.run(['git', 'clone', repo_url, clone_dir], check=True)

def copy_cpp_files(source_dir, destination_dir):
    """
    Copy all C++ files from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the cloned GitHub repository
    - destination_dir: str, the directory where the C++ files should be copied
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # Traverse the source directory and copy all .cpp files
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.cpp'):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_dir, file)
                shutil.copy2(source_file, destination_file)
    
    print(f"Successfully copied all C++ files to {destination_dir}")

# Example usage
repo_url = 'https://github.com/prakharjadaun/100-CPP-Programs-Practice.git'  # GitHub repository URL
clone_directory = 'cloned_repo_c++'  # Temporary directory to clone the repository
destination_directory = 'c++_scripts_dataset'  # Directory to copy the C++ files

# Clone the repository
clone_repo(repo_url, clone_directory)

# Copy all C++ files to the destination directory
copy_cpp_files(clone_directory, destination_directory)

# Optionally, clean up the cloned repository directory
shutil.rmtree(clone_directory)
