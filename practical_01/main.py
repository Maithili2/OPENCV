import cv2
import os

# Use forward slashes in the file path'
image_path = os.path.join(os.getcwd(), 'images', 'img1.jpg')

img = cv2.imread(image_path)

# Display the image
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite('C:/Users/Asus/Downloads/openCV_maithili/openCV/practical_01/images/img2.png', img)

print("Done....!")
