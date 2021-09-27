import cv2
import glob
from numpy import *
from .superpixels_cropping import plot_cropped_img_in_full_img

images_path_40_percent = glob.glob('db/output/segmentation_cropped/binary_cropped/40*')
images_path_80_percent = glob.glob('db/output/segmentation_cropped/binary_cropped/80*')
images_path_otsu = glob.glob('db/output/segmentation_cropped/binary_cropped/otsu*')

binary_images_40_percent = stack((images_path_40_percent))
binary_images_80_percent = stack((images_path_80_percent))
binary_images_otsu = stack((images_path_otsu))

full_image = cv2.imread('db/output/blur_cropped/blur_cropped_1.png')

plot_cropped_img_in_full_img(full_image, binary_images_40_percent, 'db/output/segmentation_cropped/binary_cropped')