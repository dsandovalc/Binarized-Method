import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float

def cropping(image_path, save_path, n_segments = 6, sigma = 150, start_label = 0, spacing = None, mode='thick', color=(0,1,0)):
    image = cv2.imread(image_path)
    segments = slic(img_as_float(image), n_segments, sigma,start_label, spacing)

    fig = plt.figure("Superpixels")
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments, mode, color))

    plt.show()

    for (i, segmentation_value) in enumerate(np.unique(segments)):
        print("--> Inspecting segment {}".format(i+1))
        mask = np.zeros(image.shape[:2], dtype="uint8")
        mask[segments == segmentation_value] = 255
        result = cv2.bitwise_and(image, image, mask=mask)

        cv2.imshow('Mask', mask)
        cv2.imshow('Segmentation', result)

    return cv2.imwrite("{}segmentation_mask_{}.png".format(save_path,i), result), cv2.waitKey()

def remove_mask(path_of_images_with_mask, save_path):
    for i, image_mask in enumerate(path_of_images_with_mask):
        s = image_mask.split('/')
        img = Image.open(path_of_images_with_mask[i])
        imageBox = img.getbbox()
        cropped = img.crop(imageBox)
    return cropped.save('{}mask_remove_{}'.format(save_path,s[-1]))

def plot_cropped_img_in_full_img(full_blur_image,cropped_img_binarized):
    x, y = 0, 0
    
    for n, binarized_cropped in enumerate(sorted(cropped_img_binarized)):
        img_cropped = cv2.imread(binarized_cropped)
        
        print('--> {}: ({},{})'.format(n, img_cropped.shape[0]*x, img_cropped.shape[1]*(y%2)))
        
        for i in range(img_cropped.shape[0]):
            for j in range(img_cropped.shape[1]):
                full_blur_image[(i + ((img_cropped.shape[0]+1) * x)), (j + ((img_cropped.shape[1]) * (y%2)))] = img_cropped[i,j] + full_blur_image[i,j]/255
        
        plt.imshow(full_blur_image)
        plt.show()
        
        x = x + y%2
        y = y + 1
    return