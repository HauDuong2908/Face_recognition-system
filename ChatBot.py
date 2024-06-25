from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Bot")
        self.root.geometry("730x650+0+0")
        self.root.bind("<Return>", self.enter_func)

        nltk.download("punkt")
        nltk.download("stopwords")
        self.stop_words = set(stopwords.words("english"))
        self.responses = {
            "hello": ["Hi there!", "Hello!"],
            "how are you": [
                "I'm doing well, thank you!",
                "I'm fine, thanks for asking.",
            ],
            "what is your name": [
                "My name is Bot. Nice to meet you!",
                "You can call me Bot.",
            ],
            "what can you do": ["I can answer your questions.", "I can chat with you."],
            "bye": ["Goodbye!", "See you later."],
            "thanks": ["You're welcome!", "No problem!"],
            "who is doing this project": [
                "It's Duong Phuc Hau with student code 20IT046, class 20AD, Please contact us at the email address dphau.20it2@vku.udn.vn!.",
                "It's Duong Phuc Hau with student code 20IT046, class 20AD, Please contact us at phone number 0979548446.",
            ],
            "bye": ["Goodbye!", "See you later."],
            "thanks": ["You're welcome!", "No problem!"],
        }
        self.chain = {}

        main_frame = Frame(self.root, bd=4, bg="white", width=610)
        main_frame.pack()

        # Image background
        img_chat = Image.open(
            "C:\Học để thành công\Face_recognition system\Chat_Bot.jpg"
        )
        img_chat = img_chat.resize((200, 90), Image.ANTIALIAS)
        self.PhotoImg = ImageTk.PhotoImage(img_chat)

        # Title chat bot
        TitleLabel = Label(
            main_frame,
            bd=3,
            relief=RAISED,
            anchor="nw",
            width=730,
            compound=LEFT,
            image=self.PhotoImg,
            text="Chat Me",
            font=("times new roman", 30, "bold"),
            fg="green",
            bg="white",
        )
        TitleLabel.pack(side=TOP)

        # Frame Chat
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(
            main_frame,
            bd=3,
            width=65,
            height=20,
            relief=RAISED,
            font=("arial", 14),
            yscrollcommand=self.scroll_y.set,
        )
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        # Button Frame Chat
        btn_frame = Frame(self.root, bd=4, bg="white", width=730)
        btn_frame.pack()

        label_1 = Label(
            btn_frame,
            text="Type Something",
            font=("times new roman", 15, "bold"),
            fg="green",
            bg="white",
        )
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        # Message chat
        self.entry = StringVar()
        self.entry1 = ttk.Entry(
            btn_frame,
            textvariable=self.entry,
            width=39,
            font=("times new roman", 17, "bold"),
        )
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        # Send
        self.send = Button(
            btn_frame,
            command=self.send,
            text="Send",
            font=("times new roman", 16, "bold"),
            width=5,
            bg="green",
        )
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        # Clear Data
        self.clear = Button(
            btn_frame,
            command=self.clear,
            text="Clear Data",
            font=("times new roman", 16, "bold"),
            width=8,
            bg="red",
            fg="white",
        )
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        # Label 2
        self.msg = ""
        self.label_2 = Label(
            btn_frame,
            text=self.msg,
            font=("times new roman", 15, "bold"),
            fg="red",
            bg="white",
        )
        self.label_2.grid(row=1, column=1, padx=5, sticky=W)

    # ----------------- Function Declaration -------------------
    def enter_func(self, event):
        self.send.invoke()
        self.entry.set("")

    def clear(self):
        clear = self.text.delete("1.0", END)
        self.entry.set("")

    def train(self, text):
        # Xử lý dữ liệu và huấn luyện mô hình Markov
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word not in self.stop_words]
        for i in range(len(tokens) - 1):
            if tokens[i] not in self.chain:
                self.chain[tokens[i]] = {}
            if tokens[i + 1] not in self.chain[tokens[i]]:
                self.chain[tokens[i]][tokens[i + 1]] = 1
            else:
                self.chain[tokens[i]][tokens[i + 1]] += 1

    def generate_response(self, input_text):
        # Sử dụng mô hình Markov để sinh ra phản hồi
        tokens = word_tokenize(input_text.lower())
        tokens = [word for word in tokens if word not in self.stop_words]
        if tokens:
            current_word = tokens[-1]
            response = ""
            for i in range(20):
                if current_word in self.chain:
                    next_word = max(
                        self.chain[current_word], key=self.chain[current_word].get
                    )
                    response += " " + next_word
                    current_word = next_word
                else:
                    break
            return response.strip()
        else:
            return None

    def send(self):
        send = "Bạn: " + self.entry.get()
        self.text.insert(END, "\n" + send)

        if self.entry.get() == "":
            self.msg = "Please enter some input"
            self.label_2.config(text=self.msg, fg="red")
        else:
            self.msg = ""
            self.label_2.config(text=self.msg, fg="red")

            # Tìm kiếm phản hồi từ từ điển
            input_text = self.entry.get()
            response = None
            for word in self.responses:
                if word in input_text.lower():
                    response = random.choice(self.responses[word])
                    break

            # Nếu không tìm thấy phản hồi, sử dụng mô hình Markov để sinh ra phản hồi
            if response is None:
                response = self.generate_response(input_text)

            # Thêm phản hồi vào khung chat
            if response is not None:
                bot_response = "Bot: " + response
                self.text.insert(END, "\n" + bot_response)
            else:
                self.text.insert(
                    END, "\n" + "Bot: I don't understand. Can you rephrase that?"
                )

        # Xoá nội dung trong ô nhập liệu
        self.entry.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
