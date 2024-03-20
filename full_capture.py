# full_capture.py

import pyscreenshot as ImageGrab
from tkinter import messagebox
from datetime import datetime
import os

class FullCapture:
    def __init__(self, save_path):
        self.save_path = save_path

    def grab_full_screen(self):
        if self.save_path:
            im = ImageGrab.grab()
            now = datetime.now()
            folder_name = now.strftime("%Y-%m")
            folder_path = os.path.join(self.save_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
            im.save(os.path.join(folder_path, file_name))
        else:
            messagebox.showerror("Error. Path not found", "Run the program with the 'path' parameter to specify the path. For example, 'program path'")
