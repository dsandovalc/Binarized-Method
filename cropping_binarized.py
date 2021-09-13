import glob
import cv2
from numpy import *
from image_processing import binarization

segmentation_images = glob.glob('db/output/segmentation_cropped/img_without_mask/*.png')
superpixels_images = stack((segmentation_images))

for i, img in enumerate(segmentation_images):
    s = img.split('/')
    binarization.percent_binarization(img,0.4,'db/output/segmentation_cropped/binary_cropped/40_{}'.format(s[-1]))
    binarization.percent_binarization(img,0.8,'db/output/segmentation_cropped/binary_cropped/80_{}'.format(s[-1]))
    
    img = cv2.imread(img,0)
    _, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite('db/output/segmentation_cropped/binary_cropped/otsu_{}'.format(s[-1]), otsu)