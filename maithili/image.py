import os
import shutil

# Base path containing the folders practical_0 to practical_8
base_path = "./"  # Update this if your folders are in a different location

# Path to the replacement image
replacement_image = "./img1.jpg"  # Provide the full path to your image here

# Ensure the replacement image exists
if not os.path.exists(replacement_image):
    print(f"Error: Replacement image not found at {replacement_image}")
    exit(1)

# Process each folder (practical_0 to practical_8)
for i in range(9):
    folder_name = f"practical_0{i}/images"  # Path to the images folder
    folder_path = os.path.join(base_path, folder_name)

    if os.path.exists(folder_path):
        # Clear the images folder
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Delete files or symbolic links
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Delete directories
            except Exception as e:
                print(f"Error while deleting {file_path}: {e}")
        
        # Place the replacement image in the folder
        try:
            shutil.copy(replacement_image, folder_path)
            print(f"Image replaced successfully in: {folder_path}")
        except Exception as e:
            print(f"Error while copying to {folder_path}: {e}")
    else:
        print(f"Folder does not exist: {folder_path}")

print("Task completed.")
