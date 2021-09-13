import cv2
from numpy import *

image = cv2.imread('../db/output/blur_cropped/blur_cropped_1.png')

img_row_size = image.shape[0]
img_column_size = image.shape[1]

cv2.imshow('Original', image)

rows = 3
columns = 3

cropped_row = round(img_row_size/rows)
cropped_column = round(img_column_size/columns)

check_row_operator = img_row_size-(cropped_row*rows) >= 0
check_column_operator = img_column_size-(cropped_column*columns) >= 0

if check_row_operator == False:
    cropped_row = round(img_row_size/rows) - 1
    print('Row -> ', cropped_row)
elif check_column_operator == False:
    cropped_column = round(img_column_size/columns) - 1
    print('Column -> ', cropped_column)


i = 0
x_min, y_min = 0, 0

for col in range(columns):
    x_min = x_min + cropped_row*col
    y_min = (y_min + cropped_column) * (col % 2)
    for row in range(rows):
        x_max = x_min + cropped_row
        y_max = y_min + cropped_column
        print(row, col, x_min, x_max, y_min, y_max)
        # cv2.imshow('Cropped {}'.format(col+row), image[x_min:cropped_row*col, y_min:cropped_column*row])
    # x_min = x_min + cropped_row * (y_min % 2)
    # y_min = (y_min + cropped_column) * (n % 2)
    # x_max = x_min + cropped_row
    # y_max = y_min + cropped_column

    # print(x_min, x_max, y_min, y_max)
    # cv2.imshow('Cropped {}'.format(n+1), image[x_min:x_max, y_min:y_max])

# cv2.waitKey()
