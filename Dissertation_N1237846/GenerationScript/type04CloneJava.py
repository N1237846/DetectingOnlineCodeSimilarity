import os
import re
import random
import shutil

def generate_type_4_clone(content):
    """
    Generate a Type 4 clone by significantly modifying the script content.
    This involves changing algorithms, altering data structures, etc.
    
    Parameters:
    - content: str, the original script content
    
    Returns:
    - str, the modified script content for Type 4 clone
    """
    modified_content = content

    # Example: Change method names and their calls
    modified_content = re.sub(r'\bmain\b', 'execute', modified_content)
    modified_content = re.sub(r'\bSystem\.out\.println\b', 'System.out.print', modified_content)
    
    # Example: Change sorting algorithm from bubble sort to insertion sort
    modified_content = re.sub(r'void bubbleSort\((.*?)\)', r'void insertionSort(\1)', modified_content)
    modified_content = re.sub(r'bubbleSort\((.*?)\);', r'insertionSort(\1);', modified_content)
    
    # Insert a new dummy method
    insert_pos = modified_content.find('public class')
    new_method = "\n    public static void dummyMethod() {\n        System.out.print(\"This is a dummy method.\");\n    }\n"
    modified_content = modified_content[:insert_pos] + new_method + modified_content[insert_pos:]
    
    # Example: Replace loops with different logic (for demonstration purposes)
    modified_content = re.sub(r'for\s*\(\s*int\s+i\s*=\s*0\s*;\s*i\s*<\s*n\s*;\s*i\s*\+\+\s*\)', 'for (int i = n-1; i >= 0; i--)', modified_content)

    return modified_content

def create_type_4_clones(source_dir, dest_dir, num_clones):
    """
    Create Type 4 clones of all Java scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original Java scripts
    - dest_dir: str, the directory where the clones will be saved
    - num_clones: int, the number of clones to generate for each script
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # List all Java scripts in the source directory
    scripts = [f for f in os.listdir(source_dir) if f.endswith('.java')]
    
    # Generate Type 4 clones for each script
    for script in scripts:
        script_path = os.path.join(source_dir, script)
        with open(script_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        for i in range(num_clones):
            # Generate Type 4 clone content
            clone_content = generate_type_4_clone(original_content)
            
            # Write the clone content to a new file
            clone_name = f"{os.path.splitext(script)[0]}_type4_clone_{i+1}.java"
            clone_path = os.path.join(dest_dir, clone_name)
            with open(clone_path, 'w', encoding='utf-8') as file:
                file.write(clone_content)
            
            print(f"Created Type 4 clone: {clone_path}")
    
    print(f"Successfully created {num_clones} Type 4 clones for each of {len(scripts)} scripts.")

# Example usage
source_directory = 'java_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type04SampleJava'  # Update this path to your destination directory
number_of_clones = 1  # Set the number of clones you want for each script

create_type_4_clones(source_directory, destination_directory, number_of_clones)
