import cv2
import numpy as np
import os
# Load the image with a Windows-compatible path
image_path_os = os.path.join(os.getcwd(), 'images', 'img1.jpg')
image_path =image_path_os
image = cv2.imread(image_path)


# Check if the image is loaded successfully
if image is None:
    print(f"Error: Unable to load image at {image_path}. Please check the file path.")
    exit()

# Get image dimensions
rows, cols = image.shape[:2]

# Translation
M_translation = np.float32([[1, 0, 50], [0, 1, 30]])  # Translation matrix
translated_image = cv2.warpAffine(image, M_translation, (cols, rows))

# Rotation
center = (cols // 2, rows // 2)
angle = 45  # Rotation angle in degrees
M_rotation = cv2.getRotationMatrix2D(center, angle, 1)  # Scale = 1 (no scaling)
rotated_image = cv2.warpAffine(image, M_rotation, (cols, rows))

# Scaling
scaling_factor = 1.5
scaled_image = cv2.resize(
    image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_LINEAR
)

# Shearing
M_shearing = np.float32([[1, 0.5, 0], [0.5, 1, 0]])  # Shearing matrix
sheared_image = cv2.warpAffine(image, M_shearing, (cols, rows))

# Reflection (Horizontal flip)
reflected_image = cv2.flip(image, 1)

# Displaying the images
cv2.imshow('Original', image)
cv2.imshow('Translated', translated_image)
cv2.imshow('Rotated', rotated_image)
cv2.imshow('Scaled', scaled_image)
cv2.imshow('Sheared', sheared_image)
cv2.imshow('Reflected', reflected_image)

# Keep windows open until manually closed
while True:
    # Check for any window closure
    if (
        cv2.getWindowProperty('Original', cv2.WND_PROP_VISIBLE) < 1 or
        cv2.getWindowProperty('Translated', cv2.WND_PROP_VISIBLE) < 1 or
        cv2.getWindowProperty('Rotated', cv2.WND_PROP_VISIBLE) < 1 or
        cv2.getWindowProperty('Scaled', cv2.WND_PROP_VISIBLE) < 1 or
        cv2.getWindowProperty('Sheared', cv2.WND_PROP_VISIBLE) < 1 or
        cv2.getWindowProperty('Reflected', cv2.WND_PROP_VISIBLE) < 1
    ):
        break
    cv2.waitKey(100)

# Close all windows
cv2.destroyAllWindows()
