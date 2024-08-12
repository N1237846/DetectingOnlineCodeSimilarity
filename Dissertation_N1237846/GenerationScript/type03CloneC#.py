import os
import shutil
import random

def modify_layout(content):
    """
    Modify the layout of the code to create Type 3 clones.
    
    Parameters:
    - content: str, the original script content
    
    Returns:
    - str, the modified script content with changed layout and added comments
    """
    lines = content.split('\n')
    
    # Add a random comment at the start of the file
    lines.insert(0, f"// This is a type 3 clone with modified layout - {random.randint(1000, 9999)}")
    
    # Add random blank lines and comments throughout the file
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if random.random() < 0.1:  # 10% chance to add a blank line
            new_lines.append('')
        if random.random() < 0.1:  # 10% chance to add a comment
            new_lines.append(f"// Random comment {random.randint(1000, 9999)}")

    return '\n'.join(new_lines)

def create_type_3_clones(source_dir, dest_dir):
    """
    Create Type 3 clones of all C# scripts from the source directory to the destination directory.
    
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
                
                # Modify layout to create a Type 3 clone
                clone_content = modify_layout(content)
                
                # Write the clone content to a new file in the destination directory
                clone_name = f"{os.path.splitext(file)[0]}_type3_clone.cs"
                dest_path = os.path.join(dest_dir, clone_name)
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(clone_content)
                
                print(f"Created Type 3 clone: {dest_path}")

    print(f"Successfully created Type 3 clones for all C# scripts in {dest_dir}")

# Example usage
source_directory = 'c#_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type03SampleC#'  # Update this path to your destination directory

create_type_3_clones(source_directory, destination_directory)
