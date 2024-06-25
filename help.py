from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk, messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")

        img_top = Image.open(r"college_images\developer_bg.png")
        img_top = img_top.resize((1380, 920), Image.ANTIALIAS)
        self.photo_img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photo_img_top)
        f_lbl.place(x=0, y=0, width=1380, height=820)

        # title section
        title_lbl = Label(
            self.root,
            text="Hỗ Trợ",
            font=("verdana", 20, "bold"),
            bg="navyblue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1380, height=45)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
