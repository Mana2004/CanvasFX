import cv2
import numpy as np


def apply_grain(frame, intensity=30):
    h, w, c = frame.shape
    noise = np.random.normal(0, intensity, (h, w, c))

    noisy_frame = frame.astype(np.float32) + noise
    return np.clip(noisy_frame, 0, 255).astype(np.uint8)


def apply_vhs_retro(frame):
    b, g, r = cv2.split(frame)
    r_shifted = np.roll(r, shift=8, axis=1)
    b_shifted = np.roll(b, shift=-8, axis=1)
    aberration = cv2.merge((b_shifted, g, r_shifted)).astype(np.float32)

    h, w, _ = frame.shape
    y_coords = np.arange(h)
    sine_wave = np.sin(y_coords * 2.0)
    scanline_matrix = ((sine_wave * 0.15) + 0.85).reshape(-1, 1)

    for i in range(3):
        aberration[:, :, i] *= scanline_matrix

    return np.clip(aberration, 0, 255).astype(np.uint8)