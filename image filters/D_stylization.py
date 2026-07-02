import cv2
import numpy as np


def apply_pencil_sketch(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    inverted = np.invert(gray)

    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

    dodge_math = (gray.astype(np.float32) * 255.0) / (255.0 - blurred.astype(np.float32) + 1e-5)

    sketch = np.clip(dodge_math, 0, 255).astype(np.uint8)

    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)


def apply_watercolor(frame):
    color_flat = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)

    hsv = cv2.cvtColor(color_flat, cv2.COLOR_BGR2HSV)

    hsv[:, :, 1] = np.clip(hsv[:, :, 1].astype(np.float32) * 1.3, 0, 255).astype(np.uint8)

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)