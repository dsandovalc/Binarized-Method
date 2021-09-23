import glob
from numpy import *
from image_processing import fast_image_analysis

images_path = glob.glob('db/output/raw_cropped/*.png')
raw_cropped_images = stack((images_path))

for i, raw_cropped_img in enumerate(sorted(raw_cropped_images)):
    s = raw_cropped_img.split('/')
    fast_image_analysis.analize_image(raw_cropped_img, 'db/output/stretch_cropped/stretch_{}'.format(
        s[-1]), 'db/output/blur_cropped/blur_{}'.format(s[-1]))