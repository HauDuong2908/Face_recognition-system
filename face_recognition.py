from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk, messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")

        title_lbl = Label(
            self.root,
            text="Face Recognition",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue",
        )
        title_lbl.place(x=0, y=0, width=1380, height=45)

        # 1st image
        img_top = Image.open(r"college_images\Face\Face_data.png")
        img_top = img_top.resize((700, 700), Image.ANTIALIAS)
        self.photo_img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photo_img_top)
        f_lbl.place(x=0, y=45, width=650, height=700)

        # 2st image
        img_bottom = Image.open(
            r"college_images\Face\face-id-4151714-852eb4adf6b741e59658793918cc9631.gif"
        )
        img_bottom = img_bottom.resize((750, 700), Image.ANTIALIAS)
        self.photo_img_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photo_img_bottom)
        f_lbl.place(x=650, y=55, width=750, height=700)

        # button
        b1_1 = Button(
            f_lbl,
            text="Nhận Diện",
            cursor="hand2",
            font=("tahoma", 12, "bold"),
            bg="white",
            fg="navyblue",
            bd=5,
            command=self.face_recog,
        )
        b1_1.place(x=290, y=550, width=180, height=35)

    # -----------Attendance--------------------------
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", encoding="utf-8", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if (
                ((i not in name_list))
                and ((r not in name_list))
                and ((n not in name_list))
            ):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {d}, {dtString}, {d1}, Co mat")

    # -----------Face Recognition--------------------

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors
            )

            coord = []

            for x, y, w, h in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="phuchau123",
                    database="face_recognition",
                )
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where StudentID=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n is not None else "Unknown"

                my_cursor.execute("select Roll from student where StudentID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r is not None else "Unknown"

                my_cursor.execute("select Dep from student where StudentID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d is not None else "Unknown"

                my_cursor.execute(
                    "select StudentID from student where StudentID=" + str(id)
                )
                i = my_cursor.fetchone()
                i = "+".join(i) if d is not None else "Unknown"

                if confidence > 77:
                    cv2.putText(
                        img,
                        f"ID: {i}",
                        (x, y - 75),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Roll: {r}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Name: {n}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Department: {d}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )

                coord = [x, y, w, h]

            return coord

        # ------------------------

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(
                img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf
            )
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        print(clf)

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Nhận Diện", img)

            key = cv2.waitKey(1) & 0xFF
            if key == 13:  # Phím Enter
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
