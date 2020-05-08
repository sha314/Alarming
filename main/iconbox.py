from tkinter import Tk
import tkinter as tk
from PIL import Image, ImageTk


class IconBox:
    def __init__(self):
        self.ICON_PATHS = {
            "delete": r"../resources/icon/png/delete.png",
            "reset": r"../resources/icon/png/reset.png",
            "start": r"../resources/icon/png/start.png",
            "stop": r"../resources/icon/png/stop.png",
        }
        self.keys = list(self.ICON_PATHS.keys())
        pass

    def get_keys(self):
        return self.keys

    def get(self, key, width=20, height=20):
        img = Image.open(self.ICON_PATHS[key])
        img = img.resize((width, height), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(img)
        return photoImg


def main():
    root = Tk()

    root.geometry("400x400+300+300")
    # root.iconbitmap('../resources/png/icon.ico') # main icon
    # root.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png')) # or this

    iconbox = IconBox()
    icon = iconbox.get('delete')
    print(iconbox.get_keys())
    btn = tk.Button(root)
    btn['image'] = icon
    btn.pack()

    root.mainloop()

if __name__ == '__main__':
    main()