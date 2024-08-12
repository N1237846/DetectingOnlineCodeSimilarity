import os
import re
import random

def rename_variables(content, suffix):
    """
    Rename variables in the content by adding a suffix.
    
    Parameters:
    - content: str, the original content of the script
    - suffix: str, the suffix to add to each variable name
    
    Returns:
    - str, the modified content with renamed variables
    """
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

def reorder_functions(content):
    """
    Randomly reorder functions in the content.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the content with reordered functions
    """
    function_pattern = r'(def [a-zA-Z_][a-zA-Z0-9_]*\(.*\):\n(?: {4,}.*\n*)*)'
    functions = re.findall(function_pattern, content)
    random.shuffle(functions)
    non_function_code = re.sub(function_pattern, '', content).strip()
    return '\n\n'.join(functions) + '\n\n' + non_function_code

def replace_control_structures(content):
    """
    Replace certain control structures with equivalent ones.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with replaced control structures
    """
    content = re.sub(r'while (.*):', r'for _ in iter(int, 1):\n    if not (\1): break', content)
    return content

def change_algorithms(content):
    """
    Change simple algorithms to more complex ones or use built-in functions.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with changed algorithms
    """
    # Example: Replace a bubble sort implementation with a built-in sorted function
    bubble_sort_pattern = r"""
    def\s+([a-zA-Z_][a-zA-Z0-9_]*)\(lst\):\n
    \s+for\s+i\s+in\s+range\(len\(lst\)\):\n
    \s+for\s+j\s+in\s+range\(0,\s+len\(lst\)\s+-\s+i\s+-\s+1\):\n
    \s+if\s+lst\[j\]\s+>\s+lst\[j\s+\+\s+1\]:\n
    \s+lst\[j\],\s+lst\[j\s+\+\s+1\]\s+=\s+lst\[j\s+\+\s+1\],\s+lst\[j\]\n
    """
    content = re.sub(bubble_sort_pattern, r'def \1(lst):\n    return sorted(lst)', content, flags=re.VERBOSE)
    return content

def change_data_structures(content):
    """
    Change data structures to achieve the same functionality.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with changed data structures
    """
    # Example: Replace a list with a set
    list_pattern = r'(\[.*?\])'
    content = re.sub(list_pattern, r'set(\1)', content)
    return content

def create_type_4_clones(source_dir, destination_dir, num_clones):
    """
    Create Type 4 clones of all Python scripts from the source directory to the destination directory.
    
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
            modified_content = reorder_functions(modified_content)
            modified_content = replace_control_structures(modified_content)
            modified_content = change_algorithms(modified_content)
            modified_content = change_data_structures(modified_content)
            
            with open(clone_path, 'w', encoding='utf-8') as clone_file:
                clone_file.write(modified_content)
    
    print(f"Successfully created {num_clones} Type 4 clones for each of {len(scripts)} scripts.")

# Example usage
source_directory = 'python_scripts_dataset'  # Update this path
destination_directory = 'type04Sample'  # Update this path
number_of_clones = 1  # Set the number of clones you want for each script

create_type_4_clones(source_directory, destination_directory, number_of_clones)
