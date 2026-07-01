import cv2
import pyglet

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("\nCannot open camera")
else:
    print("\nSuccessfully connected to camera")

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

window = pyglet.window.Window(width=1280, height=720, caption="CmraBridge_Milestone1")

current_image = None

#real_time
def update_frame(dt):   #delta time
    global current_image
    #latest frame
    success, frme = camera.read()

    if success:
        frame = cv2.cvtColor(frme, cv2.COLOR_BGR2RGB)

        current_image = pyglet.image.ImageData(1280, 720, 'RGB', frame.tobytes(), pitch=-1280 * 3)

@window.event
def on_draw():
    window.clear()

    if current_image:
        current_image.blit(0, 0)

@window.event
def on_close():
    camera.release()

pyglet.clock.schedule_interval(update_frame, 1.0 / 60.0)

if __name__ == "__main__":
    pyglet.app.run()