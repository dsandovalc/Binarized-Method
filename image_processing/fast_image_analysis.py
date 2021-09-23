import cv2
from .modify_histogram import regular_stretching

def analize_image(img_path,path_to_save_stretch,path_to_save_blur):
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    stretch = regular_stretching(gray)
    blur = cv2.medianBlur(stretch, 9)
    cv2.imwrite(path_to_save_stretch, stretch)
    cv2.imwrite(path_to_save_blur, blur)

    # i = 0
    # for i in range(1,3):
    #     blur = cv2.medianBlur(stretch, 15)
    #     stretch = blur
    #     cv2.imwrite(path_to_save_blur, blur)
    #     i = i + 1
    
    return