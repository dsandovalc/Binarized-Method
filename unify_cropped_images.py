import cv2
import glob
from numpy import *
from image_processing import superpixels_cropping

images_path_50_percent = glob.glob('db/output/segmentation_cropped/binary_cropped/50*')
images_path_80_percent = glob.glob('db/output/segmentation_cropped/binary_cropped/80*')
images_path_otsu = glob.glob('db/output/segmentation_cropped/binary_cropped/otsu*')
binary_images_50_percent = stack((images_path_50_percent))
binary_images_80_percent = stack((images_path_80_percent))
binary_images_otsu = stack((images_path_otsu))

full_image = cv2.imread('db/output/blur_cropped/blur_cropped_2.png')

superpixels_cropping.plot_cropped_img_in_full_img(full_image, binary_images_otsu)