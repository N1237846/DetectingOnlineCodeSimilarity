import os
import re
import random
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
    variable_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
    reserved_words = set(['int', 'float', 'double', 'char', 'void', 'if', 'else', 'while', 'for', 'return', 'include', 'using', 'namespace', 'std', 'cin', 'cout'])

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
    comment_pattern = r'(//.*)'
    
    def modify_comment(match):
        comment = match.group(0)
        return comment + ' ' + suffix
    
    return re.sub(comment_pattern, modify_comment, content)

def modify_loops(content):
    """
    Modify loops in the content by changing their structure.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with altered loops
    """
    loop_patterns = [
        (r'for\s*\(([^;]*);([^;]*);([^)]+)\)\s*{', r'while (\2) { \1;'),
        (r'while\s*\(([^)]+)\)\s*{', r'for (; \1;) {')
    ]
    
    for pattern, replacement in loop_patterns:
        content = re.sub(pattern, replacement, content)
    
    return content

def reorder_functions(content):
    """
    Reorder functions in the content.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with reordered functions
    """
    function_pattern = r'(\w+\s+\w+\s*\([^)]*\)\s*{[^}]*})'
    functions = re.findall(function_pattern, content, re.DOTALL)
    
    random.shuffle(functions)
    
    for i, func in enumerate(functions):
        content = content.replace(func, f'{{FUNCTION_{i}}}')
    
    for i, func in enumerate(functions):
        content = content.replace(f'{{FUNCTION_{i}}}', func)
    
    return content

def modify_arithmetic_expressions(content):
    """
    Modify arithmetic expressions in the content by changing operators.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with altered arithmetic expressions
    """
    arithmetic_patterns = [
        (r'\b(\d+)\s*\+\s*(\d+)\b', r'\1 - (-\2)'),
        (r'\b(\d+)\s*-\s*(\d+)\b', r'\1 + (-\2)')
    ]
    
    for pattern, replacement in arithmetic_patterns:
        content = re.sub(pattern, replacement, content)
    
    return content

def change_control_flow(content):
    """
    Change control flow statements such as if-else and switch-case.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with altered control flow statements
    """
    if_else_pattern = r'if\s*\(([^)]+)\)\s*{([^}]*)}\s*else\s*{([^}]*)}'
    switch_case_pattern = r'switch\s*\(([^)]+)\)\s*{([^}]*)}'
    
    def modify_if_else(match):
        condition, if_block, else_block = match.groups()
        return f'if (!({condition})) {{ {else_block} }} else {{ {if_block} }}'
    
    content = re.sub(if_else_pattern, modify_if_else, content, flags=re.DOTALL)
    
    return content

def create_type_4_clones(source_dir, destination_dir, num_clones):
    """
    Create Type 4 clones of all C++ scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original C++ scripts
    - destination_dir: str, the directory where the clones will be saved
    - num_clones: int, the number of times each script should be cloned
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # List all C++ scripts in the source directory
    scripts = [f for f in os.listdir(source_dir) if f.endswith('.cpp')]
    
    # Clone each script the specified number of times with transformations
    for script in scripts:
        script_path = os.path.join(source_dir, script)
        with open(script_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        for i in range(num_clones):
            clone_name = f"{os.path.splitext(script)[0]}_clone_{i + 1}.cpp"
            clone_path = os.path.join(destination_dir, clone_name)
            
            # Apply transformations
            modified_content = rename_variables(content, f'_{i + 1}')
            modified_content = modify_comments(modified_content, f'Clone {i + 1}')
            modified_content = modify_loops(modified_content)
            modified_content = reorder_functions(modified_content)
            modified_content = modify_arithmetic_expressions(modified_content)
            modified_content = change_control_flow(modified_content)
            
            with open(clone_path, 'w', encoding='utf-8') as clone_file:
                clone_file.write(modified_content)
    
    print(f"Successfully created {num_clones} Type 4 clones for each of {len(scripts)} scripts.")

# Example usage
source_directory = 'c++_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type04SampleC++'  # Update this path to your destination directory
number_of_clones = 1  # Set the number of clones you want for each script

create_type_4_clones(source_directory, destination_directory, number_of_clones)
