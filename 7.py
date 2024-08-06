import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("C:/Users/AI06GF13/Downloads/Image/pup.jpg")

# Get the dimensions of the image
height, width, _ = image.shape

# Calculate the center of the image
center_x, center_y = width // 2, height // 2

# Split the image into four quadrants
top_left = image[:center_y, :center_x]
top_right = image[:center_y, center_x:]
bottom_left = image[center_y:, :center_x]
bottom_right = image[center_y:, center_x:]

# Display the quadrants
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.title('Top Left')
plt.imshow(cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB))

plt.subplot(2, 2, 2)
plt.title('Top Right')
plt.imshow(cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB))

plt.subplot(2, 2, 3)
plt.title('Bottom Left')
plt.imshow(cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB))

plt.subplot(2, 2, 4)
plt.title('Bottom Right')
plt.imshow(cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()
