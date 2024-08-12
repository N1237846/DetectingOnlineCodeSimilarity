import os
import shutil
import subprocess
from git import Repo

def clone_repo(repo_url, clone_dir):
    """
    Clone a GitHub repository to a specified directory.
    
    Parameters:
    - repo_url: str, the URL of the GitHub repository
    - clone_dir: str, the directory where the repository will be cloned
    """
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    Repo.clone_from(repo_url, clone_dir)
    print(f"Cloned repository to {clone_dir}")

def copy_java_files(source_dir, dest_dir):
    """
    Copy all Java files from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the cloned repository
    - dest_dir: str, the directory where the Java files will be saved
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.java'):
                source_file = os.path.join(root, file)
                shutil.copy(source_file, dest_dir)
                print(f"Copied {source_file} to {dest_dir}")

def main():
    repo_url = 'https://github.com/MakarandPundlik/Core-Java.git'  # Update this URL to the repository you want to clone
    clone_directory = 'cloned_repo_java'  # Directory where the repository will be cloned
    destination_directory = 'java_scripts_dataset'  # Directory where the Java files will be saved

    # Clone the repository
    clone_repo(repo_url, clone_directory)
    
    # Copy all Java files to the destination directory
    copy_java_files(clone_directory, destination_directory)

    print(f"All Java files have been copied to {destination_directory}")

if __name__ == '__main__':
    main()
