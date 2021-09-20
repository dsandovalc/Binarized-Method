from matplotlib import pyplot as plt
import numpy as np
import cv2

def percent_binarization(image,percent_val):
    hist, bins = np.histogram(image.ravel(), 256, [0, 256])

    if percent_val > 100:
        print('(Warning: The percentage (%) value must be <= 100)')
    elif percent_val < 1:
        p = percent_val
    else:
        p = percent_val/100

    percent = p * sum(hist)

    i = 1
    while i <= len(bins):
        bars_sum = sum(hist[0:i])
        if bars_sum >= percent:
            break
        i += 1
    
    _, binarized = cv2.threshold(image, i, 256, cv2.THRESH_BINARY)
    
    return i, percent_val, binarized