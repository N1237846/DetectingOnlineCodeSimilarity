import os
import shutil
from git import Repo

def clone_repo(repo_url, clone_dir):
    """
    Clone a GitHub repository to the specified directory.
    
    Parameters:
    - repo_url: str, the URL of the GitHub repository
    - clone_dir: str, the local directory to clone the repository into
    """
    if not os.path.exists(clone_dir):
        os.makedirs(clone_dir)
    Repo.clone_from(repo_url, clone_dir)

def collect_python_scripts(source_dir, dataset_dir):
    """
    Collect all Python scripts from the source directory and copy them to the dataset directory.
    
    Parameters:
    - source_dir: str, the directory containing the cloned GitHub repository
    - dataset_dir: str, the directory where the Python scripts will be copied
    """
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                shutil.copy2(file_path, dataset_dir)
                print(f"Copied: {file_path}")

def main():
    repo_url = 'https://github.com/jackfrued/Python-100-Days.git'
    clone_dir = 'cloned_repo'
    dataset_dir = 'python_scripts_dataset'

    # Step 1: Clone the repository
    print("Cloning the repository...")
    clone_repo(repo_url, clone_dir)
    print("Repository cloned.")

    # Step 2: Collect Python scripts
    print("Collecting Python scripts...")
    collect_python_scripts(clone_dir, dataset_dir)
    print("Python scripts collected.")

if __name__ == '__main__':
    main()
