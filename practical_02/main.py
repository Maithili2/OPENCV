import cv2
import numpy as np
import os

# Set file paths for Windows
image_path = os.path.join(os.getcwd(), 'images', 'img1.jpg')
input_path = image_path

# Read the input image
img = cv2.imread(input_path)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Unable to load the image at {input_path}. Please check the file path.")
    exit()

# Convert the image to grayscale
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Obtain the complement of the grayscale image
complement_img = 255 - grayscale_img

# Create a binary image using a threshold
_, binary_img = cv2.threshold(grayscale_img, 127, 255, cv2.THRESH_BINARY)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', grayscale_img)
cv2.imshow('Complement Image', complement_img)
cv2.imshow('Binary Image', binary_img)

# Wait for user to close all windows
while True:
    # Check if each window is still open
    if (
        cv2.getWindowProperty('Original Image', cv2.WND_PROP_VISIBLE) < 1
        and cv2.getWindowProperty('Grayscale Image', cv2.WND_PROP_VISIBLE) < 1
        and cv2.getWindowProperty('Complement Image', cv2.WND_PROP_VISIBLE) < 1
        and cv2.getWindowProperty('Binary Image', cv2.WND_PROP_VISIBLE) < 1
    ):
        break
    cv2.waitKey(100)  # Pause briefly

# Destroy all windows
cv2.destroyAllWindows()
