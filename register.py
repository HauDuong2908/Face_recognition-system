from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector


class RegisterPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.resizable(0, 0)
        self.window.state("zoomed")
        self.window.title("Login Page")

        # =======================variable=========================================
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_contact_no = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_confPass = StringVar()

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open("images\\background1.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand="yes")
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg="#040405", width=1250, height=600)
        self.lgn_frame.place(x=60, y=70)

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
        self.sign_in_image_label.place(x=780, y=10)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(
            self.lgn_frame,
            text="Đăng ký",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 17, "bold"),
        )
        self.sign_in_label.place(x=810, y=115)

        # ========================================================================
        # ============================Firstname====================================
        # ========================================================================
        self.Firstname_label = Label(
            self.lgn_frame,
            text="First Name: ",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.Firstname_label.place(x=550, y=175)

        self.Firstname_entry = Entry(
            self.lgn_frame,
            textvariable=self.var_first_name,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.Firstname_entry.place(x=580, y=210, width=270)

        self.Firstname_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.Firstname_line.place(x=550, y=235)
        # ===== Username icon =========
        self.Firstname_icon = Image.open("images\\username_icon.png")
        photo = ImageTk.PhotoImage(self.Firstname_icon)
        self.Firstname_icon = Label(self.lgn_frame, image=photo, bg="#040405")
        self.Firstname_icon.image = photo
        self.Firstname_icon.place(x=550, y=207)
        # ========================================================================
        # ============================Lastname====================================
        # ========================================================================
        self.Lastname_label = Label(
            self.lgn_frame,
            text="Last Name: ",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.Lastname_label.place(x=900, y=175)

        self.Lastname_entry = Entry(
            self.lgn_frame,
            textvariable=self.var_last_name,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.Lastname_entry.place(x=930, y=210, width=270)

        self.Lastname_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.Lastname_line.place(x=900, y=235)
        # ===== Username icon =========
        self.Lastname_icon = Image.open("images\\username_icon.png")
        photo = ImageTk.PhotoImage(self.Lastname_icon)
        self.Lastname_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.Lastname_icon_label.image = photo
        self.Lastname_icon_label.place(x=900, y=207)
        # ========================================================================
        # ============================Contact No====================================
        # ========================================================================
        self.contactNo_label = Label(
            self.lgn_frame,
            text="Số điện thoại: ",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.contactNo_label.place(x=550, y=255)

        self.contactNo_entry = Entry(
            self.lgn_frame,
            textvariable=self.var_contact_no,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.contactNo_entry.place(x=580, y=290, width=270)

        self.contactNo_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.contactNo_line.place(x=550, y=315)
        # ===== Username icon =========
        self.contactNo_icon = Image.open("images\\username_icon.png")
        photo = ImageTk.PhotoImage(self.contactNo_icon)
        self.contactNo_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.contactNo_icon_label.image = photo
        self.contactNo_icon_label.place(x=550, y=287)

        # ========================================================================
        # ============================Email====================================
        # ========================================================================
        self.email_label = Label(
            self.lgn_frame,
            text="Email: ",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.email_label.place(x=900, y=255)

        self.email_entry = Entry(
            self.lgn_frame,
            textvariable=self.var_email,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.email_entry.place(x=930, y=290, width=270)

        self.email_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.email_line.place(x=900, y=315)
        # ===== Email icon =========
        self.email_icon = Image.open("images\\username_icon.png")
        photo = ImageTk.PhotoImage(self.email_icon)
        self.email_icon = Label(self.lgn_frame, image=photo, bg="#040405")
        self.email_icon.image = photo
        self.email_icon.place(x=900, y=287)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open("images\\btn1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=720, y=450)
        self.login = Button(
            self.lgn_button_label,
            command=self.register_data,
            text="ĐĂNG KÝ",
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
            text="Đăng nhập ngay bây giờ!",
            font=("yu gothic ui", 13, "bold underline"),
            fg="white",
            relief=FLAT,
            activebackground="#040405",
            borderwidth=0,
            background="#040405",
            cursor="hand2",
        )
        self.forgot_button.place(x=770, y=510)

        # ========================================================================
        # ============================Confirm password====================================
        # ========================================================================
        self.con_password_label = Label(
            self.lgn_frame,
            text="Nhập lại Mật khẩu",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.con_password_label.place(x=900, y=335)

        self.con_password_entry = Entry(
            self.lgn_frame,
            textvariable=self.var_confPass,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui", 12, "bold"),
            # show="*",
            insertbackground="#6b6a69",
        )
        self.con_password_entry.place(x=930, y=370, width=244)

        self.con_password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.con_password_line.place(x=900, y=395)
        # ======== Password icon ================
        self.con_password_icon = Image.open("images\\password_icon.png")
        photo = ImageTk.PhotoImage(self.con_password_icon)
        self.con_password_icon = Label(self.lgn_frame, image=photo, bg="#040405")
        self.con_password_icon.image = photo
        self.con_password_icon.place(x=900, y=367)

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
        self.password_label.place(x=550, y=335)

        self.password_entry = Entry(
            self.lgn_frame,
            textvariable=self.var_pass,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui", 12, "bold"),
            # show="*",
            insertbackground="#6b6a69",
        )
        self.password_entry.place(x=580, y=370, width=244)

        self.password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.password_line.place(x=550, y=395)
        # ======== Password icon ================
        self.password_icon = Image.open("images\\password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=367)

    # ===========================Function declaration=============================================

    def register_data(self):
        if self.var_first_name.get() == "" or self.var_last_name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confPass.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password must be the same"
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
            value = (self.var_email.get(),)  # Pass the parameter as a tuple
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror(
                    "Error", "User already exists, please try another email"
                )
            else:
                insert_query = "INSERT INTO register VALUES (%s, %s, %s, %s, %s)"
                insert_values = (
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_contact_no.get(),
                    self.var_email.get(),
                    self.var_pass.get(),
                )
                my_cursor.execute(insert_query, insert_values)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered successfully")


if __name__ == "__main__":
    window = Tk()
    RegisterPage(window)
    window.mainloop()
