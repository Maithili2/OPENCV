# Main script for practical_05
import cv2
import numpy as np
import os

# Define the path to the image
image_path = os.path.join(os.getcwd(), 'images', 'img1.jpg')

# Read the image
img = cv2.imread(image_path)

# Check if the image is loaded successfully
if img is None:
    print(f"Error: Unable to load image from {image_path}")
    exit(1)

# Make a copy of the original image to preserve it
original_img = img.copy()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges using the Canny edge detector
edges = cv2.Canny(gray, 50, 150)

# Apply Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Draw detected lines on the original image
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Concatenate the original and processed images side by side
combined_image = cv2.hconcat([original_img, img])

# Display the concatenated image
cv2.imshow('Original and Hough Transform', combined_image)

# Wait for the 'q' key to be pressed to close the window
while True:
    key = cv2.waitKey(1)  # waits for key press for 1 ms
    if key == ord('q'):  # if 'q' is pressed, close the window
        break

cv2.destroyAllWindows()
