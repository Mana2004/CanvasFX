import cv2


class CmraBridge:
    def __init__(self, source_type="webcam", path=0):
        self.source_type = source_type
        self.static_image = None

        if source_type == "webcam":
            self.cap = cv2.VideoCapture(path)
            if not self.cap.isOpened():
                raise RuntimeError(f"Source access failure for webcam index: {path}")

            success, test_frame = self.cap.read()
            if not success:
                raise RuntimeError("Empty stream package returned from webcam driver.")
            self.height, self.width = test_frame.shape[:2]

        elif source_type == "photo":
            # Load static image asset from disk
            self.static_image = cv2.imread(path)
            if self.static_image is None:
                raise RuntimeError(f"Disk read error at address: {path}")
            self.height, self.width = self.static_image.shape[:2]

    def get_frame(self):
        if self.source_type == "photo":
            return self.static_image.copy()

        success, frame = self.cap.read()
        if success:
            return frame
        return None

    def release(self):
        if self.source_type == "webcam" and hasattr(self, 'cap'):
            self.cap.release()