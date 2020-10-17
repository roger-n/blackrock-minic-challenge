import numpy as np
import imageio
import matplotlib.pyplot as plt


img1 = np.asarray(imageio.imread('imageEmbedded.png'))

imgs = np.zeros_like(img1)

for i in range(len(img1)):
    for j in range(len(img1[0])):
        imgs[i][j] = np.array([img1[i][j] << 6])

plt.imshow(imgs)
plt.show()