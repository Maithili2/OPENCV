import os

# Base directory path
base_dir = os.getcwd()  # Current working directory (modify if needed)

# Loop through folders practical_04 to practical_08
for i in range(4, 9):  # Loop from 4 to 8
    # Construct folder paths
    folder_name = f"practical_0{i}"
    folder_path = os.path.join(base_dir, folder_name)
    images_path = os.path.join(folder_path, "images")
    
    # Create folders
    os.makedirs(images_path, exist_ok=True)  # Create both practical_0X and images
    
    # Create main.py in the main folder (not inside images)
    main_py_path = os.path.join(folder_path, "main.py")
    if not os.path.exists(main_py_path):
        with open(main_py_path, "w") as f:
            f.write("# Main script for practical_0{}\n".format(i))
        print(f"Created: {main_py_path}")
    else:
        print(f"Already exists: {main_py_path}")
