import cv2
import glob
import argparse
from numpy import *
from skimage import segmentation
from image_processing import binarization, superpixels_cropping

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

superpixels_cropping.cropping(args['image'],'db/output/segmentation_cropped/img_with_mask/')

superpixels_cropping.remove_mask('db/output/segmentation_cropped/img_with_mask/*.png','db/output/segmentation_cropped/img_without_mask/')

segmentation_images = glob.glob('db/output/segmentation_cropped/img_without_mask/*.png')

for img in stack(segmentation_images):
    binarization.percent_binarization(image,0.5,'db/output/binary_cropped')
    binarization.percent_binarization(image,0.8,'db/output/binary_cropped')

superpixels_cropping.plot_cropped_img_in_full_img(image, )