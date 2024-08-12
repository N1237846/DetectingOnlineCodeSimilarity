import os
import shutil

def create_type_1_clones(source_dir, destination_dir, num_clones):
    """
    Create Type 1 clones (exact copies) of all C++ scripts from the source directory to the destination directory.
    
    Parameters:
    - source_dir: str, the directory containing the original C++ scripts
    - destination_dir: str, the directory where the clones will be saved
    - num_clones: int, the number of times each script should be cloned
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # List all C++ scripts in the source directory
    scripts = [f for f in os.listdir(source_dir) if f.endswith('.cpp')]
    
    # Clone each script the specified number of times
    for script in scripts:
        script_path = os.path.join(source_dir, script)
        with open(script_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        for i in range(num_clones):
            clone_name = f"{os.path.splitext(script)[0]}_clone_{i + 1}.cpp"
            clone_path = os.path.join(destination_dir, clone_name)
            
            with open(clone_path, 'w', encoding='utf-8') as clone_file:
                clone_file.write(content)
    
    print(f"Successfully created {num_clones} Type 1 clones for each of {len(scripts)} scripts.")

# Example usage
source_directory = 'c++_scripts_dataset'  # Update this path to your source directory
destination_directory = 'type01SampleC++'  # Update this path to your destination directory
number_of_clones = 1  # Set the number of clones you want for each script

create_type_1_clones(source_directory, destination_directory, number_of_clones)