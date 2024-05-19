import os
import sys
import threading
import time
import tkinter as tk
from tkinter import Label, messagebox

from PIL import Image, ImageTk, ImageSequence

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class RstEyeApp:
    def __init__(self, image_path, interval=1800, fullscreen=False):
        self.image_path = resource_path(image_path)
        self.interval = interval  
        self.fullscreen = fullscreen
        self.root = tk.Tk()
        self.root.withdraw()  

        if not os.path.exists(self.image_path):
            messagebox.showerror("Error", f"Image file '{self.image_path}' not found.")
            self.root.destroy()
            return

    def show_image(self):
        try:
            window = tk.Toplevel(self.root)
            window.withdraw()
            window.title("Take a Break")

            if self.fullscreen:
                window.attributes("-fullscreen", True)

            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            img = Image.open(self.image_path)

            frames = [
                ImageTk.PhotoImage(
                    frame.copy().resize((screen_width, screen_height), Image.LANCZOS)
                )
                for frame in ImageSequence.Iterator(img)
            ]

            label = Label(window)
            label.pack()

            def update_frame(frame_index):
                frame = frames[frame_index]
                label.configure(image=frame)
                frame_index = (frame_index + 1) % len(frames)
                window.after(50, update_frame, frame_index)

            window.after(0, update_frame, 0)
            window.deiconify()
            window.after(60000, window.destroy)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def start_popup(self):
        while True:
            time.sleep(self.interval)
            self.root.after(0, self.show_image)

    def start(self):
        self.root.after(0, self.show_image)
        threading.Thread(target=self.start_popup, daemon=True).start()
        self.root.mainloop()

if __name__ == "__main__":
    image_path = "med.gif"  
    app = RstEyeApp(image_path, fullscreen=True) 
    app.start()
