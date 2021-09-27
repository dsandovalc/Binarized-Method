import glob
from numpy import *
from .fast_image_analysis import analize_image

def blur_images(blur_val, original_images_path, stretch_save_path, blur_save_path):
    images_path = glob.glob(original_images_path)
    raw_cropped_images = stack((images_path))
    
    for i, raw_cropped_img in enumerate(sorted(raw_cropped_images)):
        s = raw_cropped_img.split('/')
        analize_image(raw_cropped_img, '{}{}'.format(stretch_save_path,s[-1]), '{}{}_{}'.format(blur_save_path, blur_val, s[-1]), blur_val)
    return