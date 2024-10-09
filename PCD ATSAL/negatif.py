import imageio.v3 as img 
import numpy as np
import matplotlib.pyplot as plt

path = "C:\PCD ATSAL\make-blurry-girl-image-clear-with-Fotor-ai-image-enhancer.webp"

image = img.imread(path)
image_neg = 255 - image

r_image = image[:,:,0]
r_neg = image_neg[:,:,0]

hist_r, bits_r = np.histogram(r_image.flatten(), bins=256, range =[0,256])
hist_r, bits_r_neg  = np.histogram(r_image.flatten(), bins=256, range =[0,256])

plt.figure(figsize=(10,7))

plt.subplot(2,1,1)
plt.plot(hist_r, color="blue", label="Histogram R awal")
plt.legend()

plt.subplot(2,1,2)
plt.imshow(image_neg)
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(image)
plt.axis("off")

plt.subplot(2,2,3)
plt.plot(hist_r, color="red", label="Histogram R awal")
plt.legend()

plt.show()
img.imwrite("C:\PCD ATSAL\make-blurry-girl-image-clear-with-Fotor-ai-image-enhancerr.webp",image_neg)