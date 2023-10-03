# 15.Load an image as a Mumpy array. Perform image manipulations such as cropping,resizing and color channel conversions. Visualize the original and modified images using Matplotlib.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open(r'CO1\NumPy, Matplotlib Questions\sample.jpg')
original_image = np.array(image)


crop_box = (100, 100, 400, 400)  
cropped_image = original_image[crop_box[1]:crop_box[3], crop_box[0]:crop_box[2]]

new_size = (200, 200)
resized_image = image.resize(new_size)
resized_array = np.array(resized_image)

gray_image = image.convert('L')
gray_array = np.array(gray_image)

plt.figure(figsize=(12, 4))

plt.subplot(1, 4, 1)
plt.imshow(original_image)
plt.title('Original Image')

plt.subplot(1, 4, 2)
plt.imshow(cropped_image)
plt.title('Cropped Image')

plt.subplot(1, 4, 3)
plt.imshow(resized_array)
plt.title('Resized Image')

plt.subplot(1, 4, 4)
plt.imshow(gray_array, cmap='gray')
plt.title('Grayscale Image')

plt.tight_layout()
plt.show()