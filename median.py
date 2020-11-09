import numpy as np
import random
import cv2
from matplotlib import pyplot as plt

### Function to add salt and pepper noise using operations on each pixel
# def sp_noise(image,prob):
#     output = np.zeros(image.shape,np.uint8)
#     thres = 1 - prob 
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             rdn = random.random()
#             if rdn < prob:
#                 output[i][j] = 0
#             elif rdn > thres:
#                 output[i][j] = 255
#             else:
#                 output[i][j] = image[i][j]
#     return output

def sp_noise(image, prob):
    output = image.copy()
    if len(image.shape) == 2:
        black = 0
        white = 255            
    else:
        colorspace = image.shape[2]
        if colorspace == 3:  # RGB
            black = np.array([0, 0, 0], dtype='uint8')
            white = np.array([255, 255, 255], dtype='uint8')
        else:  # RGBA
            black = np.array([0, 0, 0, 255], dtype='uint8')
            white = np.array([255, 255, 255, 255], dtype='uint8')
    probs = np.random.random(image.shape)
    image[probs < (prob / 2)] = black
    image[probs > 1 - (prob / 2)] = white
    return image

image = cv2.imread("input images/lena.jpg",0) 
noise_img = sp_noise(image,0.30)
cv2.imwrite('output/lenanoise.jpg', noise_img)


img = cv2.imread('output/lenanoise.jpg')
median = cv2.medianBlur(img, 5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('median')
plt.xticks([]), plt.yticks([])
plt.show()
