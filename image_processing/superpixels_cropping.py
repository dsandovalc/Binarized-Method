import cv2
import glob
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float

def cropping(image_path, save_path, n_segments = 6, sigma = 200, start_label = 0, spacing = None):
    image = cv2.imread(image_path)
    segments = slic(img_as_float(image), n_segments=n_segments, sigma=sigma, start_label=start_label, spacing=spacing)

    fig = plt.figure("Superpixels")
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments, color=(0,1,0)))

    plt.show()

    for (i, segmentation_value) in enumerate(np.unique(segments)):
        print("--> Inspecting segment {}".format(i+1))
        mask = np.zeros(image.shape[:2], dtype="uint8")
        mask[segments == segmentation_value] = 255
        result = cv2.bitwise_and(image, image, mask=mask)

        cv2.imshow('Segmentation', result)
        cv2.imwrite('{}segmentation_mask_{}.png'.format(save_path,i+1), result)
        cv2.waitKey()

    return


def remove_mask(path_of_images_with_mask, save_path):
    images = glob.glob(path_of_images_with_mask)
    
    for i, image_mask in enumerate(images):
        s = image_mask.split('/')
        img = Image.open(image_mask)
        imageBox = img.getbbox()
        cropped = img.crop(imageBox)
        cropped.save('{}mask_remove_{}'.format(save_path,s[-1]))
    return

def stack_plot_cropped_img_in_full_img(full_blur_image,cropped_img_binarized_path,second_img_binarized_path):

    x, y = 0, 0
    
    for n, binarized_cropped in enumerate(sorted(cropped_img_binarized_path)):
        img_cropped = cv2.imread(binarized_cropped)
        if n > 3:
            img_cropped = cv2.imread('{}/80_mask_remove_segmentation_mask_{}.png'.format(second_img_binarized_path,n+1))
        
        print('{} --> {}: ({},{})'.format(binarized_cropped, n+1, img_cropped.shape[0]*x, img_cropped.shape[1]*(y%2)))
        
        for i in range(img_cropped.shape[0]):
            for j in range(img_cropped.shape[1]):
                full_blur_image[(i + ((img_cropped.shape[0]) * x)), (j + ((img_cropped.shape[1]) * (y%2)))] = img_cropped[i,j]
        
        plt.imshow(full_blur_image)
        plt.show()
        
        x = x + y%2
        y = y + 1
        
    return print('Finished!')

def plot_cropped_img_in_full_img(full_blur_image, img_cropped, number_of_images):
    
    x, y = 0, 0
    
    for n in range(0,number_of_images):
        for i in range(img_cropped.shape[0]):
            for j in range(img_cropped.shape[1]):
                full_blur_image[(i + ((img_cropped.shape[0]) * x)), (j + ((img_cropped.shape[1]) * (y%2)))] = img_cropped[i,j]
        
        plt.imshow(full_blur_image)
        plt.show()
        
        x = x + y%2
        y = y + 1
        
    return print('Finished!')