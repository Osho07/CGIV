import cv2
import numpy as np

# Load the image
image = cv2.imread("C:\\Users\\manis\\OneDrive\\Pictures\\IMG_20231218_235235_307.jpg", cv2.IMREAD_GRAYSCALE)

# Edge detection using Canny
edges_canny = cv2.Canny(image, 100, 200)

# Edge detection using Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Edge detection using Laplacian of Gaussian
log = cv2.Laplacian(image, cv2.CV_64F)

# Texture extraction using Gabor filter
def apply_gabor_filter(image, ksize=31, sigma=4.0, theta=0, lambd=10.0, gamma=0.5, psi=0):
    kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_32F)
    return cv2.filter2D(image, cv2.CV_8UC3, kernel)

gabor_filtered = apply_gabor_filter(image)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges_canny)
cv2.imshow('Sobel Edges', sobel_combined / np.max(sobel_combined))  # Normalize for display
cv2.imshow('Laplacian of Gaussian (LoG)', log / np.max(log))  # Normalize for display
cv2.imshow('Gabor Filtered Texture', gabor_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()