import argparse
from .superpixels_cropping import cropping

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

cropping(args['image'], 'db/output/segmentation_cropped/img_with_mask/', n_segments=9, sigma=200)
