import cv2
import matplotlib.pyplot as plt

def multiplot(images_path, plot_title, save_path, save_figure_name):
    for i, img in enumerate(images_path):
        x_ray = cv2.imread(img)
        plt.suptitle(plot_title)
        plt.subplot(5, 6, i+1)
        plt.imshow(x_ray)
        plt.axis('off')
    return plt.savefig('{}/Figure_{}.png'.format(save_path,save_figure_name))