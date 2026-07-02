import tkinter as tk
from App import FXCanvas


def main():
    root = tk.Tk()

    app = FXCanvas(root, "Computer Vision & Mathematical Engine V2")

    root.mainloop()


if __name__ == "__main__":
    main()