import os
import re
import shutil

def rename_variables(content, suffix):
    """
    Rename variables in the content by adding a suffix.
    
    Parameters:
    - content: str, the original content of the script
    - suffix: str, the suffix to add to each variable name
    
    Returns:
    - str, the modified content with renamed variables
    """
    # Regular expression to find variable names (simple version)
    variable_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
    reserved_words = set(['def', 'class', 'if', 'else', 'elif', 'for', 'while', 'return', 'import', 'from', 'as', 'with', 'pass', 'break', 'continue', 'try', 'except', 'finally', 'raise', 'yield', 'assert', 'lambda', 'True', 'False', 'None', 'and', 'or', 'not', 'is', 'in'])

    def rename(match):
        word = match.group(0)
        if word not in reserved_words:
            return word + suffix
        return word
    
    return re.sub(variable_pattern, rename, content)

def modify_comments(content, suffix):
    """
    Modify comments in the content by adding a suffix.
    
    Parameters:
    - content: str, the original content of the script
    - suffix: str, the suffix to add to each comment
    
    Returns:
    - str, the modified content with updated comments
    """
    comment_pattern = r'(#.*)'
    
    def modify_comment(match):
        comment = match.group(0)
        return comment + ' ' + suffix
    
    return re.sub(comment_pattern, modify_comment, content)

def create_type_2_clones(source_dir, destination_dir, num_clones):
    """
    Create Type 2 clones of all Python scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original Python scripts
    - destination_dir: str, the directory where the clones will be saved
    - num_clones: int, the number of times each script should be cloned
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # List all Python scripts in the source directory
    scripts = [f for f in os.listdir(source_dir) if f.endswith('.py')]
    
    # Clone each script the specified number of times with transformations
    for script in scripts:
        script_path = os.path.join(source_dir, script)
        with open(script_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        for i in range(num_clones):
            clone_name = f"{os.path.splitext(script)[0]}_clone_{i + 1}.py"
            clone_path = os.path.join(destination_dir, clone_name)
            
            # Apply transformations
            modified_content = rename_variables(content, f'_{i + 1}')
            modified_content = modify_comments(modified_content, f'Clone {i + 1}')
            
            with open(clone_path, 'w', encoding='utf-8') as clone_file:
                clone_file.write(modified_content)
    
    print(f"Successfully created {num_clones} Type 2 clones for each of {len(scripts)} scripts.")

# Example usage
source_directory = 'python_scripts_dataset'  # Update this path
destination_directory = 'type02Sample'  # Update this path
number_of_clones = 1  # Set the number of clones you want for each script

create_type_2_clones(source_directory, destination_directory, number_of_clones)
