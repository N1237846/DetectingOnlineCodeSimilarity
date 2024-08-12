import os
import shutil
import parso
import builtins
import sys
import pkgutil
import random

# A preset list of meaningful comments to replace existing comments
meaningful_comments = [
    "# This is a crucial part of the algorithm",
    "# Optimization needed here",
    "# Temporary workaround",
    "# Review this section carefully",
    "# Consider edge cases",
    "# This function could be optimized further",
    "# Ensure this works with the latest API changes",
    "# Refactor if necessary",
    "# Legacy code, consider updating",
    "# Potential performance bottleneck"
]

def get_standard_library_names():
    """Returns a set of all top-level names in the standard library."""
    stdlib_names = set(sys.builtin_module_names)
    for module_info in pkgutil.iter_modules():
        stdlib_names.add(module_info.name)
    for module in sys.modules:
        if module in stdlib_names:
            continue
        try:
            imported_module = __import__(module)
            for attr in dir(imported_module):
                stdlib_names.add(attr)
        except ImportError:
            continue
    return stdlib_names

def modify_code(code):
    tree = parso.parse(code)
    built_in_names = set(dir(builtins))
    stdlib_names = get_standard_library_names()
    imported_names = set()
    preserved_import_statements = []

    def track_imports_and_functions(node):
        if node.type in {'import_from', 'import_name'}:
            preserved_import_statements.append((node.start_pos, node.get_code().strip()))
            for name in node.get_defined_names():
                imported_names.add(name.value)
                parts = name.value.split('.')
                imported_names.add(parts[0])
                imported_names.add(name.value)
        if hasattr(node, 'children'):
            for child in node.children:
                track_imports_and_functions(child)
        elif node.type == 'atom_expr':
            # Track function calls to avoid renaming them
            if node.children and isinstance(node.children[0], parso.python.tree.Name):
                function_call_name = node.children[0].value
                imported_names.add(function_call_name)

    def should_rename(node):
        """Determine if a node should be renamed."""
        if node.type != 'name':
            return False

        # Skip renaming if it's a built-in, standard library, or an imported name
        if node.value in built_in_names or node.value in stdlib_names or node.value in imported_names:
            return False

        # For dot-notated imports, ensure the entire path is preserved
        code = node.get_code()
        for imp_name in imported_names:
            if code == imp_name or code.startswith(imp_name + '.'):
                return False

        return True

    def rename_variable(node):
        if hasattr(node, 'children'):
            for child in node.children:
                rename_variable(child)
        if should_rename(node):
            node.value = 'cloned_' + node.value

    def modify_comments_in_prefix(prefix):
        lines = prefix.splitlines(keepends=True)
        modified_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith('#'):
                action = random.choice(["delete", "replace", "keep"])
                if action == "replace":
                    modified_lines.append(' ' * (len(line) - len(stripped_line)) + random.choice(meaningful_comments) + "\n")
                elif action == "delete":
                    continue
                else:
                    modified_lines.append(line)
            else:
                modified_lines.append(line)
        return ''.join(modified_lines)

    def modify_prefixes(node):
        if hasattr(node, 'prefix'):
            node.prefix = modify_comments_in_prefix(node.prefix)
        if hasattr(node, 'children'):
            for child in node.children:
                modify_prefixes(child)

    # Track all import statements and function calls to preserve them
    track_imports_and_functions(tree)

    # Traverse the AST and apply changes, skipping preserved import statements and function calls
    rename_variable(tree)
    modify_prefixes(tree)

    # Generate the modified code
    modified_code = tree.get_code().splitlines()

    # Reinsert the preserved import statements exactly as they were
    for pos, statement in preserved_import_statements:
        line_number = pos[0] - 1  # Convert 1-based line number to 0-based index
        modified_code[line_number] = statement

    return "\n".join(modified_code)

def clone_python_file(src_file_path, dst_file_path):
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

            if file_name.endswith('.py'):
                clone_python_file(src_file_path, dst_file_path)
            else:
                shutil.copy2(src_file_path, dst_file_path)

if __name__ == "__main__":
    src_folder = "python_scripts_dataset"
    dst_folder = "type02SamplePython"

    clone_folder(src_folder, dst_folder)

    print(f"Cloning completed. All files and folders from '{src_folder}' have been cloned to '{dst_folder}'.")
