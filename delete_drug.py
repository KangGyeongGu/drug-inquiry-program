# delete_drug.py
import tkinter as tk
from tkinter import messagebox
from mysql.connector import Error


class DeleteDrug:
    def __init__(self, master, db, drug_id, refresh_callback):
        self.db = db
        self.drug_id = drug_id
        self.refresh_callback = refresh_callback
        self.confirm_deletion()

    def confirm_deletion(self):
        confirm = messagebox.askyesno("확인", f"DrugBank ID {self.drug_id}를 삭제하시겠습니까?")
        if confirm:
            try:
                self.db.execute_query(
                    "DELETE FROM DRUG WHERE DRUGBANK_ID = %s",
                    (self.drug_id,)
                )
                messagebox.showinfo("성공", "약물이 성공적으로 삭제되었습니다.")
                self.refresh_callback()
            except Error as e:
                messagebox.showerror("삭제 오류", f"오류: {e}")
