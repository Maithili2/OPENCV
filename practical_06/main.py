# Main script for practical_06
import cv2

# Read images
img1 = cv2.imread('img-1.jpg')  # Update with the correct image path
img2 = cv2.imread('img-2.jpg')

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Match keypoints
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Draw matches
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None,
                              flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the output
cv2.imshow('SIFT Matches', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()
