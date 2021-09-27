import numpy as np

def regular_stretching(image):
    zero_matrix = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            zero_matrix[i, j] = 255 * ((image[i, j]-np.min(image))/(np.max(image)-np.min(image)))
    return zero_matrix

def clip_stretching(image):
    zero_matrix = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            zero_matrix[i, j] = np.clip((255 * (image[i, j]-np.min(image))/(np.max(image)-np.min(image))), np.min(image), np.max(image))
    return zero_matrix