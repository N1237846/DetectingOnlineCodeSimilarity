import os
import shutil

def create_type_1_clones(source_dir, dest_dir, num_clones):
    """
    Create Type 1 clones of all Java scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original Java scripts
    - dest_dir: str, the directory where the clones will be saved
    - num_clones: int, the number of times each script should be cloned
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # List all Java scripts in the source directory
    scripts = [f for f in os.listdir(source_dir) if f.endswith('.java')]
    
    # Clone each script the specified number of times
    for script in scripts:
        script_path = os.path.join(source_dir, script)
        for i in range(num_clones):
            clone_name = f"{os.path.splitext(script)[0]}_clone_{i + 1}.java"
            clone_path = os.path.join(dest_dir, clone_name)
            shutil.copyfile(script_path, clone_path)
            print(f"Copied {script} to {clone_path}")
    
    print(f"Successfully created {num_clones} Type 1 clones for each of {len(scripts)} scripts.")

# Example usage
source_directory = 'java_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type01SampleJava'  # Update this path to your destination directory
number_of_clones = 1  # Set the number of clones you want for each script

create_type_1_clones(source_directory, destination_directory, number_of_clones)
