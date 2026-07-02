import cv2
import numpy as np

def apply_pixel_art(frame, pixel_size=16):
    h, w = frame.shape[:2]
    low_res = cv2.resize(frame, (w // pixel_size, h // pixel_size), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(low_res, (w, h), interpolation=cv2.INTER_NEAREST)