import cv2
import numpy as np
import os

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

# 4. Cropping (ensure valid crop indices)
start_row, end_row = 100, min(300, rows)  # Ensure indices are within bounds
start_col, end_col = 200, min(400, cols)
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
