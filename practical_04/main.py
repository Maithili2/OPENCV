import cv2
import numpy as np
import os
import random

# Define the path to the image
image_path = os.path.join(os.getcwd(), 'images', 'img1.jpg')

# Load the image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print(f"Error: Unable to load image from {image_path}. Please check the path.")
    exit(1)

# 1. Negative Transformation
negative_image = 255 - image

# 2. Logarithmic Transformation
c = 255 / np.log(1 + np.max(image))  # Scaling constant
log_transformed_image = c * np.log1p(image)  # log1p ensures log(1 + image) computation
log_transformed_image = np.uint8(np.clip(log_transformed_image, 0, 255))  # Scale to uint8

# 3. Affine Transformation (rotation by 45 degrees)
rows, cols = image.shape
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
affine_transformed_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

# 4. Random Cropping (without manually specifying crop indices)
crop_height = 200  # Crop height
crop_width = 200   # Crop width

# Ensure the crop size does not exceed image dimensions
if crop_height > rows or crop_width > cols:
    print("Error: Crop size is larger than image dimensions.")
    exit(1)

# Generate random start row and column within the valid range
start_row = random.randint(0, rows - crop_height)
start_col = random.randint(0, cols - crop_width)

# Calculate the end row and column based on the start position and crop size
end_row = start_row + crop_height
end_col = start_col + crop_width

# Crop the image
cropped_image = image[start_row:end_row, start_col:end_col]

# Display the transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)
cv2.imshow('Logarithmic Transformation', log_transformed_image)
cv2.imshow('Affine Transformation', affine_transformed_image)
cv2.imshow('Cropped Image', cropped_image)

# Wait for key press to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
