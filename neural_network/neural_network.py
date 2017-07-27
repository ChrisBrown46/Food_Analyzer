import logging

from cv2 import cv2


logger = logging.getLogger('logger')


def image_to_numpy_bgr_array(image_path):
    return cv2.imread(image_path)


def image_to_numpy_rgb_array(image_path):
    image = image_to_numpy_bgr_array(image_path)
    b, g, r = cv2.split(image)
    return cv2.merge((r, g, b))
