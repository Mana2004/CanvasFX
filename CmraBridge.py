import cv2
import pyglet
from pyglet.window import key

# 1. Initialize Webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("\n Cannot access webcam.")
    exit()

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

success, test_frame = camera.read()
if not success:
    print("failed to send video data.")
    exit()

cam_height, cam_width, _ = test_frame.shape
print(f"\n CAMERA LINKED!")
print(f"True Hardware Resolution: {cam_width}x{cam_height}\n")

window = pyglet.window.Window(width=cam_width, height=cam_height, caption="Filter Engine - Milestone 1")
current_image = None


def update_frame(dt):
    global current_image
    success, frame = camera.read()

    if success:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        current_image = pyglet.image.ImageData(
            cam_width,
            cam_height,
            'RGB',
            frame.tobytes(),
            pitch=-cam_width * 3
        )


@window.event
def on_draw():
    window.clear()
    if current_image:
        current_image.blit(0, 0)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        print("Closing window cleanly...")
        camera.release()
        window.close()
        pyglet.app.exit()


@window.event
def on_close():
    camera.release()


pyglet.clock.schedule_interval(update_frame, 1.0 / 60.0)

if __name__ == "__main__":
    pyglet.app.run()