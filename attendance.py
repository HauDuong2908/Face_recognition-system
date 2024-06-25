from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk, messagebox
import mysql.connector
import cv2
import codecs
import os
import csv
from tkinter import filedialog

myData = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")

        # -------------- Variables -------------
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_day = StringVar()
        self.var_attend_attendance = StringVar()

        # First image
        img = Image.open(
            r"C:\Học để thành công\Face_recognition system\college_images\Student\Fisrt_std.png"
        )
        img = img.resize((495, 130), Image.ANTIALIAS)
        self.photo_img = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photo_img)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(
            r"C:\Học để thành công\Face_recognition system\college_images\Student\second_std.png"
        )
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photo_img1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(
            r"C:\Học để thành công\Face_recognition system\college_images\Student\third_std.png"
        )
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photo_img2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photo_img2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image
        img3 = Image.open(
            r"C:\Học để thành công\Face_recognition system\college_images\Face_2.png"
        )
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photo_img3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photo_img3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="Student management system",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg="blue",
        )
        title_lbl.place(x=0, y=0, width=1450, height=35)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=45, width=1350, height=520)

        # Left label frame
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Thông tin sinh viên",
            font=("times new roman", 12, "bold"),
        )
        left_frame.place(x=10, y=10, width=660, height=495)

        img_left = Image.open(
            r"C:\Học để thành công\Face_recognition system\college_images\bg_left_student.png"
        )
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photo_img_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photo_img_left)
        f_lbl.place(x=5, y=0, width=648, height=130)

        left_inside_frame = Frame(bg_img, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=28, y=210, width=650, height=330)

        # Labe land entry
        # Student id
        attendanceId_label = Label(
            left_inside_frame,
            text="ID Sinh Viên:",
            font=("verdana", 12, "bold"),
            fg="navyblue",
            bg="white",
        )
        attendanceId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_attend_id,
            width=15,
            font=("verdana", 12, "bold"),
        )
        attendanceId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Student Roll
        student_roll_label = Label(
            left_inside_frame,
            text="Mã Sinh Viên:",
            font=("verdana", 12, "bold"),
            fg="navyblue",
            bg="white",
        )
        student_roll_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        student_roll_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_attend_roll,
            width=15,
            font=("verdana", 12, "bold"),
        )
        student_roll_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Studnet Name
        student_name_label = Label(
            left_inside_frame,
            text="Tên Sinh Viên:",
            font=("verdana", 12, "bold"),
            fg="navyblue",
            bg="white",
        )
        student_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        student_name_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_attend_name,
            width=15,
            font=("verdana", 12, "bold"),
        )
        student_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Department
        dep_label = Label(
            left_inside_frame,
            text="Department:",
            font=("verdana", 12, "bold"),
            fg="navyblue",
            bg="white",
        )
        dep_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        dep_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_attend_dep,
            width=15,
            font=("verdana", 12, "bold"),
        )
        dep_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # time
        time_label = Label(
            left_inside_frame,
            text="Giờ:",
            font=("verdana", 12, "bold"),
            fg="navyblue",
            bg="white",
        )
        time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        time_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_attend_time,
            width=15,
            font=("verdana", 12, "bold"),
        )
        time_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Date
        date_label = Label(
            left_inside_frame,
            text="Ngày:",
            font=("verdana", 12, "bold"),
            fg="navyblue",
            bg="white",
        )
        date_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        date_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_attend_day,
            width=15,
            font=("verdana", 12, "bold"),
        )
        date_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Attendance
        student_attend_label = Label(
            left_inside_frame,
            text="Trạng thái:",
            font=("verdana", 12, "bold"),
            fg="navyblue",
            bg="white",
        )
        student_attend_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        attend_combo = ttk.Combobox(
            left_inside_frame,
            textvariable=self.var_attend_attendance,
            width=13,
            font=("verdana", 12, "bold"),
            state="readonly",
        )
        attend_combo["values"] = ("Có mặt", "Vắng mặt")
        attend_combo.current(0)
        attend_combo.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=190, width=645, height=30)

        save_btn = Button(
            btn_frame,
            text="import CSV",
            command=self.importCsv,
            width=17,
            font=("times new roman", 11, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            text="Export CSV",
            command=self.exportCSV,
            width=17,
            font=("times new roman", 11, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            width=17,
            font=("times new roman", 11, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            command=self.reset_data,
            text="Reset",
            width=17,
            font=("times new roman", 11, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        # Right label frame
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        right_frame.place(x=680, y=10, width=660, height=495)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=650, height=460)

        # ------------------scroll bar table --------------------------

        scoll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scoll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=("id", "roll", "name", "department", "time", "date", "attendance"),
            xscrollcommand=scoll_x.set,
            yscrollcommand=scoll_y.set,
        )

        scoll_x.pack(side=BOTTOM, fill=X)
        scoll_y.pack(side=RIGHT, fill=Y)

        scoll_x.config(command=self.AttendanceReportTable.xview)
        scoll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ==============Fetch Data ======================

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # import CSV
    def importCsv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*csv"), ("All File", "*,*")),
            parent=self.root,
        )
        with codecs.open(fln, "r", encoding="utf-8-sig") as myfile:
            csvRead = csv.reader(myfile, delimiter=",")
            for i in csvRead:
                myData.append(i)
            self.fetchData(myData)

    # Export CSV
    def exportCSV(self):
        try:
            if len(myData) < 1:
                messagebox.showerror(
                    "No Data", "No data found to export", parent=self.root
                )
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV File", "*csv"), ("All File", "*,*")),
                parent=self.root,
            )
            with open(fln, mode="w", newline="", encoding="utf-8-sig") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export",
                    "Your data exported to" + os.path.basename(fln) + ("Successfully"),
                )
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_day.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_day.set("")
        self.var_attend_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
