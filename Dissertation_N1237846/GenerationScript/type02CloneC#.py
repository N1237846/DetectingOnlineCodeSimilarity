import os
import re
import shutil
import random

def rename_identifiers(content):
    """
    Rename variables, methods, and classes to create Type 2 clones.
    
    Parameters:
    - content: str, the original script content
    
    Returns:
    - str, the modified script content with renamed identifiers
    """
    # Example pattern replacements to rename identifiers
    patterns = {
        r'\bint\b': 'int32',  # Example type change
        r'\bstring\b': 'str',  # Example type change
        r'\bbool\b': 'boolean',  # Example type change
    }

    # Replace identifiers in the content
    for old, new in patterns.items():
        content = re.sub(old, new, content)

    # Randomly rename variables and methods
    content = re.sub(r'\bvar\b', lambda x: 'var_' + str(random.randint(100, 999)), content)
    content = re.sub(r'\bfunc\b', lambda x: 'func_' + str(random.randint(100, 999)), content)

    return content

def create_type_2_clones(source_dir, dest_dir):
    """
    Create Type 2 clones of all C# scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original C# scripts (including subdirectories)
    - dest_dir: str, the directory where the cloned scripts will be saved
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # Walk through the source directory and find all .cs files
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.cs'):
                src_path = os.path.join(root, file)
                with open(src_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Rename identifiers to create a Type 2 clone
                clone_content = rename_identifiers(content)
                
                # Write the clone content to a new file in the destination directory
                clone_name = f"{os.path.splitext(file)[0]}_type2_clone.cs"
                dest_path = os.path.join(dest_dir, clone_name)
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(clone_content)
                
                print(f"Created Type 2 clone: {dest_path}")

    print(f"Successfully created Type 2 clones for all C# scripts in {dest_dir}")

# Example usage
source_directory = 'c#_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type02SampleC#'  # Update this path to your destination directory

create_type_2_clones(source_directory, destination_directory)
