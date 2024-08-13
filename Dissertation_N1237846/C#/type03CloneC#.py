import os
import random
import shutil
import re

# Predefined list of meaningful sentences for string literals
meaningful_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Hello, this is a meaningful message.",
    "Important: Check your input data.",
    "Operation completed successfully.",
    "Warning: Low disk space.",
    "Please enter a valid number.",
    "Thank you for using our service.",
    "Goodbye, see you soon!",
    "Error: Something went wrong.",
    "Starting the process now."
]

def insert_logging(cs_code):
    """Inserts a logging statement at the beginning of each method."""
    method_pattern = re.compile(r'(public|private|protected|internal|static)\s+\w+\s+\w+\s*\(.*?\)\s*\{')
    modified_code = []

    lines = cs_code.splitlines()
    for line in lines:
        match = method_pattern.match(line.strip())
        if match:
            method_name = match.group(0)
            modified_code.append(line)
            modified_code.append(f'    Console.WriteLine("Entering method: {method_name}");')
        else:
            modified_code.append(line)
    
    return "\n".join(modified_code)

def is_safe_to_rearrange(line):
    """Determine if a line is safe to rearrange."""
    line = line.strip()
    # Avoid rearranging control structures and critical keywords
    return not (line.startswith("if") or
                line.startswith("else") or
                line.startswith("for") or
                line.startswith("while") or
                line.startswith("switch") or
                line.startswith("case") or
                line.startswith("return") or
                line.startswith("{") or
                line.startswith("}") or
                line.startswith("public") or
                line.startswith("private") or
                line.startswith("protected") or
                line.startswith("internal") or
                line.startswith("static") or
                line.startswith("using") or
                line.startswith("break") or
                line.startswith("continue") or
                line.startswith("Console"))

def rearrange_code_blocks(cs_code):
    """Ensure that code blocks are correctly structured and safely rearrange code inside method bodies."""
    lines = cs_code.splitlines()
    modified_code = []
    method_body = []
    in_method = False
    in_control_structure = False
    block_indent = 0

    for line in lines:
        stripped_line = line.strip()

        # Detect method or constructor start
        if stripped_line.endswith("{") and not in_method:
            in_method = True
            block_indent = len(line) - len(line.lstrip())  # Capture indentation level
            modified_code.append(line)  # Add the method signature with the opening brace
            continue

        # Detect method or constructor end
        if stripped_line == "}" and in_method:
            in_method = False
            # Rearrange safe statements within the method or constructor body
            safe_statements = [l for l in method_body if is_safe_to_rearrange(l)]
            other_statements = [l for l in method_body if not is_safe_to_rearrange(l)]
            random.shuffle(safe_statements)
            modified_code.extend(other_statements + safe_statements)  # Maintain other statements at the top
            modified_code.append(line)  # Add the closing brace
            method_body = []
            continue

        # Detect control structures like switch, while, for, if, etc.
        if stripped_line.startswith(("if", "else", "for", "while", "switch", "case", "return", "break", "continue")):
            in_control_structure = True
            modified_code.append(line)
            continue

        # Exit control structure when it ends
        if in_control_structure and stripped_line == "}":
            in_control_structure = False
            modified_code.append(line)
            continue

        # Collect lines within a method body or control structure body
        if in_method:
            if in_control_structure:
                modified_code.append(line)
            else:
                method_body.append(line)
        else:
            modified_code.append(line)

    return "\n".join(modified_code)

def modify_loops(cs_code):
    """Transforms loops by changing their structure."""
    loop_pattern = re.compile(r'for\s*\((int|long|double|float|char)\s+(\w+)\s*=\s*(\d+);\s*\2\s*<\s*(\d+);\s*\2\s*\+\+\)')
    
    def loop_replacement(match):
        loop_type = match.group(1)
        var_name = match.group(2)
        start_value = match.group(3)
        end_value = match.group(4)
        return f'{loop_type} {var_name} = {start_value}; while({var_name} < {end_value})'

    return re.sub(loop_pattern, loop_replacement, cs_code)

def invert_conditionals(cs_code):
    """Invert conditional statements to create structural differences."""
    conditional_pattern = re.compile(r'if\s*\((.*?)\)\s*\{')
    
    def conditional_replacement(match):
        condition = match.group(1)
        return f'if (!({condition})) {{'

    return re.sub(conditional_pattern, conditional_replacement, cs_code)

def rename_variables(cs_code):
    """Randomly rename variables in the code."""
    var_pattern = re.compile(r'\b(int|long|double|float|char|string|bool)\s+(\w+)\b')

    variables = {}
    modified_code = []
    lines = cs_code.splitlines()

    for line in lines:
        match = var_pattern.findall(line)
        for var_type, var_name in match:
            if var_name not in variables:
                new_name = "var_" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
                variables[var_name] = new_name
            line = re.sub(r'\b' + var_name + r'\b', variables[var_name], line)
        modified_code.append(line)

    return "\n".join(modified_code)

def modify_string_literals(cs_code):
    """Modify string literals in the code to meaningful words or sentences."""
    string_pattern = re.compile(r'\"(.*?)\"')
    
    def string_replacement(match):
        return f'"{random.choice(meaningful_sentences)}"'
    
    return re.sub(string_pattern, string_replacement, cs_code)

def add_redundant_code(cs_code):
    """Add redundant code that does not affect the logic."""
    modified_code = []
    lines = cs_code.splitlines()

    for line in lines:
        modified_code.append(line)
        if line.strip().endswith(";") and not line.strip().startswith("//"):
            modified_code.append("    // No-op")
    
    return "\n".join(modified_code)

def apply_modifications(cs_code):
    """Apply all modifications to the C# code."""
    cs_code = insert_logging(cs_code)
    cs_code = rearrange_code_blocks(cs_code)
    cs_code = modify_loops(cs_code)
    cs_code = invert_conditionals(cs_code)
    cs_code = rename_variables(cs_code)
    cs_code = modify_string_literals(cs_code)
    cs_code = add_redundant_code(cs_code)
    return cs_code

def process_file(file_path, clone_folder):
    """Processes a single C# file to generate its Type III clone."""
    with open(file_path, 'r', encoding='utf-8') as source_file:
        original_code = source_file.read()

    # Apply modifications to the C# code
    modified_code = apply_modifications(original_code)

    # Prepare the clone file path
    relative_path = os.path.relpath(file_path, os.path.dirname(file_path))
    clone_file_path = os.path.join(clone_folder, relative_path)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(clone_file_path), exist_ok=True)

    # Write the modified code to the new clone file
    with open(clone_file_path, 'w', encoding='utf-8') as clone_file:
        clone_file.write(modified_code)

def clone_folder(original_folder, clone_folder):
    """Transforms all C# files in the original folder into Type III clones and saves them in the clone folder."""
    if not os.path.exists(clone_folder):
        os.makedirs(clone_folder)

    for root, _, files in os.walk(original_folder):
        for file_name in files:
            if file_name.endswith('.cs'):
                file_path = os.path.join(root, file_name)
                process_file(file_path, clone_folder)
            else:
                # Copy non-C# files directly
                src_file_path = os.path.join(root, file_name)
                dst_file_path = os.path.join(clone_folder, os.path.relpath(src_file_path, original_folder))
                os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
                shutil.copy2(src_file_path, dst_file_path)

if __name__ == "__main__":
    original_folder = "c#_scripts_dataset"
    clone_folder_name = "type03SampleC#"
    clone_folder(original_folder, clone_folder_name)
    print(f"Type III clones have been generated and saved to '{clone_folder_name}'.")
