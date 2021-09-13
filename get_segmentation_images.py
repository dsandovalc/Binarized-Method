import argparse
from image_processing import superpixels_cropping

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

superpixels_cropping.cropping(args['image'], 'db/output/segmentation_cropped/img_with_mask/', n_segments=9, sigma=200)
