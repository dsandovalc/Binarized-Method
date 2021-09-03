import cv2
from numpy import *
import matplotlib.pyplot as plt

def image_contour():
    template_path = 'img/crop_test.jpg'
    _, thresh = cv2.threshold(blur, 128, 255, 0)
    cv2.imwrite('out/Thresh.png', thresh)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours_lenghts = [len(contour) for contour in contours]

    larger_contour_array = contours[contours_lenghts.index(max(contours_lenghts))]

    x, y = [], [] 

    for i, val in enumerate(larger_contour_array): 
        x.append(val[0][0])
        y.append(val[0][1])

    plt.plot(x, y)

    fx = list(diff(x))
    fy = list(diff(y))

    dx = list(diff(fx))
    dy = list(diff(fy))

    critical_values_x = [i for i, value_zero in enumerate(dx) if value_zero == 0.0]

    for i in critical_values_x:
        x_val = x[i]
        y_val = y[i]
        plt.scatter(x_val, y_val)

    h, w = larger_contour_array.shape[:2]
    moments = cv2.moments(thresh)

    x_m = moments['m10']/moments['m00']
    y_m = moments['m01']/moments['m00']

    plt.scatter(x_m, y_m)
    plt.annotate("Centroid", (x_m, y_m), xytext=(x_m, y_m-25), arrowprops = dict(arrowstyle="->"))

    plt.imshow(image[:, :, ::-1])

    plt.savefig('out/Result_plot.png')

    result = cv2.drawContours(gray, contours, -1, (0, 255, 0))

    cv2.imwrite('out/Result.png', result)

    return plt.show()
