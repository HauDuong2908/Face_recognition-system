from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk, messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")

        img_top = Image.open(r"college_images\developer_bg.png")
        img_top = img_top.resize((1380, 920), Image.ANTIALIAS)
        self.photo_img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photo_img_top)
        f_lbl.place(x=0, y=0, width=1380, height=820)

        # # backgorund image
        # bg1 = Image.open(r"college_images\developer_bg.png")
        # bg1 = bg1.resize((1380, 600), Image.ANTIALIAS)
        # self.photo_img_top1 = ImageTk.PhotoImage(bg1)

        # # set image as lable
        # bg_img = Label(self.root, image=self.photo_img_top1)
        # bg_img.place(x=220, y=55, width=1000, height=600)

        # title section
        title_lbl = Label(
            self.root,
            text="VKU - Thông tin nhà phát triển",
            font=("verdana", 20, "bold"),
            bg="navyblue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1380, height=45)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------

        att_img_btn = Image.open(r"college_images\Admin.jpg")
        att_img_btn = att_img_btn.resize((200, 200), Image.ANTIALIAS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(
            f_lbl,
            image=self.att_img1,
            cursor="hand2",
        )
        att_b1.place(x=350, y=120, width=250, height=250)

        att_b1_1 = Button(
            f_lbl,
            text="Dương Phúc Hậu",
            cursor="hand2",
            font=("tahoma", 10, "bold"),
            bg="white",
            fg="navyblue",
        )
        att_b1_1.place(x=350, y=370, width=250, height=50)

        # Creating Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")  # bd mean border
        main_frame.place(x=600, y=120, width=400, height=300)
        # Right Label Frame
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Thông tin nhà phát triển",
            font=("verdana", 10, "bold"),
            fg="navyblue",
        )
        right_frame.place(x=7, y=7, width=380, height=280)

        # label Name
        name_label = Label(
            right_frame,
            text="Họ tên:",
            font=("verdana", 12, "bold"),
            bg="white",
            fg="navyblue",
        )
        name_label.grid(row=0, column=0, padx=5, pady=12)
        # Name
        name = Label(
            right_frame, text="Dương Phúc Hậu", font=("verdana", 12), bg="white"
        )
        name.grid(row=0, column=1, padx=5, pady=12, sticky=W)

        # label ID
        idstd_label = Label(
            right_frame,
            text="Mã Sinh viên:",
            font=("verdana", 12, "bold"),
            bg="white",
            fg="navyblue",
        )
        idstd_label.grid(row=1, column=0, padx=5, pady=12)
        # ID
        idstd = Label(right_frame, text="20IT046", font=("verdana", 12), bg="white")
        idstd.grid(row=1, column=1, padx=5, pady=12, sticky=W)

        # label class
        classStd_label = Label(
            right_frame,
            text="Lớp sinh hoạt:",
            font=("verdana", 12, "bold"),
            bg="white",
            fg="navyblue",
        )
        classStd_label.grid(row=2, column=0, padx=5, pady=12)
        # class
        classStd = Label(right_frame, text="20AD", font=("verdana", 12), bg="white")
        classStd.grid(row=2, column=1, padx=5, pady=12, sticky=W)

        # label phone
        phone_label = Label(
            right_frame,
            text="Di động:",
            font=("verdana", 12, "bold"),
            bg="white",
            fg="navyblue",
        )
        phone_label.grid(row=3, column=0, padx=5, pady=12)
        # phone
        phone = Label(
            right_frame, text="0979.548.446", font=("verdana", 12), bg="white"
        )
        phone.grid(row=3, column=1, padx=5, pady=12, sticky=W)

        # label email
        email_label = Label(
            right_frame,
            text="Email:",
            font=("verdana", 12, "bold"),
            bg="white",
            fg="navyblue",
        )
        email_label.grid(row=4, column=0, padx=5, pady=12)
        # email
        email = Label(
            right_frame, text="dphau.20it2@vku.udn.vn", font=("verdana", 12), bg="white"
        )
        email.grid(row=4, column=1, padx=5, pady=12, sticky=W)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
