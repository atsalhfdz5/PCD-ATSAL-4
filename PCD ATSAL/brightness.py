import imageio as img 
import numpy as np 
import matplotlib.pyplot as plt

def bright(image,factor):
    bright_image = image.astype(np.float32)
    bright_image += bright_image + factor
    
    bright_image = np.clip(bright_image,0,255)
    
    return bright_image.astype(np.uint8)

image = img.imread("C:\PCD ATSAL\ea8c1519f8aee1dfc5cf5d5454844927.jpg")
br_image = bright(image,50)

plt.figure(figsize=(15,8))
plt.subplot(2,1,1)
plt.imshow(image)
plt.subplot(2,1,2)
plt.imshow(br_image)
plt.show()

