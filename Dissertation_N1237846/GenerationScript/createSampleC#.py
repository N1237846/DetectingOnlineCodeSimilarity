import os
import shutil
import subprocess

def clone_repo(repo_url, clone_dir):
    """
    Clone the GitHub repository to a local directory.
    
    Parameters:
    - repo_url: str, the URL of the GitHub repository
    - clone_dir: str, the local directory to clone the repository into
    """
    if os.path.exists(clone_dir):
        print(f"Directory {clone_dir} already exists. Deleting it.")
        shutil.rmtree(clone_dir)
    subprocess.run(['git', 'clone', repo_url, clone_dir], check=True)
    print(f"Repository cloned to {clone_dir}")

def find_and_copy_csharp_files(source_dir, dest_dir):
    """
    Find all C# files in the source directory and copy them to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original C# scripts
    - dest_dir: str, the directory where the C# scripts will be copied
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # Walk through the source directory and find all .cs files
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.cs'):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, source_dir)
                dest_path = os.path.join(dest_dir, rel_path)
                
                # Ensure the destination subdirectories exist
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                # Copy the file
                shutil.copy2(src_path, dest_path)
                print(f"Copied {src_path} to {dest_path}")

    print(f"Successfully copied all C# files to {dest_dir}")

# Example usage
repo_url = 'https://github.com/Kalutu/csharp-for-everybody.git'  # GitHub repository URL
clone_directory = 'cloned_repo_c#'  # Update this path to your local clone directory
destination_directory = 'c#_scripts_dataset'  # Update this path to your destination directory

# Clone the repository
clone_repo(repo_url, clone_directory)

# Find and copy all C# files
find_and_copy_csharp_files(clone_directory, destination_directory)
