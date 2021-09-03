import cv2
import glob
from numpy import *

def crop_images(input_img_path, output_img_path):
    path = glob.glob(input_img_path)
    images = stack((path))

    for i, img in enumerate(images):
        image = cv2.imread(img)
        select_roi = cv2.selectROI(image)
        cropped_img = image[int(select_roi[1]):int(select_roi[1]+select_roi[3]), int(select_roi[0]):int(select_roi[0]+select_roi[2])]
        cv2.imwrite('{}cropped_{}.png'.format(output_img_path,i+1), cropped_img)
    return print('Succesfully saved in: {}'.format(output_img_path))