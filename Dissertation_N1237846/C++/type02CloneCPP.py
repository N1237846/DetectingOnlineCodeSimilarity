import os
import shutil
import random
import re

# A preset list of meaningful comments to replace existing comments
meaningful_comments = [
    "// This is a crucial part of the algorithm",
    "// Optimization needed here",
    "// Temporary workaround",
    "// Review this section carefully",
    "// Consider edge cases",
    "// This function could be optimized further",
    "// Ensure this works with the latest API changes",
    "// Refactor if necessary",
    "// Legacy code, consider updating",
    "// Potential performance bottleneck"
]

# List of C++ standard functions, methods, classes, and keywords to preserve
CPP_STANDARD_NAMES = set([
    "cout", "cin", "cerr", "clog", "string", "vector", "map", "set", "deque", "list",
    "unordered_map", "unordered_set", "pair", "tuple", "algorithm", "numeric", "iostream",
    "fstream", "sstream", "iomanip", "thread", "mutex", "condition_variable", "future", "shared_ptr",
    "unique_ptr", "weak_ptr", "exception", "static_cast", "dynamic_cast", "reinterpret_cast", "const_cast",
    "bool", "char", "int", "long", "float", "double", "void", "size_t", "nullptr", "true", "false",
    "if", "else", "for", "while", "do", "switch", "case", "default", "break", "continue", "return", "try", "catch", "throw",
    "public", "private", "protected", "class", "struct", "namespace", "template", "typename", "friend", "virtual", "override", "final",
    "operator", "new", "delete", "sizeof", "alignof", "decltype", "static", "extern", "inline", "const", "volatile", "mutable", "static_assert",
    "enum", "typedef", "using", "static_assert", "dynamic_cast", "explicit", "noexcept",
    "main"  # Preserve the main function
])

def generate_random_name(name):
    """Generate a new name for variables by adding a prefix."""
    return f"cloned_{name}"

def preserve_output_statements(code):
    """Preserve content inside cout, cerr, etc., and temporarily replace them with placeholders."""
    output_placeholder = "PLACEHOLDER_FOR_OUTPUT"
    placeholders = []
    
    def replacer(match):
        placeholders.append(match.group(0))
        return output_placeholder

    code = re.sub(r'(\bcout\s*<<\s*".*?"|cerr\s*<<\s*".*?")', replacer, code)
    
    return code, placeholders

def restore_output_statements(code, placeholders):
    """Restore the original content in output statements from placeholders."""
    for placeholder in placeholders:
        code = code.replace("PLACEHOLDER_FOR_OUTPUT", placeholder, 1)
    
    return code

def replace_comments(code):
    """Replace comments with meaningful comments."""
    def comment_replacer(match):
        action = random.choice(["delete", "replace", "keep"])
        if action == "replace":
            return random.choice(meaningful_comments)
        elif action == "delete":
            return ""
        else:
            return match.group(0)  # Keep the comment unchanged

    return re.sub(r'//.*', comment_replacer, code)

def preserve_standard_names(code):
    """Identify and preserve C++ standard names."""
    preserved_names = set(CPP_STANDARD_NAMES)

    # Extract and preserve function names, class names, and other critical identifiers
    identifiers = re.findall(r'\b[a-zA-Z_]\w*\b', code)
    for identifier in identifiers:
        if identifier in CPP_STANDARD_NAMES:
            preserved_names.add(identifier)

    return preserved_names

def replace_variable_names(code, preserved_names):
    """Replace variable names with new names, while preserving specific names."""
    # Extract variable names using regex
    variable_pattern = re.compile(r'\b[a-zA-Z_]\w*\b')
    variable_names = set(variable_pattern.findall(code))

    # Replace variable names with new names
    for name in variable_names:
        if name not in preserved_names and name != 'main':
            new_name = generate_random_name(name)
            code = re.sub(r'\b{}\b'.format(re.escape(name)), new_name, code)

    return code

def modify_code(code):
    """Modify code by changing comments and variable names."""
    code, output_placeholders = preserve_output_statements(code)
    preserved_names = preserve_standard_names(code)
    code_with_modified_comments = replace_comments(code)
    modified_code = replace_variable_names(code_with_modified_comments, preserved_names)
    modified_code = restore_output_statements(modified_code, output_placeholders)
    return modified_code

def clone_cpp_file(src_file_path, dst_file_path):
    with open(src_file_path, 'r', encoding='utf-8') as src_file:
        original_code = src_file.read()

    # Modify the code
    modified_code = modify_code(original_code)

    # Write the modified code to the destination file
    with open(dst_file_path, 'w', encoding='utf-8') as dst_file:
        dst_file.write(modified_code)

def clone_folder(src_folder, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for root, dirs, files in os.walk(src_folder):
        relative_path = os.path.relpath(root, src_folder)
        clone_root = os.path.join(dst_folder, relative_path)

        for dir_name in dirs:
            os.makedirs(os.path.join(clone_root, dir_name), exist_ok=True)

        for file_name in files:
            src_file_path = os.path.join(root, file_name)
            dst_file_path = os.path.join(clone_root, file_name)

            if file_name.endswith('.cpp') or file_name.endswith('.h'):
                clone_cpp_file(src_file_path, dst_file_path)
            else:
                shutil.copy2(src_file_path, dst_file_path)

if __name__ == "__main__":
    src_folder = "c++_scripts_dataset"
    dst_folder = "type02SampleCPP"

    clone_folder(src_folder, dst_folder)

    print(f"Cloning completed. All files and folders from '{src_folder}' have been cloned to '{dst_folder}'.")
