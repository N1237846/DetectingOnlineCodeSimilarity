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

# List of Java keywords and standard classes to preserve
JAVA_KEYWORDS_AND_CLASSES = set([
    "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class",
    "const", "continue", "default", "do", "double", "else", "enum", "extends", "final",
    "finally", "float", "for", "goto", "if", "implements", "import", "instanceof", "int",
    "interface", "long", "native", "new", "null", "package", "private", "protected", "public",
    "return", "short", "static", "strictfp", "super", "switch", "synchronized", "this", "throw",
    "throws", "transient", "try", "void", "volatile", "while", "java", "javax", "org",
    "java.awt", "java.io", "java.lang", "java.net", "java.nio", "java.sql", "java.util",
    "javax.swing"
])

def generate_random_name(name):
    """Generate a new name for variables by adding a prefix."""
    return f"cloned_{name}"

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

def preserve_imports(code):
    """Preserve import statements and standard libraries."""
    import_statements = re.findall(r'^\s*import\s+[^\s;]+;', code, re.MULTILINE)
    preserved_code = re.sub(r'^\s*import\s+[^\s;]+;', '/* preserved import */', code, flags=re.MULTILINE)
    return import_statements, preserved_code

def replace_variable_names(code, import_statements):
    """Replace variable names with new names, while preserving imports."""
    # Extract variable names using regex
    variable_pattern = re.compile(r'\b([a-zA-Z_]\w*)\b')
    variable_names = set(variable_pattern.findall(code))

    # Preserve names from imports and standard libraries
    preserved_names = set()
    for imp in import_statements:
        matches = re.findall(r'import\s+([^\s;]+)', imp)
        for match in matches:
            parts = match.split('.')
            preserved_names.add(parts[-1])  # e.g., 'List' from 'java.util.List'

    # Remove Java keywords and classes from the list of variable names to rename
    preserved_names.update(JAVA_KEYWORDS_AND_CLASSES)
    
    for name in variable_names:
        if name not in preserved_names and name not in JAVA_KEYWORDS_AND_CLASSES:
            new_name = generate_random_name(name)
            code = re.sub(r'\b{}\b'.format(re.escape(name)), new_name, code)

    return code

def modify_code(code):
    """Modify code by changing comments and variable names."""
    import_statements, code_without_imports = preserve_imports(code)
    code_with_modified_comments = replace_comments(code_without_imports)
    modified_code = replace_variable_names(code_with_modified_comments, import_statements)

    # Reinsert preserved imports
    modified_code_with_imports = '\n'.join(import_statements) + '\n' + modified_code
    return modified_code_with_imports

def clone_java_file(src_file_path, dst_file_path):
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

            if file_name.endswith('.java'):
                clone_java_file(src_file_path, dst_file_path)
            else:
                shutil.copy2(src_file_path, dst_file_path)

if __name__ == "__main__":
    src_folder = "java_scripts_dataset"
    dst_folder = "type02SampleJava"

    clone_folder(src_folder, dst_folder)

    print(f"Cloning completed. All files and folders from '{src_folder}' have been cloned to '{dst_folder}'.")
