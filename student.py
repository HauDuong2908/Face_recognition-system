from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk, messagebox
import mysql.connector
import cv2
import mysql.connector.locales.eng.client_error


class Student:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")
        # self.root = Tk()

        # ---------------------Variable-----------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_div = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # First image
        img = Image.open(
            r"C:\Học để thành công\Face_recognition system\college_images\banner2.png"
        )
        img = img.resize((1380, 130), Image.ANTIALIAS)
        self.photo_img = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photo_img)
        f_lbl.place(x=0, y=0, width=1380, height=130)

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
            text="VKU - Quản lí thông tin sinh viên",
            font=("verdana", 20, "bold"),
            bg="navyblue",
            fg="white",
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
            font=("verdana", 10, "bold"),
            fg="navyblue",
        )
        left_frame.place(x=7, y=7, width=640, height=480)

        # img_left = Image.open(
        #     r"C:\Học để thành công\Face_recognition system\college_images\bg_left_student.png"
        # )
        # img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        # self.photo_img_left = ImageTk.PhotoImage(img_left)

        # f_lbl = Label(left_frame, image=self.photo_img_left)
        # f_lbl.place(x=5, y=0, width=648, height=130)

        # Current Course information
        current_course_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Thông tin khóa học",
            font=("verdana", 10, "bold"),
            fg="navyblue",
        )
        current_course_frame.place(x=10, y=5, width=620, height=120)

        # Department
        dep_label = Label(
            current_course_frame,
            text="Khoa",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_dep,
            font=("times new roman", 12, "bold"),
            state="readonly",
            width=20,
        )
        dep_combo["values"] = (
            "Chọn khoa",
            "khoa học máy tính",
            "khoa kỹ thuật máy tính",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(
            current_course_frame,
            text="Lớp HP",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        course_label.grid(row=0, column=2, padx=10)

        course_label = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_course,
            font=("times new roman", 11, "bold"),
            state="readonly",
            width=20,
        )
        course_label["values"] = ("Chọn học kỳ", "AD", "DA", "CE", "AB", "SE1", "SE2")
        course_label.current(0)
        course_label.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(
            current_course_frame,
            text="Năm Học",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        year_label.grid(row=1, column=0, padx=10)

        year_label = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_year,
            font=("times new roman", 11, "bold"),
            state="readonly",
            width=20,
        )
        year_label["values"] = (
            "Chọn năm học",
            "2020-2025",
            "2021-2026",
            "2022-2027",
            "2023-2028",
        )
        year_label.current(0)
        year_label.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(
            current_course_frame,
            text="Học Kỳ",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=10)

        semester_label = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_semester,
            font=("times new roman", 11, "bold"),
            state="readonly",
            width=20,
        )
        semester_label["values"] = ("Chọn học kỳ", "I", "II")
        semester_label.current(0)
        semester_label.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student information
        class_student_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Thông tin lớp học",
            font=("verdana", 10, "bold"),
            fg="navyblue",
        )
        class_student_frame.place(x=10, y=130, width=620, height=220)

        # Student ID
        studentId_label = Label(
            class_student_frame,
            text="Mã sinh viên:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_id,
            width=18,
            font=("times new roman", 11, "bold"),
        )
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student name
        studentName_label = Label(
            class_student_frame,
            text="Họ và tên:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_name,
            width=18,
            font=("times new roman", 11, "bold"),
        )
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class division
        class_div_label = Label(
            class_student_frame,
            text="Ngành học:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_div,
            width=16,
            state="readonly",
            font=("times new roman", 11, "bold"),
        )

        class_div_combo["value"] = (
            "Chọn ngành học",
            "Trí tuệ nhân tạo",
            "Mỹ thuật số",
            "Kỹ sư phần mềm",
            "Kỹ thuật máy tính",
            "Truyền thông đa phương tiện",
            "Lập trình nhúng",
        )
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # roll no
        roll_no_label = Label(
            class_student_frame,
            text="Roll no:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_roll,
            width=18,
            font=("times new roman", 11, "bold"),
        )
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(
            class_student_frame,
            text="Giới Tính:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_label = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_gender,
            font=("times new roman", 11, "bold"),
            state="readonly",
            width=16,
        )
        gender_label["values"] = ("Chọn giới tính", "Nam", "Nữ")
        gender_label.current(0)
        gender_label.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Roll no
        dob_label = Label(
            class_student_frame,
            text="Ngày Sinh:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_dob,
            width=18,
            font=("times new roman", 11, "bold"),
        )
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(
            class_student_frame,
            text="Email:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_email,
            width=18,
            font=("times new roman", 11, "bold"),
        )
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no
        phone_label = Label(
            class_student_frame,
            text="Số điện thoại:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_phone,
            width=18,
            font=("times new roman", 11, "bold"),
        )
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(
            class_student_frame,
            text="Địa chỉ:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_address,
            width=18,
            font=("times new roman", 11, "bold"),
        )
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        teacher_label = Label(
            class_student_frame,
            text="Giảng Viên:",
            font=("times new roman", 11, "bold"),
            bg="white",
        )
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_teacher,
            width=18,
            font=("times new roman", 11, "bold"),
        )
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        # radio Buttons
        self.var_radio1 = StringVar()
        radio_bt1 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Quét khuôn mặt",
            value="Có",
        )
        radio_bt1.grid(row=6, column=0)

        radio_bt2 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Không quét khuôn mặt ",
            value="Không",
        )
        radio_bt2.grid(row=6, column=1)

        # buttons frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=370, width=620, height=60)

        save_btn = Button(
            btn_frame,
            text="Lưu",
            command=self.add_data,
            width=9,
            font=("verdana", 10, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0, padx=7, pady=10, sticky=W)

        update_btn = Button(
            btn_frame,
            text="Cập nhập",
            command=self.update_data,
            width=9,
            font=("verdana", 10, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1, padx=7, pady=8, sticky=W)

        delete_btn = Button(
            btn_frame,
            text="Xóa",
            command=self.delete_data,
            width=9,
            font=("verdana", 10, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2, padx=7, pady=10, sticky=W)

        # Reset Information for students

        reset_btn = Button(
            btn_frame,
            text="Đặt lại",
            command=self.reset_data,
            width=9,
            font=("verdana", 10, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3, padx=7, pady=10, sticky=W)

        # Add Image

        take_photo_btn = Button(
            btn_frame,
            text="Lấy ảnh",
            command=self.generate_dataset,
            width=9,
            font=("verdana", 10, "bold"),
            bg="blue",
            fg="white",
        )
        take_photo_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        # Update image

        update_photo_btn = Button(
            btn_frame,
            text="Sửa ảnh",
            width=7,
            font=("verdana", 10, "bold"),
            bg="blue",
            fg="white",
        )
        update_photo_btn.grid(row=0, column=5, padx=5, pady=10, sticky=W)

        # --------------------------------------------------------------------------------------------------------------

        # Right label frame
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Danh sách",
            font=("verdana", 10, "bold"),
            fg="navyblue",
        )
        right_frame.place(x=650, y=8, width=680, height=480)

        # img_right = Image.open(
        #     r"C:\Học để thành công\Face_recognition system\college_images\bg_left_student.png"
        # )
        # img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        # self.photo_img_right = ImageTk.PhotoImage(img_right)

        # f_lbl = Label(right_frame, image=self.photo_img_right)
        # f_lbl.place(x=5, y=0, width=648, height=81)

        # =========Search System==============
        # Searching System in Right Label Frame
        search_frame = LabelFrame(
            right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Hệ thống tìm kiếm",
            font=("verdana", 10, "bold"),
            fg="navyblue",
        )
        search_frame.place(x=10, y=8, width=648, height=70)
        # Phone Number
        search_label = Label(
            search_frame,
            text="Tìm kiếm theo:",
            font=("verdana", 10, "bold"),
            fg="navyblue",
            bg="white",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.var_searchTX = StringVar()
        # combo box
        search_combo = ttk.Combobox(
            search_frame,
            textvariable=self.var_searchTX,
            width=12,
            font=("verdana", 10, "bold"),
            state="readonly",
        )
        search_combo["values"] = ("Chọn", "Mã-Sinh-Viên", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.var_search,
            width=12,
            font=("verdana", 10, "bold"),
        )
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(
            search_frame,
            command=self.search_data,
            text="Tìm kiếm",
            width=10,
            font=("verdana", 10, "bold"),
            fg="white",
            bg="navyblue",
        )
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(
            search_frame,
            command=self.fetch_data,
            text="Xem tất cả",
            width=10,
            font=("verdana", 10, "bold"),
            fg="white",
            bg="navyblue",
        )
        showAll_btn.grid(row=0, column=4, padx=4)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=90, width=655, height=360)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Khoa")
        self.student_table.heading("course", text="Lớp học phần")
        self.student_table.heading("year", text="Năm học")
        self.student_table.heading("sem", text="Học kỳ")
        self.student_table.heading("id", text="Mã sinh viên")
        self.student_table.heading("name", text="Họ và tên")
        self.student_table.heading("div", text="Ngành học")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Giới tính")
        self.student_table.heading("dob", text="ngày sinh")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Số điện thoại")
        self.student_table.heading("address", text="Địa chỉ")
        self.student_table.heading("teacher", text="Giảng viên")
        self.student_table.heading("photo", text="Tình trạng quét khuôn mặt")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=150)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("div", width=150)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=150)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ----------------Functions Deration-----------------

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_id.get() == ""
            or self.var_std_name.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="phuchau123",
                    database="face_recognition",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Thành công",
                    "Đã lưu thông tin sinh viên thành công",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # =========== Fetch data ===================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="phuchau123",
            database="face_recognition",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============= Get Cursor ==================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # Update Function
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_id.get() == ""
            or self.var_std_name.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Bạn muốn cập nhập thông tin Sinh viên này!",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="phuchau123",
                        database="face_recognition",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,course=%s,semester=%s,Year=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentID=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get(),
                        ),
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Cập nhập thông tin sinh thành công", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete page",
                    "Bạn muốn xóa thông tin sinh viên này?",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="phuchau123",
                        database="face_recognition",
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where StudentID=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Đã xóa thông tin sinh viên!", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # Reset
    def reset_data(self):
        self.var_dep.set("Chọn khoa")
        self.var_course.set("Chọn lớp học phần")
        self.var_year.set("Chọn năm học")
        self.var_semester.set("Chọn học kỳ")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Chọn giới tính")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ---------------------------------search---------------------
    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Chọn":
            messagebox.showerror(
                "lỗi", "Chọn tùy chọn Combo và nhập vào hộp nhập", parent=self.root
            )
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="phuchau123",
                    database="face_recognition",
                )
                my_cursor = conn.cursor()
                spl = (
                    "SELECT StudentID,Name,Dep,course,Year,semester,Division,Gender,Dob,Phone,Address,Roll,Email,Teacher,PhotoSample FROM student where Roll='"
                    + str(self.var_search.get())
                    + "'"
                )
                my_cursor.execute(spl)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    if rows == None:
                        messagebox.showerror(
                            "Error", "Data Not Found", parent=self.root
                        )
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ----------- Generate data set take photo sample------
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_id.get() == ""
            or self.var_std_name.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="phuchau123",
                    database="face_recognition",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student set Dep=%s,course=%s,Year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentID=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1,
                    ),
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # -------Load predifiend data on function -------------

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # Minium Neighbor = 5

                    for x, y, w, h in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    face = face_cropped(my_frame)
                    if face is not None:
                        img_id += 1
                        face = cv2.resize(
                            face, (450, 450), interpolation=cv2.INTER_AREA
                        )
                        print(face.shape)
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                        file_name_path = (
                            "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        )
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 225, 0),
                            2,
                        )
                        cv2.imshow("Face Attendance", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets complied!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
