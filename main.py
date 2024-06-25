from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from ChatBot import ChatBot

# from main import Face_Recognition_System


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")

        # First image
        img = Image.open(r"college_images\Face.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photo_img = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photo_img)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"college_images\Face_1.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photo_img1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"college_images\Face_2.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photo_img2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photo_img2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image
        img3 = Image.open(r"college_images\Face_2.png")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photo_img3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photo_img3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # title section
        title_lb1 = Label(
            bg_img,
            text="VKU - Hệ thống điểm danh nhận dạng khuôn mặt",
            font=("verdana", 20, "bold"),
            bg="navyblue",
            fg="white",
        )
        title_lb1.place(x=0, y=0, width=1380, height=40)

        # Student button
        img4 = Image.open(r"college_images\Students.png")
        img4 = img4.resize((180, 180), Image.ANTIALIAS)
        self.photo_img4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img,
            image=self.photo_img4,
            command=self.student_details,
            cursor="hand2",
            bd=5,
        )
        b1.place(x=220, y=70, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Sinh Viên",
            command=self.student_details,
            cursor="hand2",
            font=("tohoma", 15, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
        )
        b1_1.place(x=220, y=220, width=180, height=40)

        # Detect face button
        img5 = Image.open(r"college_images\Detect_Face.png")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photo_img5 = ImageTk.PhotoImage(img5)

        b1 = Button(
            bg_img, command=self.face_data, image=self.photo_img5, cursor="hand2", bd=5
        )
        b1.place(x=450, y=70, width=180, height=180)

        b1_1 = Button(
            bg_img,
            command=self.face_data,
            text="Nhận Diện",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
        )
        b1_1.place(x=450, y=220, width=180, height=40)

        # Attendance face button
        img6 = Image.open(r"college_images\Attendance_Face.png")
        img6 = img6.resize((180, 180), Image.ANTIALIAS)
        self.photo_img6 = ImageTk.PhotoImage(img6)

        b1 = Button(
            bg_img,
            image=self.photo_img6,
            command=self.attendance_data,
            cursor="hand2",
            bd=5,
        )
        b1.place(x=680, y=70, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Điểm Danh",
            command=self.attendance_data,
            cursor="hand2",
            font=("tahoma", 15, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
        )
        b1_1.place(x=680, y=220, width=180, height=40)

        # Help desk button
        img7 = Image.open(r"college_images\Help.png")
        img7 = img7.resize((180, 180), Image.ANTIALIAS)
        self.photo_img7 = ImageTk.PhotoImage(img7)

        b1 = Button(
            bg_img,
            command=self.ChatBot_data,
            image=self.photo_img7,
            cursor="hand2",
            bd=5,
        )
        b1.place(x=910, y=70, width=180, height=180)

        b1_1 = Button(
            bg_img,
            command=self.help_data,
            text="Hỗ Trợ",
            cursor="hand2",
            font=("tahoma", 15, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
        )
        b1_1.place(x=910, y=220, width=180, height=40)

        # Top 4 buttons end..........
        # ----------------------------------------------------------------------------------------------------
        # Start below buttons.........
        # Train data button
        img8 = Image.open(r"college_images\train_data.png")
        img8 = img8.resize((180, 180), Image.ANTIALIAS)
        self.photo_img8 = ImageTk.PhotoImage(img8)

        b1 = Button(
            bg_img, image=self.photo_img8, cursor="hand2", command=self.train_data, bd=5
        )
        b1.place(x=220, y=270, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Train Data",
            cursor="hand2",
            command=self.train_data,
            font=("tahoma", 13, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
        )
        b1_1.place(x=220, y=420, width=180, height=40)

        # Photos button
        img9 = Image.open(r"college_images\photos.png")
        img9 = img9.resize((180, 180), Image.ANTIALIAS)
        self.photo_img9 = ImageTk.PhotoImage(img9)

        b1 = Button(
            bg_img, image=self.photo_img9, cursor="hand2", command=self.open_img, bd=5
        )
        b1.place(x=450, y=270, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Bộ Dữ liệu",
            cursor="hand2",
            command=self.open_img,
            font=("tahoma", 15, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
        )
        b1_1.place(x=450, y=420, width=180, height=40)

        # Developer button
        img10 = Image.open(r"college_images\Developer.png")
        img10 = img10.resize((180, 180), Image.ANTIALIAS)
        self.photo_img10 = ImageTk.PhotoImage(img10)

        b1 = Button(
            bg_img,
            command=self.developer_data,
            image=self.photo_img10,
            cursor="hand2",
            bd=5,
        )
        b1.place(x=680, y=270, width=180, height=180)

        b1_1 = Button(
            bg_img,
            command=self.developer_data,
            text="Nhà phát triển",
            cursor="hand2",
            font=("tahoma", 15, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
        )
        b1_1.place(x=680, y=420, width=180, height=40)

        # Exit button
        img11 = Image.open(r"college_images\exit.png")
        img11 = img11.resize((180, 180), Image.ANTIALIAS)
        self.photo_img11 = ImageTk.PhotoImage(img11)

        b1 = Button(
            bg_img, command=self.iExit, image=self.photo_img11, cursor="hand2", bd=5
        )
        b1.place(x=910, y=270, width=180, height=180)

        b1_1 = Button(
            bg_img,
            command=self.iExit,
            text="Đăng xuất",
            cursor="hand2",
            font=("tahoma", 15, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
        )
        b1_1.place(x=910, y=420, width=180, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure exit", parent=self.root
        )
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

        # --------------Functions buttons-----------------

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def ChatBot_data(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
