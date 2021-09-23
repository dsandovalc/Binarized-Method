import cv2
from numpy import *
from seaborn import *
from matplotlib.pyplot import *
from modify_histogram import regular_stretching
from multiplot import multiplot_from_array

original_image = cv2.imread('../db/output/raw_cropped/cropped_1.png')
image = cv2.imread('../db/output/blur_cropped/blur_cropped_1.png')

full_image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

normalized_image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=-1)
new_expansion = regular_stretching(full_image_gray)

img_row_sixe = new_expansion.shape[0]
img_column_sixe = new_expansion.shape[1]

print('\n')
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print(':: To cropped the image, choose the segmentation values ::')
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('\n')
rows, columns = int(input('Rows: ')), int(input('Columns: '))
print('\n')

cropped_row = round(img_row_sixe/rows)
cropped_column = round(img_column_sixe/columns)

check_row_operator = img_row_sixe-(cropped_row*rows) >= 0
check_column_operator = img_column_sixe-(cropped_column*columns) >= 0

if check_row_operator == False:
    cropped_row = round(img_row_sixe/rows) - 1
    print('... Resizing row to -> ', cropped_row)
elif check_column_operator == False:
    cropped_column = round(img_column_sixe/columns) - 1
    print('... Resizing column to -> ', cropped_column)

print('\n')
print('__===============================================__')
print('||  Global Mean  | (min, max) |  Global Std Dev  ||')
print('||---------------|------------|------------------||')
print(f'||{round(mean(new_expansion),3):^15}| ({new_expansion.min():>3},{new_expansion.max():>4}) |{round(std(new_expansion),3):^18}||')
print('^^===============================================^^')
print('\n')
print('_-----_----------_------------_----------_-----------_----------------_----------_---------_------------_')
print('|  n  | Position | (min, max) |   Mean   | Norm_Mean | Mean/Glob_Mean |  Std Dev | Norm_SD | SD/Glob_SD |')
print('|-----|----------|------------|----------|-----------|----------------|----------|---------|------------|')

n = 0
x, y = 0, 0
x_min, y_min = 0, 0
x_ticks, y_ticks = [], []
x_labels, y_labels = [], []
x_max_values, y_max_values = [], []

images_cropped = []
full_images_gray = []
for row in range(rows):
    for col in range(columns):
        n = n + 1
        x_max = ((col+1)*cropped_column)
        y_max = ((row+1)*cropped_row)

        img_cropped = new_expansion[y_min:y_max, x_min:x_max]
        cropped_expansion = regular_stretching(img_cropped)

        normalized_img = cv2.normalize(img_cropped, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=-1)
        
        print(f'|{n:^5}|  ({row:^1}, {col:^1})  | ({amin(cropped_expansion):>3},{amax(cropped_expansion):>4}) | {round(mean(cropped_expansion),3):^8} | {round(mean(normalized_img),3):^9} |{round(mean(cropped_expansion)/mean(new_expansion),5):^16}|{round(std(cropped_expansion),3):^10}|{round(std(normalized_img),3):^9}|{round(std(cropped_expansion)/std(new_expansion),3):^12}|')

        x_ticks.append(x_min)
        x_labels.append(col)
        x_max_values.append(x_max)

        y_ticks.append(y_min)
        y_labels.append(row)
        y_max_values.append(y_max)

        full_images_gray.append(full_image_gray)
        images_cropped.append(cropped_expansion)

        x_min = x_max
    x_min = 0
    y_min = y_max
print('^-----^----------^------------^----------^-----------^----------------^----------^---------^------------^')
print('\n')

val = 0
binarized_images = []
for val in range(0, n):
    if val == 0:
        figure(figsize=(9,6))
        new_expansion[y_ticks[val]:y_max_values[val],x_ticks[val]:x_max_values[val]] = images_cropped[val]
        full_image_gray[y_ticks[val]:y_max_values[val], x_ticks[val]:x_max_values[val]] = images_cropped[val]
        
        images_array = [original_image, new_expansion, images_cropped[val], full_image_gray]
        images_titles = ['Original', 'Blured Expansion', 'Position ({},{})'.format(y_labels[val], x_labels[val]), 'Binarized']
        grid_colors = ['royalblue', 'gold', 'seagreen', 'gray']
        
        multiplot_from_array(2, 4, images_array, images_titles, grid_colors, x_ticks, x_labels, y_ticks, y_labels)
    else:
        bin_val = int(input('... Input threshold value: -> '))
        
        _, binarized_img = cv2.threshold(images_cropped[val-1], bin_val, 256, cv2.THRESH_BINARY)
        
        binarized_images.append(binarized_img)
        
        figure(figsize=(9,6))
        new_expansion[y_ticks[val]:y_max_values[val],x_ticks[val]:x_max_values[val]] = images_cropped[val]
        full_image_gray[y_ticks[val-1]:y_max_values[val-1], x_ticks[val-1]:x_max_values[val-1]] = binarized_images[val-1]
        
        images_array = [original_image, new_expansion, images_cropped[val], full_image_gray]
        images_titles = ['Original', 'Blured Expansion', 'Position ({},{})'.format(y_labels[val], x_labels[val]), 'Binarized']
        grid_colors = ['royalblue', 'gold', 'seagreen', 'gray']
        
        multiplot_from_array(2, 4, images_array, images_titles, grid_colors, x_ticks, x_labels, y_ticks, y_labels)
        
        val = val + 1
        
        if val == n:
            val = val - 1
            
            bin_val = int(input('... Input threshold value: -> '))
            
            _, binarized_img = cv2.threshold(images_cropped[val], bin_val, 256, cv2.THRESH_BINARY)
            
            binarized_images.append(binarized_img)
            
            figure(figsize=(9,6))
            new_expansion[y_ticks[val]:y_max_values[val],x_ticks[val]:x_max_values[val]] = images_cropped[val]
            full_image_gray[y_ticks[val]:y_max_values[val], x_ticks[val]:x_max_values[val]] = binarized_images[val]
            
            images_array = [original_image, new_expansion, images_cropped[val], full_image_gray]
            images_titles = ['Original', 'Blured Expansion', 'Position ({},{})'.format(y_labels[val], x_labels[val]), 'Binarized']
            grid_colors = ['royalblue', 'gold', 'seagreen', 'gray']
            
            multiplot_from_array(2, 4, images_array, images_titles, grid_colors, x_ticks, x_labels, y_ticks, y_labels)
            print('\n')