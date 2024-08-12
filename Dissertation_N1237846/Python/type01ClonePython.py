
import os
import shutil

def clone_scripts(source_dir, destination_dir, num_clones):
    """
    Clone all Python scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original Python scripts
    - destination_dir: str, the directory where the clones will be saved
    - num_clones: int, the number of times each script should be cloned
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # List all Python scripts in the source directory
    scripts = [f for f in os.listdir(source_dir) if f.endswith('.py')]
    
    # Clone each script the specified number of times
    for script in scripts:
        script_path = os.path.join(source_dir, script)
        with open(script_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        for i in range(num_clones):
            clone_name = f"{os.path.splitext(script)[0]}_clone_{i + 1}.py"
            clone_path = os.path.join(destination_dir, clone_name)
            with open(clone_path, 'w', encoding='utf-8') as clone_file:
                clone_file.write(content)
    
    print(f"Successfully cloned {len(scripts)} scripts {num_clones} times each.")

# Example usage
source_directory = 'python_scripts_dataset'  # Update this path
destination_directory = 'type01Sample'  # Update this path
number_of_clones = 1  # Set the number of clones you want for each script

clone_scripts(source_directory, destination_directory, number_of_clones)

