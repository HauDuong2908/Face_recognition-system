from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from register import RegisterPage
from main import Face_Recognition_System


def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.resizable(0, 0)
        self.window.state("zoomed")
        self.window.title("Login Page")

        # ========================variable========================================
        self.var_email = StringVar()
        self.var_password = StringVar()

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open("images\\background1.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand="yes")
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg="#040405", width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open("images\\vector.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open("images\\hyy.png")
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(
            self.lgn_frame,
            text="Đăng nhập",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 17, "bold"),
        )
        self.sign_in_label.place(x=630, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(
            self.lgn_frame,
            text="Tên đăng nhập",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(
            self.lgn_frame,
            textvariable=self.var_email,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open("images\\username_icon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open("images\\btn1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(
            self.lgn_button_label,
            command=self.login,
            text="ĐĂNG NHẬP",
            font=("yu gothic ui", 13, "bold"),
            width=25,
            bd=0,
            bg="#3047ff",
            cursor="hand2",
            activebackground="#3047ff",
            fg="white",
        )
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(
            self.lgn_frame,
            command=self.forgot_password_window,
            text="Bạn quên mật khẩu ?",
            font=("yu gothic ui", 13, "bold underline"),
            fg="white",
            relief=FLAT,
            activebackground="#040405",
            borderwidth=0,
            background="#040405",
            cursor="hand2",
        )
        self.forgot_button.place(x=630, y=510)
        # =========== Sign Up ==================================================
        self.sign_label = Label(
            self.lgn_frame,
            text="Chưa có tài khoản ?",
            font=("yu gothic ui", 11, "bold"),
            relief=FLAT,
            borderwidth=0,
            background="#040405",
            fg="white",
        )
        self.sign_label.place(x=530, y=560)

        self.signup_img = ImageTk.PhotoImage(file="images\\register.png")
        self.signup_button_label = Button(
            self.lgn_frame,
            command=self.register_window,
            image=self.signup_img,
            bg="#98a65d",
            cursor="hand2",
            borderwidth=0,
            background="#040405",
            activebackground="#040405",
        )
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(
            self.lgn_frame,
            text="Mật khẩu",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(
            self.lgn_frame,
            textvariable=self.var_password,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui", 12, "bold"),
            show="*",
            insertbackground="#6b6a69",
        )
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open("images\\password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage(file="images\\show.png")

        self.hide_image = ImageTk.PhotoImage(file="images\\hide.png")

        self.show_button = Button(
            self.lgn_frame,
            image=self.show_image,
            command=self.show,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(
            self.lgn_frame,
            image=self.hide_image,
            command=self.hide,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show="")

    def hide(self):
        self.show_button = Button(
            self.lgn_frame,
            image=self.show_image,
            command=self.show,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show="*")

    # ---------------------------------Forgot Password-----------------------------------

    # def forgot_password_window(self):

    # -----------------------------------------------------------------------------------

    def register_window(self):
        self.new_window = Toplevel(self.window)
        self.app = RegisterPage(self.new_window)

    def login(self):
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.username_entry.get() == "hau" and self.password_entry.get() == "123":
            messagebox.showinfo(
                "Thành công", "Chào mừng đến với hệ thống nhận diện khuôn mặt"
            )
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="phuchau123",
                database="face_recognition",
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT * FROM register WHERE email=%s and password=%s",
                (self.var_email.get(), self.var_password.get()),
            )

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Inavalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.window)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # =====================Forgot Password Window==================================
    def forgot_password_window(self):
        if self.username_entry.get() == "":
            messagebox.showerror(
                "Error", "Please winter the Email address to reset password"
            )
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="phuchau123",
                database="face_recognition",
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.username_entry.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("My Error", "Please enter the valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                label = Label(
                    self.root2,
                    text="Forgot Password",
                    bg="#040405",
                    fg="#6b6a69",
                    font=("yu gothic ui", 12, "bold"),
                )
                label.place(x=0, y=10, relwidth=1)
                # ====== contact no Frame =========================
                self.lgn_frame1 = Frame(self.root2, bg="#040405")
                self.lgn_frame1.pack(fill=BOTH, expand=True)

                self.contactNo_label1 = Label(
                    self.lgn_frame1,
                    text="Số điện thoại: ",
                    bg="#040405",
                    fg="#4f4e4d",
                    font=("yu gothic ui", 13, "bold"),
                )
            self.contactNo_label1.place(x=0, y=10)

            self.contactNo_entry1 = Entry(
                self.lgn_frame1,
                highlightthickness=0,
                relief=FLAT,
                bg="#040405",
                fg="#6b6a69",
                font=("yu gothic ui ", 12, "bold"),
                insertbackground="#6b6a69",
            )
            self.contactNo_entry1.place(x=30, y=45, width=270)

            self.contactNo_line1 = Canvas(
                self.lgn_frame1,
                width=300,
                height=2.0,
                bg="#bdb9b1",
                highlightthickness=0,
            )
            self.contactNo_line1.place(x=0, y=70)
            # ===== Contact No icon =========
            self.contactNo_icon1 = Image.open("images\\username_icon.png")
            photo = ImageTk.PhotoImage(self.contactNo_icon1)
            self.contactNo_icon_label1 = Label(
                self.lgn_frame1, image=photo, bg="#040405"
            )
            self.contactNo_icon_label1.image = photo
            self.contactNo_icon_label1.place(x=0, y=42)

            # ====== new password Frame =========================

            self.new_password_label1 = Label(
                self.lgn_frame1,
                text="New Password: ",
                bg="#040405",
                fg="#4f4e4d",
                font=("yu gothic ui", 13, "bold"),
            )
            self.new_password_label1.place(x=0, y=78)

            self.new_password_entry1 = Entry(
                self.lgn_frame1,
                highlightthickness=0,
                relief=FLAT,
                bg="#040405",
                fg="#6b6a69",
                font=("yu gothic ui ", 12, "bold"),
                insertbackground="#6b6a69",
            )
            self.new_password_entry1.place(x=30, y=113, width=270)

            self.new_password_line1 = Canvas(
                self.lgn_frame1,
                width=300,
                height=2.0,
                bg="#bdb9b1",
                highlightthickness=0,
            )
            self.new_password_line1.place(x=0, y=138)
            # ===== New password icon =========
            self.new_password_icon1 = Image.open("images\\username_icon.png")
            photo = ImageTk.PhotoImage(self.new_password_icon1)
            self.new_password_icon_label1 = Label(
                self.lgn_frame1, image=photo, bg="#040405"
            )
            self.new_password_icon_label1.image = photo
            self.new_password_icon_label1.place(x=0, y=110)

            # ====== confirm new password Frame =========================

            self.conf_new_password_label1 = Label(
                self.lgn_frame1,
                text="Confirm New Password: ",
                bg="#040405",
                fg="#4f4e4d",
                font=("yu gothic ui", 13, "bold"),
            )
            self.conf_new_password_label1.place(x=0, y=146)

            self.conf_new_password_entry1 = Entry(
                self.lgn_frame1,
                highlightthickness=0,
                relief=FLAT,
                bg="#040405",
                fg="#6b6a69",
                font=("yu gothic ui ", 12, "bold"),
                insertbackground="#6b6a69",
            )
            self.conf_new_password_entry1.place(x=30, y=181, width=270)

            self.conf_new_password_line1 = Canvas(
                self.lgn_frame1,
                width=300,
                height=2.0,
                bg="#bdb9b1",
                highlightthickness=0,
            )
            self.conf_new_password_line1.place(x=0, y=206)
            # =====Confirm New password icon =========
            self.conf_new_password_icon1 = Image.open("images\\username_icon.png")
            photo = ImageTk.PhotoImage(self.conf_new_password_icon1)
            self.conf_new_password_icon_label1 = Label(
                self.lgn_frame1, image=photo, bg="#040405"
            )
            self.conf_new_password_icon_label1.image = photo
            self.conf_new_password_icon_label1.place(x=0, y=178)

            # ===== Reset Button =============
            self.lgn_button1 = Image.open("images\\btn1.png")
            photo1 = ImageTk.PhotoImage(self.lgn_button1)
            self.lgn_button_label1 = Label(self.lgn_frame1, image=photo1, bg="#040405")
            self.lgn_button_label1.image = photo1
            self.lgn_button_label1.place(x=10, y=300)
            self.reset = Button(
                self.lgn_button_label1,
                command=self.reset_password,
                text="Reset",
                font=("yu gothic ui", 13, "bold"),
                width=25,
                bd=0,
                bg="#3047ff",
                cursor="hand2",
                activebackground="#3047ff",
                fg="white",
            )
            self.reset.place(x=20, y=10)

    # =====================Reset Password==========================================

    def reset_password(self):
        if self.contactNo_entry1.get() == "":
            messagebox.showerror("", "Hãy nhập số điện thoại", parent=self.root2)
        elif self.new_password_entry1.get() == "":
            messagebox.showerror("", "Hãy nhập mật khẩu mới", parent=self.root2)
        elif self.conf_new_password_entry1.get() == "":
            messagebox.showerror("", "Hãy nhập lại mật khẩu mới", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="phuchau123",
                database="face_recognition",
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s and contact=%s"
            value = (self.username_entry.get(), self.contactNo_entry1.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "", "Hãy điền đầy đủ các thông tin trên", parent=self.root2
                )
            else:
                query = "UPDATE register SET password=%s WHERE email=%s"
                value = (
                    self.new_password_entry1.get(),
                    self.username_entry.get(),
                )
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Thông báo",
                    "Bạn đã đổi mật khẩu mới, vui lòng nhập mật khẩu mới vào tài khoản",
                    parent=self.root2,
                )
                self.root2.destroy()


if __name__ == "__main__":
    main()
