# view_details.py
import tkinter as tk
from tkinter import ttk, messagebox
from mysql.connector import Error

class ViewDetails(tk.Toplevel):
    def __init__(self, master, db, drug_id):
        super().__init__(master)
        self.db = db
        self.drug_id = drug_id
        self.title(f"{drug_id} 상세 정보")
        self.resizable(True, True)  
        self.set_window_size()
        self.create_widgets()

    def set_window_size(self):
        # 메인 창의 크기 가져오기
        self.master.update_idletasks() 
        main_width = self.master.winfo_width()
        main_height = self.master.winfo_height()

        # 새 창의 크기 계산 (80%)
        new_width = int(main_width * 0.8)
        new_height = int(main_height * 0.8)

        # 메인 창의 위치 가져오기
        main_x = self.master.winfo_x()
        main_y = self.master.winfo_y()

        # 새 창의 위치 계산
        new_x = main_x + (main_width - new_width) // 2
        new_y = main_y + (main_height - new_height) // 2

        # 새 창의 크기와 위치 설정
        self.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")

    def create_widgets(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # 약물 및 분류 정보 탭
        self.add_drug_class_tab(notebook)
        # 약물-효소-작용 정보 탭
        self.add_enzyme_tab(notebook)
        # 약물-타겟 정보 탭
        self.add_target_tab(notebook)
        # 약물-경로 연관 정보 탭
        self.add_pathway_tab(notebook)

    def add_drug_class_tab(self, notebook):
        frame = tk.Frame(notebook)
        notebook.add(frame, text="약물 및 분류 정보")

        query = """
            SELECT DRUG.DRUGBANK_ID, DRUG.NAME, DRUG.DESCRIPTION, DRUG.CAS_NUMBER,
                   CLASSIFICATION.KINGDOM, CLASSIFICATION.SUPERCLASS, CLASSIFICATION.CLASS, CLASSIFICATION.SUBCLASS
            FROM DRUG
            LEFT JOIN CLASSIFICATION ON DRUG.DRUGBANK_ID = CLASSIFICATION.DRUGBANK_ID
            WHERE DRUG.DRUGBANK_ID = %s
        """
        try:
            drug_class_info = self.db.execute_query(query, (self.drug_id,), fetch=True)
            if drug_class_info:
                columns = ["DrugBank_ID", "Name", "Description", "CAS_Number", "Kingdom", "Superclass", "Class", "Subclass"]
                tree_frame = tk.Frame(frame)
                tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    # Description 컬럼은 더 넓게 설정
                    if col == "Description":
                        tree.column(col, width=600, anchor='w')
                    else:
                        tree.column(col, width=150, anchor='center', stretch=True)
                tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                # 가로 스크롤바 추가
                h_scrollbar = ttk.Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
                tree.configure(xscrollcommand=h_scrollbar.set)
                h_scrollbar.pack(side=tk.BOTTOM, fill='x')

                tree.insert("", tk.END, values=(
                    drug_class_info["DRUGBANK_ID"],
                    drug_class_info["NAME"],
                    drug_class_info["DESCRIPTION"],
                    drug_class_info["CAS_NUMBER"],
                    drug_class_info["KINGDOM"] or "N/A",
                    drug_class_info["SUPERCLASS"] or "N/A",
                    drug_class_info["CLASS"] or "N/A",
                    drug_class_info["SUBCLASS"] or "N/A"
                ))
            else:
                tk.Label(frame, text="약물 및 분류 정보가 없습니다.").pack(padx=10, pady=10)
        except Error as e:
            messagebox.showerror("조회 오류", f"오류: {e}")

    def add_enzyme_tab(self, notebook):
        frame = tk.Frame(notebook)
        notebook.add(frame, text="약물-효소-작용 정보")

        query = """
            SELECT DRUG_ENZYME_ACTION.ENZYME_ACTION, ENZYME.ENZYME_ID, ENZYME.NAME, ENZYME.ORGANISM
            FROM DRUG_ENZYME_ACTION
            LEFT JOIN ENZYME ON DRUG_ENZYME_ACTION.ENZYME_ID = ENZYME.ENZYME_ID
            WHERE DRUG_ENZYME_ACTION.DRUGBANK_ID = %s
        """
        try:
            enzyme_info = self.db.execute_query(query, (self.drug_id,), fetchall=True)
            if enzyme_info:
                columns = ["ENZYME_ID", "Name", "Organism", "Action"]
                tree_frame = tk.Frame(frame)
                tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=200, anchor='center', stretch=True)
                tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                # 가로 스크롤바 추가
                h_scrollbar = ttk.Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
                tree.configure(xscrollcommand=h_scrollbar.set)
                h_scrollbar.pack(side=tk.BOTTOM, fill='x')

                for row in enzyme_info:
                    tree.insert("", tk.END, values=(
                        row["ENZYME_ID"] or "N/A",
                        row["NAME"] or "N/A",
                        row["ORGANISM"] or "N/A",
                        row["ENZYME_ACTION"] or "N/A"
                    ))
            else:
                tk.Label(frame, text="약물-효소-작용 정보가 없습니다.").pack(padx=10, pady=10)
        except Error as e:
            messagebox.showerror("조회 오류", f"오류: {e}")

    def add_target_tab(self, notebook):
        frame = tk.Frame(notebook)
        notebook.add(frame, text="약물-타겟 정보")

        query = """
            SELECT DRUG_TARGET.TARGET_ID, TARGET.NAME, TARGET.ORGANISM
            FROM DRUG_TARGET
            LEFT JOIN TARGET ON DRUG_TARGET.TARGET_ID = TARGET.TARGET_ID
            WHERE DRUG_TARGET.DRUGBANK_ID = %s
        """
        try:
            target_info = self.db.execute_query(query, (self.drug_id,), fetchall=True)
            if target_info:
                columns = ["TARGET_ID", "Name", "Organism"]
                tree_frame = tk.Frame(frame)
                tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=220, anchor='center', stretch=True)
                tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                # 가로 스크롤바 추가
                h_scrollbar = ttk.Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
                tree.configure(xscrollcommand=h_scrollbar.set)
                h_scrollbar.pack(side=tk.BOTTOM, fill='x')

                for row in target_info:
                    tree.insert("", tk.END, values=(
                        row["TARGET_ID"] or "N/A",
                        row["NAME"] or "N/A",
                        row["ORGANISM"] or "N/A"
                    ))
            else:
                tk.Label(frame, text="약물-타겟 정보가 없습니다.").pack(padx=10, pady=10)
        except Error as e:
            messagebox.showerror("조회 오류", f"오류: {e}")

    def add_pathway_tab(self, notebook):
        frame = tk.Frame(notebook)
        notebook.add(frame, text="약물-경로 연관 정보")

        query = """
            SELECT DRUG_PATH_ASSOCIATION.SMPDB_ID, PATHWAY.NAME, PATHWAY.CATEGORY, DRUG_PATH_ASSOCIATION.UNIPROT_ID
            FROM DRUG_PATH_ASSOCIATION
            LEFT JOIN PATHWAY ON DRUG_PATH_ASSOCIATION.SMPDB_ID = PATHWAY.SMPDB_ID
            WHERE DRUG_PATH_ASSOCIATION.DRUGBANK_ID = %s
        """
        try:
            pathway_info = self.db.execute_query(query, (self.drug_id,), fetchall=True)
            if pathway_info:
                columns = ["SMPDB_ID", "Name", "Category", "UNIPROT_ID"]
                tree_frame = tk.Frame(frame)
                tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=200, anchor='center', stretch=True)
                tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                # 가로 스크롤바 추가
                h_scrollbar = ttk.Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
                tree.configure(xscrollcommand=h_scrollbar.set)
                h_scrollbar.pack(side=tk.BOTTOM, fill='x')

                for row in pathway_info:
                    tree.insert("", tk.END, values=(
                        row["SMPDB_ID"] or "N/A",
                        row["NAME"] or "N/A",
                        row["CATEGORY"] or "N/A",
                        row["UNIPROT_ID"] or "N/A"
                    ))
            else:
                tk.Label(frame, text="약물-경로 연관 정보가 없습니다.").pack(padx=10, pady=10)
        except Error as e:
            messagebox.showerror("조회 오류", f"오류: {e}")
