import os
import random
import re

def modify_algorithm(content):
    """
    Modify the algorithm to create Type 4 clones.
    
    Parameters:
    - content: str, the original script content
    
    Returns:
    - str, the modified script content with algorithmic changes
    """
    lines = content.split('\n')
    modified_lines = []
    in_function = False
    function_indent = ""
    
    for line in lines:
        stripped_line = line.strip()
        
        if stripped_line.startswith("for ("):
            in_function = True
            function_indent = re.match(r'\s*', line).group()
            modified_lines.append(line.replace("for (", "while ("))
        elif in_function and stripped_line.endswith(") {"):
            in_function = False
            modified_lines.append(line)
            modified_lines.append(f"{function_indent}int counter = 0;")
            modified_lines.append(f"{function_indent}while (condition) {{")
        elif stripped_line == "}":
            if in_function:
                in_function = False
            modified_lines.append(line)
        else:
            modified_lines.append(line)
            
    modified_content = '\n'.join(modified_lines)
    
    # Add a comment indicating it's a type 4 clone
    modified_content = f"// This is a type 4 clone with algorithmic changes - {random.randint(1000, 9999)}\n" + modified_content
    
    return modified_content

def create_type_4_clones(source_dir, dest_dir):
    """
    Create Type 4 clones of all C# scripts from the source directory to the destination directory.
    
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
                
                # Modify algorithm to create a Type 4 clone
                clone_content = modify_algorithm(content)
                
                # Write the clone content to a new file in the destination directory
                clone_name = f"{os.path.splitext(file)[0]}_type4_clone.cs"
                dest_path = os.path.join(dest_dir, clone_name)
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(clone_content)
                
                print(f"Created Type 4 clone: {dest_path}")

    print(f"Successfully created Type 4 clones for all C# scripts in {dest_dir}")

# Example usage
source_directory = 'c#_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type04SampleC#'  # Update this path to your destination directory

create_type_4_clones(source_directory, destination_directory)
