import cv2
import os

# Create a portable path for the input image
image_folder = os.path.join(os.getcwd(), 'images')  # Folder path
image_path = os.path.join(image_folder, 'img1.jpg')  # Full input image path

# Check if the image exists
if not os.path.exists(image_path):
    print(f"Error: The file '{image_path}' does not exist.")
else:
    # Read the image
    img = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if img is None:
        print(f"Error: Could not load the image from '{image_path}'.")
    else:
        # Display the image
        cv2.imshow('Original Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Define a portable path for saving the output image
        save_folder = os.path.join(os.getcwd(), 'output_images')  # Output folder path
        os.makedirs(save_folder, exist_ok=True)  # Create the folder if it doesn't exist
        save_path = os.path.join(save_folder, 'img2.png')  # Full output image path

        # Save the image
        cv2.imwrite(save_path, img)
        print(f"Image saved successfully at: {save_path}")

print("Done....!")
