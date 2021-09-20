import cv2
from matplotlib.pyplot import *
from numpy import *
from binarization import percent_binarization
from modify_histogram import regular_stretching

original_image = cv2.imread('../db/output/raw_cropped/cropped_1.png')
image = cv2.imread('../db/output/blur_cropped/blur_cropped_1.png')
full_image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


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
print('_-----_----------_------------_----------_-----------_----------------_----------_---------_------------_-------------_')
print('|  n  | Position | (min, max) |   Mean   | Norm_Mean | Mean/Glob_Mean |  Std Dev | Norm_SD | SD/Glob_SD |  Threshold  |')
print('|-----|----------|------------|----------|-----------|----------------|----------|---------|------------|-------------|')

n = 0
x, y = 0, 0
x_min, y_min = 0, 0
x_ticks, y_ticks = [], []
x_labels, y_labels = [], []
for row in range(rows):
    for col in range(columns):
        n = n + 1
        x_max = ((col+1)*cropped_column)
        y_max = ((row+1)*cropped_row)
        
        img_cropped = new_expansion[y_min:y_max, x_min:x_max]
        
        normalized_img = cv2.normalize(img_cropped, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=-1)
        
        if mean(img_cropped)/mean(new_expansion) < 1.2:
            binarized_val, percent_val, binarized_img = percent_binarization(img_cropped, 0.80)
        elif mean(img_cropped)/mean(new_expansion) > 1.2:
            binarized_val, percent_val, binarized_img = percent_binarization(img_cropped, 0.50)
        else:
            binarized_val, percent_val, binarized_img = percent_binarization(img_cropped, 0.25)
        
        print(f'|{n:^5}|  ({row:^1}, {col:^1})  | ({amin(img_cropped):>3},{amax(img_cropped):>4}) | {round(mean(img_cropped),3):^8} | {round(mean(normalized_img),3):^9} |{round(mean(img_cropped)/mean(new_expansion),5):^16}|{round(std(img_cropped),3):^10}|{round(std(normalized_img),3):^9}|{round(std(img_cropped)/std(new_expansion),3):^12}| {round(percent_val*100)} % -> {binarized_val:>3} |')
        
        full_image_gray[y_min:y_max, x_min:x_max] = binarized_img
        subplot(2, 5, 5)
        title('Binarized')
        imshow(full_image_gray, cmap='gray')
        grid(ls='dotted')
        
        x_ticks.append(x_min)
        x_labels.append(col)
        
        y_ticks.append(y_min)
        y_labels.append(row)
        
        xticks(x_ticks,x_labels)
        yticks(y_ticks,y_labels)
        
        x_min = x_max
    x_min = 0
    y_min = y_max
print('^-----^----------^------------^----------^-----------^----------------^----------^---------^------------^-------------^')
print('\n')

subplot(2, 5, 3)
title('New Expansion')
imshow(new_expansion, cmap='gray')
grid(color='green', ls='solid')
xticks(x_ticks,x_labels)
yticks(y_ticks,y_labels)

subplot(2, 5, 2)
title('Blured Expansion')
imshow(image, cmap='gray')
grid(color='yellow', ls='dotted')
xticks(x_ticks,x_labels)
yticks(y_ticks,y_labels)

subplot(2, 5, 1)
title('Original')
imshow(original_image, cmap='gray')
grid(color='blue', ls='dotted')
xticks(x_ticks,x_labels)
yticks(y_ticks,y_labels)

subplot(2, 5, 4)
title('Normalized')
imshow(normalized_image, cmap='gray')
grid(color='purple', ls='dotted')
xticks(x_ticks,x_labels)
yticks(y_ticks,y_labels)


original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
normalized_image = cv2.cvtColor(normalized_image, cv2.COLOR_BGR2GRAY)

subplot(2, 5, 6)
hist(original_image.ravel(), 256, [0,256], color='b', histtype='stepfilled')
xlim([0,256])
ylim([0,850])

subplot(2, 5, 7)
hist(image.ravel(), 256, [0,256], color='y', histtype='stepfilled')
xlim([0,256])
ylim([0,850])

subplot(2, 5, 8)
hist(new_expansion.ravel(), 256, [0,256], color='g', histtype='stepfilled')
xlim([0,256])
ylim([0,850])

subplot(2, 5, 9)
hist(normalized_image.ravel(), 256, [0,256], color='purple', histtype='stepfilled')
xlim([0,256])
ylim([0,850])

subplot(2, 5, 10)
hist(new_expansion.ravel(), 256, [0,256], color='g', histtype='step')
hist(image.ravel(), 256, [0,256], color='y', histtype='step')
hist(original_image.ravel(), 256, [0,256], color='b', histtype='step')
hist(full_image_gray.ravel(), 256, [0,256], color='k', histtype='step')
xlim([0,256])
ylim([0,850])

show()