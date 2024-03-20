# screen_capture_app.py

from tkinter import Tk, Canvas, filedialog, messagebox
from datetime import datetime
import os
import sys
import time
from full_capture import FullCapture
from area_capture import AreaCapture

class ScreenCaptureApp:
    def __init__(self):
        self.save_path = self.load_save_path()

    def load_save_path(self):
    try:
        with open(".config/wayscreen-setting.conf", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        # Create the .config directory if it doesn't exist
        os.makedirs(".config", exist_ok=True)
        return None
    except Exception as e:
        print(f"Error while loading save path: {e}")
        return None


    def save_save_path(self, save_path):
        with open(".config/wayscreen-setting.conf", "w") as f:
            f.write(save_path)

    def show_save_path_dialog(self):
        self.root = Tk()
        self.root.withdraw()  

        self.save_path = filedialog.askdirectory()
        if self.save_path:
            self.save_save_path(self.save_path)
            self.root.destroy()

    def main(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == "area":
                area_capture = AreaCapture(self.save_path)
                area_capture.run_area_capture()
            elif sys.argv[1] == "full":
                full_capture = FullCapture(self.save_path)
                full_capture.grab_full_screen()
            elif sys.argv[1] == "path":
                self.show_save_path_dialog()
            else:
                print("Invalid command line argument. Use 'area', 'full' or 'path'.")
        else:
            messagebox.showinfo("Settings", "Run the program with the 'path' parameter to specify the path. For example, 'wayscreen path'.")
