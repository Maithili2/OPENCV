import os

# Base directory path
base_dir = os.getcwd()  # Current working directory (can be modified if needed)

# Create folders from practical_04 to practical_08
for i in range(4, 9):  # Loop from 4 to 8
    folder_name = f"practical_0{i}/images"  # Construct folder name
    folder_path = os.path.join(base_dir, folder_name)  # Full path

    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")
