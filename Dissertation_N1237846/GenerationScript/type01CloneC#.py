import os
import shutil

def create_type_1_clones(source_dir, dest_dir):
    """
    Create Type 1 clones of all C# scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original C# scripts (including subdirectories)
    - dest_dir: str, the directory where the cloned scripts will be saved
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # Walk through the source directory and find all .cs files
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.cs'):
                src_path = os.path.join(root, file)
                clone_name = f"{os.path.splitext(file)[0]}_clone.cs"
                dest_path = os.path.join(dest_dir, clone_name)
                
                # Copy the file
                shutil.copy2(src_path, dest_path)
                print(f"Cloned {src_path} to {dest_path}")

    print(f"Successfully created Type 1 clones for all C# scripts in {dest_dir}")

# Example usage
source_directory = 'c#_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type01SampleC#'  # Update this path to your destination directory

create_type_1_clones(source_directory, destination_directory)
