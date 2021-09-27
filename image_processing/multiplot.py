import cv2
import numpy as np
from seaborn import *
import matplotlib.pyplot as plt

def multiplot_from_path(rows, cols, images_path, plot_title, save_path, save_figure_name):
    for i, img in enumerate(images_path):
        x_ray = cv2.imread(img)
        plt.suptitle(plot_title)
        plt.subplot(rows, cols, i+1)
        plt.imshow(x_ray)
        plt.axis('off')
    return plt.savefig('{}/Figure_{}.png'.format(save_path,save_figure_name))

def multiplot_from_array(rows, cols, images_list, plot_titles_list, graph_titles_list, grid_color_list, x_ticks, x_labels, y_ticks, y_labels):
    i=0
    for i, img in enumerate(images_list):
        plt.subplot(rows, cols, i+1)
        plt.title(plot_titles_list[i])
        plt.grid(color=grid_color_list[i], ls='dotted')
        plt.xticks(x_ticks, x_labels)
        plt.yticks(y_ticks, y_labels)
        plt.imshow(img, cmap='gray')
        i = i + 1
    
    n=0
    for n, graph in enumerate(images_list):
        plt.subplot(rows, cols, i+n+1)
        plt.title(graph_titles_list[n])
        # plt.hist(graph.ravel(), 256, [0,256], histtype='bar', color=grid_color_list[n])
        histplot(graph.ravel(), kde=True, color=grid_color_list[n])
        # hist = cv2.calcHist([graph], [0], None, [256], [0,256])
        # plt.plot(hist, color=grid_color_list[n])
        n = n + 1
    
    return plt.tight_layout(), plt.show()