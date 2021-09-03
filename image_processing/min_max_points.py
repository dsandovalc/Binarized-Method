import numpy as np
import cv2

def critic_points(image_path, bilateralFilter_d=13, bilateralFilter_sigmaColor=35, bilateralFilter_sigmaSpace=10, Canny_thresh1=70, Canny_thresh2=200):
    colors = [(0, 0, 255), (0, 43, 255), (0, 85, 255), (0, 128, 255), (0, 170, 255), (0, 213, 255), (0, 255, 255), (0, 255, 212), (0, 255, 170), (0, 255, 127), (0, 255, 85), (0, 255, 42), (0, 255, 0), (43, 255, 0), (85, 255, 0), (128, 255, 0), (170, 255, 0), (213, 255, 0), (255, 255, 0), (255, 212, 0), (255, 170, 0), (255, 127, 0), (255, 85, 0), (255, 42, 0), (255, 0, 0)]

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, bilateralFilter_d, bilateralFilter_sigmaColor, bilateralFilter_sigmaSpace)
    edged = cv2.Canny(blur, Canny_thresh1, Canny_thresh2)

    ret, labels = cv2.connectedComponents(edged)

    canvas = np.zeros_like(img, np.uint8)
    
    for i in range(1,ret):
        pts = labels == i
        canvas[pts] = colors[i%len(colors)]

    cv2.imshow("blur", blur)
    cv2.imshow("res", canvas)
    return cv2.waitKey()