import cv2

# Load the image
image = cv2.imread("C:\\Users\\\manis\\OneDrive\\Pictures\\IMG_20240604_155347_055.jpg")

# Apply Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)

# Apply Median Blur
median_blur = cv2.medianBlur(image, 15)

# Apply Bilateral Filter
bilateral_filter = cv2.bilateralFilter(image, 15, 75, 75)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Filter', bilateral_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()