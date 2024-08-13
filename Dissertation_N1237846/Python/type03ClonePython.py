import os
import ast
import astor
import random
import shutil

# Predefined list of meaningful words or sentences
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

def insert_logging(node):
    """Inserts a logging statement at the beginning of each function."""
    if isinstance(node, ast.FunctionDef):
        new_node = ast.parse("print('Entering function: {}')".format(node.name)).body[0]
        node.body.insert(0, new_node)
    return node

def is_safe_to_rearrange(node):
    """Determine if a statement is safe to rearrange."""
    return isinstance(node, (ast.Expr, ast.Assign, ast.Pass, ast.AugAssign))

def rearrange_code_blocks(node):
    """Rearrange safe code blocks within functions, avoiding control structures."""
    if isinstance(node, ast.FunctionDef):
        # Separate safe-to-move statements and other statements
        safe_statements = []
        other_statements = []
        for stmt in node.body:
            if is_safe_to_rearrange(stmt):
                safe_statements.append(stmt)
            else:
                other_statements.append(stmt)

        # Shuffle safe statements
        random.shuffle(safe_statements)

        # Combine shuffled safe statements with other statements
        node.body = safe_statements + other_statements
    return node

def modify_loops(node):
    """Transforms loops by changing their structure."""
    if isinstance(node, ast.For):
        # Convert a for-loop to a while-loop as an example
        target = node.target
        iter_ = node.iter
        body = node.body
        if isinstance(iter_, ast.Call) and isinstance(iter_.func, ast.Name):
            if iter_.func.id == 'range':  # Assuming a simple range loop
                init = ast.Assign(targets=[target], value=ast.Constant(value=0))
                test = ast.Compare(left=target, ops=[ast.Lt()], comparators=iter_.args)
                update = ast.AugAssign(target=target, op=ast.Add(), value=ast.Constant(value=1))
                body.append(update)  # Increment step
                new_node = ast.While(test=test, body=body, orelse=node.orelse)
                return [init, new_node]  # Need to return multiple statements
    return node

def invert_conditionals(node):
    """Invert conditional statements to create structural differences."""
    if isinstance(node, ast.If):
        if node.orelse:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.body, node.orelse = node.orelse, node.body  # Swap branches
    return node

def rename_variables(tree):
    """Randomly rename variables in the code."""
    class VariableRenamer(ast.NodeTransformer):
        def __init__(self):
            self.mapping = {}

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store):  # Variable being assigned
                new_name = "var_" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
                self.mapping[node.id] = new_name
                node.id = new_name
            elif isinstance(node.ctx, ast.Load):  # Variable being used
                if node.id in self.mapping:
                    node.id = self.mapping[node.id]
            return node

    return VariableRenamer().visit(tree)

def modify_string_literals(tree):
    """Modify string literals in the code to meaningful words or sentences."""
    class StringLiteralModifier(ast.NodeTransformer):
        def visit_Str(self, node):
            # Replace the string content with a meaningful sentence
            new_str = random.choice(meaningful_sentences)
            return ast.copy_location(ast.Str(s=new_str), node)

    return StringLiteralModifier().visit(tree)

def add_redundant_code(node):
    """Add redundant code that does not affect the logic."""
    if isinstance(node, ast.FunctionDef):
        noop_node = ast.Pass()
        node.body.insert(random.randint(0, len(node.body)), noop_node)  # Insert no-op randomly
    return node

def apply_modifications(tree):
    """Apply all modifications to the AST."""
    for node in ast.walk(tree):
        node = insert_logging(node)
        node = rearrange_code_blocks(node)
        node = modify_loops(node)
        node = invert_conditionals(node)
        node = add_redundant_code(node)

    # Rename variables across the entire tree
    tree = rename_variables(tree)

    # Modify string literals across the entire tree
    tree = modify_string_literals(tree)
    return tree

def process_file(file_path, clone_folder):
    """Processes a single Python file to generate its Type III clone."""
    with open(file_path, 'r', encoding='utf-8') as source_file:
        original_code = source_file.read()

    # Parse the original code into an AST
    tree = ast.parse(original_code)

    # Apply modifications to the AST
    modified_tree = apply_modifications(tree)

    # Convert the modified AST back to source code
    modified_code = astor.to_source(modified_tree)

    # Prepare the clone file path
    relative_path = os.path.relpath(file_path, os.path.dirname(file_path))
    clone_file_path = os.path.join(clone_folder, relative_path)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(clone_file_path), exist_ok=True)

    # Write the modified code to the new clone file
    with open(clone_file_path, 'w', encoding='utf-8') as clone_file:
        clone_file.write(modified_code)

def clone_folder(original_folder, clone_folder):
    """Transforms all Python files in the original folder into Type III clones and saves them in the clone folder."""
    if not os.path.exists(clone_folder):
        os.makedirs(clone_folder)

    for root, _, files in os.walk(original_folder):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                process_file(file_path, clone_folder)
            else:
                # Copy non-Python files directly
                src_file_path = os.path.join(root, file_name)
                dst_file_path = os.path.join(clone_folder, os.path.relpath(src_file_path, original_folder))
                os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
                shutil.copy2(src_file_path, dst_file_path)

if __name__ == "__main__":
    original_folder = "python_scripts_dataset"
    clone_folder_name = "type03SamplePython"
    clone_folder(original_folder, clone_folder_name)
    print(f"Type III clones have been generated and saved to '{clone_folder_name}'.")
