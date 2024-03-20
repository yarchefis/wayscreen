# area_capture.py

import pyscreenshot as ImageGrab
from tkinter import Tk, Canvas, filedialog, messagebox
from datetime import datetime
import os
import time

class AreaCapture:
    def __init__(self, save_path):
        self.save_path = save_path

    def on_click(self, event):
        self.x1 = event.x
        self.y1 = event.y

    def on_drag(self, event):
        self.x2, self.y2 = event.x, event.y
        self.canvas.coords(self.rect, self.x1, self.y1, self.x2, self.y2)

    def on_release(self, event):
        if self.save_path:
            self.root.destroy()
            time.sleep(0.5)  

            im = ImageGrab.grab(bbox=(self.x1, self.y1, self.x2, self.y2))
            now = datetime.now()
            folder_name = now.strftime("%Y-%m")
            folder_path = os.path.join(self.save_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
            im.save(os.path.join(folder_path, file_name))
        else:
            messagebox.showerror("Error. Path not found", "Run the program with the 'path' parameter to specify the path. For example, 'wayscreen path'")

    def run_area_capture(self):
        if self.save_path:
            self.root = Tk()
            self.root.attributes('-fullscreen', True)
            self.root.wait_visibility(self.root)
            self.root.wm_attributes('-alpha', 0.4)
            self.root.configure(bg='black')

            self.canvas = Canvas(self.root, bg='black', highlightthickness=0)
            self.canvas.pack(fill='both', expand=True)

            self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0

            self.canvas.bind("<Button-1>", self.on_click)
            self.canvas.bind("<B1-Motion>", self.on_drag)
            self.canvas.bind("<ButtonRelease-1>", self.on_release)

            self.rect = self.canvas.create_rectangle(0, 0, 0, 0, outline='red')

            self.root.mainloop()
        else:
            messagebox.showerror("Error. Path not found", "Run the program with the 'path' parameter to specify the path. For example, 'wayscreen path'")
