import os
import sys
import threading
import time
import tkinter as tk
import tkinter as ttk
from tkinter import Label, messagebox, Button

from PIL import Image, ImageTk, ImageSequence

from dotenv import load_dotenv

load_dotenv()

POPUP_DURATION = int(os.getenv("POPUP_DURATION", 60))  # Ensure these are integers
POPUP_INTERVAL = int(os.getenv("POPUP_INTERVAL", 60))  # Ensure these are integers


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class RstEyeApp:
    def __init__(self, image_path, interval=POPUP_INTERVAL * 60, fullscreen=False):
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
            popup = tk.Toplevel(self.root)
            popup.title("Please Wait")

            # Set the popup window size and position it in the center
            popup_width = 350
            popup_height = 200
            screen_width = popup.winfo_screenwidth()
            screen_height = popup.winfo_screenheight()
            x = (screen_width / 2) - (popup_width / 2)
            y = (screen_height / 2) - (popup_height / 2)
            popup.geometry(f"{popup_width}x{popup_height}+{int(x)}+{int(y)}")

            # Customize the popup window with a background image and better colors
            background_image = ImageTk.PhotoImage(
                Image.open(resource_path("rsteye.png")).resize(
                    (popup_width, popup_height)
                )
            )
            background_label = tk.Label(popup, image=background_image)
            background_label.place(relwidth=1, relheight=1)

            popup_label = Label(
                popup,
                text=f"An image is going to load in a few seconds... \n with breathing exercise for {POPUP_DURATION // 60} min\nPlease wait.",
                font=("Helvetica", 12, "bold"),
                wraplength=300,
            )
            popup_label.pack(pady=20)

            # Add buttons to the popup window
            button_frame = tk.Frame(popup)
            button_frame.pack(pady=10)

            def load_image():
                # Create the main window for the GIF
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
                        frame.copy().resize(
                            (screen_width, screen_height), Image.LANCZOS
                        )
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

                # Close the popup window after the GIF window is displayed
                popup.destroy()

                window.after(POPUP_DURATION * 1000, window.destroy)

            # Define button actions
            def on_accept():
                self.root.after(0, load_image)

            def on_exit():
                popup.destroy()

            # Create buttons without specifying foreground or background colors
            button_frame = tk.Frame(popup)
            button_frame.pack(pady=10)

            load_button = Button(
                button_frame,
                text="Yes",
                command=on_accept,
                font=("Helvetica", 12, "bold"),
                relief="flat",
            )
            load_button.pack(side="left", padx=20)

            exit_button = Button(
                button_frame,
                text="No",
                command=on_exit,
                font=("Helvetica", 12, "bold"),
                relief="flat",
            )
            exit_button.pack(side="right", padx=20)

            popup.mainloop()

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
