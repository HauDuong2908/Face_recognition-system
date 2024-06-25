from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk, messagebox
import mysql.connector
import face_recognition
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root,
            text="Train Data Set",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue",
        )
        title_lbl.place(x=0, y=0, width=1380, height=45)

        img_top = Image.open(r"college_images\bg_left_student.png")
        img_top = img_top.resize((1380, 225), Image.ANTIALIAS)
        self.photo_img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photo_img_top)
        f_lbl.place(x=0, y=45, width=1380, height=225)

        # button
        b1_1 = Button(
            self.root,
            text="Train Data",
            command=self.train_classifier,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
            bd=5,
        )
        b1_1.place(x=0, y=355, width=1380, height=60)

        img_bottom = Image.open(r"college_images\bg_left_student.png")
        img_bottom = img_bottom.resize((1380, 225), Image.ANTIALIAS)
        self.photo_img_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photo_img_bottom)
        f_lbl.place(x=0, y=440, width=1380, height=225)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # Gray scale image
            imgNp = np.array(img, dtype=np.uint8)
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imgNp)
            ids.append(id)
            cv2.imshow("Training", imgNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ------------ Train the classifier And save ---------------
        print(dir(cv2.face))
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, ids)
        recognizer.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets completed!!! ")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
