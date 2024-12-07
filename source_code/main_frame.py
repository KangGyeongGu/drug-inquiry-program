# main_frame.py
import tkinter as tk
from tkinter import ttk, messagebox
from view_details import ViewDetails
from add_drug import AddDrug
from edit_drug import EditDrug
from delete_drug import DeleteDrug
from mysql.connector import Error

class MainFrame(tk.Frame):
    def __init__(self, master, db):
        super().__init__(master)
        self.master = master
        self.db = db
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # 검색 섹션
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="검색어:").grid(row=0, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(search_frame, width=50)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        search_button = tk.Button(search_frame, text="검색", command=self.search_drugs)
        search_button.grid(row=0, column=2, padx=5, pady=5)

        view_all_button = tk.Button(search_frame, text="전체 조회", command=self.view_all_drugs)
        view_all_button.grid(row=0, column=3, padx=5, pady=5)

        # 초기화 버튼 추가
        reset_button = tk.Button(search_frame, text="초기화", command=self.reset_search)
        reset_button.grid(row=0, column=4, padx=5, pady=5)  # 버튼을 오른쪽에 추가

        # Treeview 설정
        columns = ("DrugBank_ID", "Name", "Description", "CAS_Number")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor='center' if col != "Description" else 'w')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 버튼 섹션
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        view_button = tk.Button(button_frame, text="상세 정보 보기", command=self.view_details)
        view_button.grid(row=0, column=0, padx=5)

        add_button = tk.Button(button_frame, text="약물 추가", command=self.add_drug)
        add_button.grid(row=0, column=1, padx=5)

        edit_button = tk.Button(button_frame, text="약물 수정", command=self.edit_drug)
        edit_button.grid(row=0, column=2, padx=5)

        delete_button = tk.Button(button_frame, text="약물 삭제", command=self.delete_drug)
        delete_button.grid(row=0, column=3, padx=5)

    def search_drugs(self):
        keyword = self.search_entry.get().strip()
        if not keyword:
            messagebox.showwarning("경고", "검색어를 입력하세요.")
            return

        query = """
            SELECT DRUG.DRUGBANK_ID, DRUG.NAME, DRUG.DESCRIPTION, DRUG.CAS_NUMBER
            FROM DRUG
            WHERE DRUG.DRUGBANK_ID = %s OR DRUG.NAME LIKE %s
        """
        like_keyword = f"%{keyword}%"
        try:
            results = self.db.execute_query(query, (keyword, like_keyword), fetchall=True)
            self.update_treeview(results)
        except Error as e:
            messagebox.showerror("검색 오류", f"오류: {e}")

    def view_all_drugs(self):
        query = """
            SELECT DRUG.DRUGBANK_ID, DRUG.NAME, DRUG.DESCRIPTION, DRUG.CAS_NUMBER
            FROM DRUG
        """
        try:
            results = self.db.execute_query(query, fetchall=True)
            self.update_treeview(results)
        except Error as e:
            messagebox.showerror("조회 오류", f"오류: {e}")

    def update_treeview(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert("", tk.END, values=(
                row["DRUGBANK_ID"],
                row["NAME"],
                row["DESCRIPTION"],
                row["CAS_NUMBER"]
            ))

    def view_details(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("경고", "약물을 선택하세요.")
            return

        drug_id = self.tree.item(selected_item[0])['values'][0]
        ViewDetails(self.master, self.db, drug_id)

    def add_drug(self):
        AddDrug(self.master, self.db, self.refresh)

    def edit_drug(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("경고", "수정할 약물을 선택하세요.")
            return

        drug_id = self.tree.item(selected_item[0])['values'][0]
        EditDrug(self.master, self.db, drug_id, self.refresh)

    def delete_drug(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("경고", "삭제할 약물을 선택하세요.")
            return

        drug_id = self.tree.item(selected_item[0])['values'][0]
        DeleteDrug(self.master, self.db, drug_id, self.refresh)

    def refresh(self):
        self.view_all_drugs()

    # 초기화 버튼 동작 메서드 추가
    def reset_search(self):
        """
        검색어 입력 필드를 지우고, Treeview에 표시된 모든 약물 정보를 삭제합니다.
        """
        # 검색어 입력 필드 지우기
        self.search_entry.delete(0, tk.END)
        
        # Treeview의 모든 항목 삭제
        for item in self.tree.get_children():
            self.tree.delete(item)

