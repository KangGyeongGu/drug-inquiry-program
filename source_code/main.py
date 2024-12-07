# main.py
import tkinter as tk
from connection_frame import ConnectionFrame
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from tkinter import messagebox
import platform

def set_font():
    font_path = 'C:/Windows/Fonts/malgun.ttf' 
    if not os.path.exists(font_path):
        messagebox.showerror("폰트 오류", "Malgun Gothic 폰트를 찾을 수 없음")
        return

    font_prop = fm.FontProperties(fname=font_path, size=12)
    plt.rcParams['font.family'] = font_prop.get_name()
    plt.rcParams['axes.unicode_minus'] = False 

def main():
    root = tk.Tk()
    root.title("약물 조회 프로그램")

    os_name = platform.system()
    if os_name == "Windows":
        root.state('zoomed') 
    elif os_name == "Darwin": 
        root.attributes('-zoomed', True)
    else:  
        root.state('zoomed') 

    set_font() 

    app = ConnectionFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
