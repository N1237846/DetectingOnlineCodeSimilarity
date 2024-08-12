import os
import re
import random
import string

def generate_meaningful_name(prefix, index):
    """
    Generate a new, meaningful variable name based on a prefix and index.
    
    Parameters:
    - prefix: str, the base prefix for the variable name
    - index: int, the index used to ensure uniqueness
    
    Returns:
    - str, the new variable name
    """
    prefixes = ['data', 'value', 'item', 'result', 'temp', 'counter', 'index', 'value', 'number', 'flag']
    return f'{random.choice(prefixes)}_{index}'

def rename_user_defined_functions_and_references(content, suffix):
    """
    Rename user-defined functions and their references by appending the length of the function name as a suffix.
    
    Parameters:
    - content: str, the original content of the script
    - suffix: str, the suffix to add to each user-defined function name
    
    Returns:
    - str, the modified content with renamed functions and updated references
    """
    function_pattern = r'\bdef\s+([a-zA-Z_][a-zA-Z0-9_]*)\b'
    reserved_words = set([
        'async', 'await', 'print', 'threading', 'asyncio', 'get_event_loop', 'wait', 'sleep'
    ])
    function_names = {}

    def rename_function(match):
        function_name = match.group(1)
        if function_name not in reserved_words:
            new_name = f'{function_name}_{len(function_name)}{suffix}'
            function_names[function_name] = new_name
            return f'def {new_name}'
        return match.group(0)

    # Rename functions and store their new names
    content = re.sub(function_pattern, rename_function, content)
    
    # Update function references
    for old_name, new_name in function_names.items():
        content = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, content)
    
    return content

def replace_variable_names(content):
    """
    Replace variable names with new, meaningful names, excluding library functions and method names.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with replaced variable names
    """
    variable_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
    reserved_words = set([
        'def', 'class', 'if', 'else', 'elif', 'for', 'while', 'return', 'import', 'from', 
        'as', 'with', 'pass', 'break', 'continue', 'try', 'except', 'finally', 'raise', 
        'yield', 'assert', 'lambda', 'True', 'False', 'None', 'and', 'or', 'not', 'is', 'in',
        'async', 'await', 'print', 'threading', 'asyncio', 'get_event_loop', 'wait', 'sleep'
    ])
    variable_names = {}
    index = 1

    def replace(match):
        nonlocal index
        word = match.group(0)
        if word not in reserved_words and not word.startswith('__'):
            if word not in variable_names:
                new_name = generate_meaningful_name(word, index)
                variable_names[word] = new_name
                index += 1
            return variable_names[word]
        return word

    return re.sub(variable_pattern, replace, content)

def replace_or_delete_comments(content):
    """
    Replace comments with new, meaningful comments or delete them entirely based on random choice.
    
    Parameters:
    - content: str, the original content of the script
    
    Returns:
    - str, the modified content with either replaced or deleted comments
    """
    comment_pattern = r'(#.*)'

    def replace_or_delete_comment(match):
        # Randomly decide whether to replace or delete the comment
        if random.choice([True, False]):  # 50% chance to replace or delete
            comment = match.group(0)
            new_comment = random.choice([
                "# Initialize the variable",
                "# Perform some calculation",
                "# Handle the exception",
                "# Define a new function",
                "# Set up the environment",
                "# Execute the logic",
                "# Wait for the operation to complete",
                "# Log the information",
                "# Close the resources",
                "# Check for errors",
                "# Prepare the output",
                "# Process the input data",
                "# Update the status",
                "# Manage the state",
                "# Run the main loop"
            ])
            return f'# {new_comment}'
        else:
            return ''  # Delete the comment

    return re.sub(comment_pattern, replace_or_delete_comment, content)

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
            modified_content = rename_user_defined_functions_and_references(content, f'_{i + 1}')
            modified_content = replace_variable_names(modified_content)
            modified_content = replace_or_delete_comments(modified_content)
            
            with open(clone_path, 'w', encoding='utf-8') as clone_file:
                clone_file.write(modified_content)
    
    print(f"Successfully created {num_clones} Type 2 clones for each of {len(scripts)} scripts.")

# Example usage
source_directory = 'python_scripts_dataset'  # Update this path
destination_directory = 'type02SamplePython'  # Update this path
number_of_clones = 1  # Set the number of clones you want for each script

create_type_2_clones(source_directory, destination_directory, number_of_clones)
