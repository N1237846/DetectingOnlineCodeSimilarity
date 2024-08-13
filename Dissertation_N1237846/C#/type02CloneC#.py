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

# Extended list of standard C# names to preserve
CSharp_STANDARD_NAMES = set([
    "Console", "WriteLine", "Write", "ReadLine", "ReadKey", "Clear",
    "List", "Add", "Remove", "Find", "Sort", "Count",
    "Dictionary", "TryGetValue", "Keys", "Values",
    "Queue", "Enqueue", "Dequeue", "Peek",
    "Stack", "Push", "Pop", "Peek", "Contains",
    "DateTime", "Now", "Today", "AddDays", "ToString",
    "Math", "Abs", "Pow", "Sqrt", "Round",
    "String", "Concat", "Compare", "Equals", "Substring", "Replace",
    "StreamReader", "ReadLine", "ReadToEnd", "Close",
    "StreamWriter", "WriteLine", "Write", "Flush", "Close",
    "File", "ReadAllText", "WriteAllText", "Delete", "Exists",
    "Task", "Run", "Wait", "ContinueWith", "WhenAll",
    "HttpClient", "GetStringAsync", "PostAsync", "SendAsync",
    "Thread", "Start", "Sleep", "Join", "Abort",
    "Action", "Func", "ValueTuple",
    "IEnumerable", "IEnumerator",
    "Nullable",
    "static", "void", "public", "private", "protected", "internal",
    "class", "interface", "enum", "struct", "new", "this", "base", "null",
    "true", "false", "var", "dynamic", "object", "sizeof", "typeof",
    "as", "is", "operator", "event", "delegate", "async", "await",
    "partial", "unsafe", "checked", "unchecked", "default", "extern",
    "ref", "out", "in", "params", "yield",
    "Main",
    "Console", "WriteLine", "Write", "ReadLine", "int", "string", "void", "bool", "char",
    "double", "float", "decimal", "if", "else", "for", "foreach", "while", "do",
    "switch", "case", "default", "break", "continue", "return", "try", "catch",
    "finally", "throw", "using", "namespace", "class", "struct", "interface",
    "public", "private", "protected", "internal", "static", "readonly", "const",
    "virtual", "override", "abstract", "sealed", "new", "base", "this", "null",
    "true", "false", "var", "dynamic", "object", "sizeof", "typeof", "as", "is",
    "operator", "event", "delegate", "async", "await", "partial", "unsafe",
    "checked", "unchecked", "default", "enum", "extern", "ref", "out",
    "in", "params", "yield", "main", "List", "Dictionary", "DateTime", "File",
    "StreamReader", "StreamWriter", "Task", "HttpClient", "Thread", "ThreadPool",
    "Action", "Func", "Task", "ValueTuple", "IEnumerable", "IEnumerator",
    "Collection", "Queue", "Stack", "Nullable", "Clear", "ReadKey", "Add", "get", "set",
    "Parse", "RemoveAt", "Remove", "IndexOf", "Substring",
    # Additional built-in functions
    "Math.Abs", "Math.Sqrt", "Math.Pow", "Math.Max", "Math.Min", "String.Length",
    "String.Concat", "String.Compare", "String.Contains", "String.Replace",
    "String.ToUpper", "String.ToLower", "String.Substring", "Array.Sort",
    "Array.Reverse", "Array.IndexOf", "DateTime.Now", "DateTime.Today",
    "DateTime.AddDays", "DateTime.AddMonths", "DateTime.AddYears", "DateTime.ToString",
    # Additional built-in methods
    "List.Add", "List.Remove", "List.RemoveAt", "List.Clear", "List.Contains",
    "List.Count", "List.IndexOf", "Dictionary.Add", "Dictionary.Remove",
    "Dictionary.ContainsKey", "Dictionary.ContainsValue", "Dictionary.Clear",
    "Dictionary.TryGetValue", "Queue.Enqueue", "Queue.Dequeue", "Stack.Push",
    "Stack.Pop",
    # Additional built-in libraries (namespaces)
    "System", "System.IO", "System.Text", "System.Net", "System.Collections",
    "System.Collections.Generic", "System.Linq", "System.Threading",
    "System.Threading.Tasks", "System.Xml", "System.Data", "System.Diagnostics",
    "System.Drawing", "System.Windows.Forms", "System.Web"
])

def preserve_output_statements(code):
    """Preserve content inside Console.WriteLine, Console.Write, etc., and temporarily replace them with placeholders."""
    placeholders = []

    def replacer(match):
        placeholders.append(match.group(0))
        return "PLACEHOLDER_FOR_OUTPUT"

    # Preserve Console.WriteLine and Console.Write content
    code = re.sub(r'(Console\.WriteLine\(".*?"\)|Console\.Write\(".*?"\))', replacer, code)

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

def is_standard_name(name):
    """Check if the name is in the list of standard C# names."""
    return name in CSharp_STANDARD_NAMES

def replace_variable_names(code):
    """Replace variable names with new names, while preserving specific names."""
    def rename_match(match):
        name = match.group(0)
        if not is_standard_name(name) and not name.startswith("PLACEHOLDER"):
            return generate_random_name(name)
        return name

    # Find all identifiers and replace them
    code = re.sub(r'\b[a-zA-Z_]\w*\b', rename_match, code)
    return code

def generate_random_name(name):
    """Generate a new name for variables by adding a prefix."""
    return f"cloned_{name}"

def modify_code(code):
    """Modify code by changing comments and variable names."""
    code, output_placeholders = preserve_output_statements(code)
    code_with_modified_comments = replace_comments(code)
    modified_code = replace_variable_names(code_with_modified_comments)
    modified_code = restore_output_statements(modified_code, output_placeholders)
    return modified_code

def clone_csharp_file(src_file_path, dst_file_path):
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

            if file_name.endswith('.cs'):
                clone_csharp_file(src_file_path, dst_file_path)
            else:
                shutil.copy2(src_file_path, dst_file_path)

if __name__ == "__main__":
    src_folder = "c#_scripts_dataset"
    dst_folder = "type02SampleC#"

    clone_folder(src_folder, dst_folder)

    print(f"Cloning completed. All files and folders from '{src_folder}' have been cloned to '{dst_folder}'.")
