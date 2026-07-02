import cv2
import numpy as np


def apply_warm(frame, intensity=30):
    res = frame.copy().astype(np.int16)
    res[:, :, 2] += intensity  # Red Channel
    res[:, :, 0] -= intensity  # Blue Channel
    return np.clip(res, 0, 255).astype(np.uint8)


def apply_cold(frame, intensity=30):
    res = frame.copy().astype(np.int16)
    res[:, :, 0] += intensity  # Blue Channel
    res[:, :, 2] -= intensity  # Red Channel
    return np.clip(res, 0, 255).astype(np.uint8)


def apply_cinematic_teal_orange(frame):
    lut_x = np.arange(256)

    lut_blue = np.clip(lut_x + (30 * np.sin(lut_x * np.pi / 255)), 0, 255).astype(np.uint8)
    lut_red = np.clip(lut_x - (30 * np.sin(lut_x * np.pi / 255)), 0, 255).astype(np.uint8)
    lut_green = lut_x.astype(np.uint8)

    lut = cv2.merge([lut_blue, lut_green, lut_red])
    return cv2.LUT(frame, lut)


def apply_black_and_white(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)