# main.py

import sys
from screen_capture import ScreenCaptureApp
from tkinter import Tk, Label, Button

def specify_path(app):  # Принимаем переменную app в качестве аргумента
    app.show_save_path_dialog()

if __name__ == "__main__":
    app = ScreenCaptureApp()

    if len(sys.argv) == 1:
        # Create a main window with text
        root = Tk()
        root.title("wayscreen")
        
        # Set window dimensions
        root.geometry("250x180")

        # Disable resizing of the window
        root.resizable(False, False)

        # Label for title
        label = Label(root, text="Screen Capture App", font=("Arial", 14))
        label.pack()

        # Button to specify screenshot path
        path_button = Button(root, text="Specify Screenshot Path", command=lambda: specify_path(app))  # Передаем app в lambda функцию
        path_button.pack()

        # English description
        description_label = Label(root, text="Parameters:\n- full: Capture full screen\n- area: Capture a specific area\n\nExample:\n- wayscreen full\n- wayscreen area", justify="left", font=("Arial", 10))
        description_label.pack()

        root.mainloop()
    else:
        app.main()
