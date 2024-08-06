import cv2
import numpy as np

# Load the image
image = cv2.imread("C:\\Users\\manis\\OneDrive\\Pictures\\IMG20240319160844.jpg")

# Get the image dimensions
(h, w) = image.shape[:2]

# Define the center of the image for rotation
center = (w // 2, h // 2)

# Rotation matrix (rotate by 45 degrees)
angle = 45
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# Scaling matrix (scale by 0.5)
scaled_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Translation matrix (translate by 50 pixels right and 50 pixels down)
translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]])
translated_image = cv2.warpAffine(image, translation_matrix, (w, h))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Translated Image', translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()