import os
import re
import shutil
import random

def modify_script(content):
    """
    Modify the script content to create a Type 2 clone.
    - Renames variables
    - Changes comments
    
    Parameters:
    - content: str, the original script content
    
    Returns:
    - str, the modified script content
    """
    # Replace variable names
    content = re.sub(r'\bvar\b', 'variable', content)
    
    # Change comments
    content = re.sub(r'//.*', lambda match: f'// Comment modified: {match.group(0)}', content)
    
    # Change some formatting
    content = re.sub(r'\s+', ' ', content)
    
    return content

def create_type_2_clones(source_dir, dest_dir, num_clones):
    """
    Create Type 2 clones of all Java scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original Java scripts
    - dest_dir: str, the directory where the clones will be saved
    - num_clones: int, the number of times each script should be cloned
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # List all Java scripts in the source directory
    scripts = [f for f in os.listdir(source_dir) if f.endswith('.java')]
    
    # Clone each script the specified number of times
    for script in scripts:
        script_path = os.path.join(source_dir, script)
        with open(script_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        for i in range(num_clones):
            clone_content = modify_script(content)
            clone_name = f"{os.path.splitext(script)[0]}_clone_{i + 1}.java"
            clone_path = os.path.join(dest_dir, clone_name)
            with open(clone_path, 'w', encoding='utf-8') as file:
                file.write(clone_content)
            print(f"Created {clone_path}")
    
    print(f"Successfully created {num_clones} Type 2 clones for each of {len(scripts)} scripts.")

# Example usage
source_directory = 'java_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type02SampleJava'  # Update this path to your destination directory
number_of_clones = 1  # Set the number of clones you want for each script

create_type_2_clones(source_directory, destination_directory, number_of_clones)
