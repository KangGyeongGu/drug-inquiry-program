# connection_frame.py
import tkinter as tk
from tkinter import messagebox
from database import Database
from main_frame import MainFrame
from mysql.connector import Error


class ConnectionFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20)
        self.create_widgets()

    def create_widgets(self):
        labels = ["호스트:", "포트:", "데이터베이스:", "사용자 이름:", "비밀번호:"]
        defaults = ["", "", "", "", ""]
        self.entries = {}

        for i, (label_text, default) in enumerate(zip(labels, defaults)):
            label = tk.Label(self, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky='e')
            entry = tk.Entry(self, width=30, show='*' if label_text == "비밀번호:" else '')
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry.insert(0, default)
            self.entries[label_text] = entry

        connect_button = tk.Button(self, text="접속", command=self.connect_to_db)
        connect_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def connect_to_db(self):
        host = self.entries["호스트:"].get()
        port = self.entries["포트:"].get()
        database = self.entries["데이터베이스:"].get()
        user = self.entries["사용자 이름:"].get()
        password = self.entries["비밀번호:"].get()

        try:
            db = Database(host, port, database, user, password)
            messagebox.showinfo("성공", "데이터베이스에 성공적으로 연결되었습니다.")
            self.destroy()
            MainFrame(self.master, db)
        except Error as e:
            messagebox.showerror("연결 실패", f"오류: {e}")
