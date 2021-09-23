import cv2
from statistics import *
from scipy.signal import find_peaks

img = cv2.imread('../db/output/blur_cropped/blur_cropped_1.png')

def find_min_max(image):
    x_0, y_0 = [], [] 
    for i, val in enumerate(image): 
        x_0.append(i)
        y_0.append(val[0])

    hist_img = cv2.calcHist([image.ravel()], [0], None, [256], [0,256])
    
    # high_freq_fft = fftpack.fft(hist_img)
    # sample_freq = fftpack.fftfreq(hist_img.size)
    # pos_mask = where(sample_freq > 0)
    # freqs = sample_freq[pos_mask]
    # peak_freq = freqs[power([pos_mask], 3).argmax()]
    # high_freq_fft[abs(sample_freq) > peak_freq] = 0
    # filtered_sig = fftpack.ifft(high_freq_fft)
    # # plot(f)
    
    peaks, _ = find_peaks(y_0, height=0)

    return #plot(x_0, filtered_sig) #plot(hist_img, color=color_val)#, plot(peaks, hist_img[peaks], '.', color='green')
