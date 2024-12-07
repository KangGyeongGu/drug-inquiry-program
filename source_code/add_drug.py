# add_drug.py
import tkinter as tk
from tkinter import ttk, messagebox
from mysql.connector import Error, IntegrityError

class AddDrug(tk.Toplevel):
    def __init__(self, master, db, refresh_callback):
        super().__init__(master)
        self.db = db
        self.refresh_callback = refresh_callback
        self.title("약물 추가")
        self.resizable(True, True)  # 창 크기 조정 가능
        self.set_window_size()
        self.create_widgets()

    def set_window_size(self):
        # 메인 창의 크기 가져오기
        self.master.update_idletasks()  # 창 업데이트
        main_width = self.master.winfo_width()
        main_height = self.master.winfo_height()

        # 새 창의 크기 계산 (80%)
        new_width = int(main_width * 0.8)
        new_height = int(main_height * 0.8)

        # 메인 창의 위치 가져오기
        main_x = self.master.winfo_x()
        main_y = self.master.winfo_y()

        # 새 창의 위치 계산 (메인 창의 중앙)
        new_x = main_x + (main_width - new_width) // 2
        new_y = main_y + (main_height - new_height) // 2

        # 새 창의 크기와 위치 설정
        self.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")

    def create_widgets(self):
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        canvas = tk.Canvas(main_frame)
        v_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        h_scrollbar = ttk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar.pack(side="bottom", fill="x")

        self.entries = {}
        self.create_form(scrollable_frame)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10, fill=tk.X, side=tk.BOTTOM)

        register_button = tk.Button(button_frame, text="등록", command=self.submit)
        register_button.pack()

    def create_form(self, frame):
        sections = {
            "DRUG 정보": ["DrugBank ID", "Name", "Description", "CAS Number"],
            "CLASSIFICATION 정보": ["KINGDOM", "SUPERCLASS", "CLASS", "SUBCLASS"],
            "TARGET 정보": ["Target ID"],
            "ENZYME 정보": ["Enzyme ID", "Enzyme Action"],
            "PATHWAY 정보": ["SMPDB ID", "UNIPROT ID"]
        }

        # 관리할 다중 입력 섹션의 레퍼런스 저장
        self.dynamic_sections = {
            "TARGET 정보": [],
            "ENZYME 정보": [],
            "PATHWAY 정보": []
        }

        for section, fields in sections.items():
            if section in ["TARGET 정보", "ENZYME 정보", "PATHWAY 정보"]:
                self.create_dynamic_section(frame, section, fields)
            else:
                section_frame = tk.LabelFrame(frame, text=section)
                section_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                for idx, field in enumerate(fields):
                    label = tk.Label(section_frame, text=f"{field}:")
                    label.grid(row=idx, column=0, padx=10, pady=10, sticky='e')
                    entry = tk.Entry(section_frame, width=50)
                    entry.grid(row=idx, column=1, padx=10, pady=10)
                    self.entries[f"{section}_{field}"] = entry

    def create_dynamic_section(self, frame, section, fields):
        section_frame = tk.LabelFrame(frame, text=section)
        section_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 내부 프레임과 추가 버튼 생성
        inner_frame = tk.Frame(section_frame)
        inner_frame.pack(fill=tk.BOTH, expand=True)

        # 첫 번째 입력 행 추가
        self.add_dynamic_row(inner_frame, section, fields)

    def add_dynamic_row(self, parent, section, fields, initial_values=None):
        row_frame = tk.Frame(parent)
        row_frame.pack(fill=tk.X, pady=2)

        entries = []
        for idx, field in enumerate(fields):
            label = tk.Label(row_frame, text=f"{field}:")
            label.grid(row=0, column=idx*2, padx=5, pady=5, sticky='e')
            entry = tk.Entry(row_frame, width=30)
            entry.grid(row=0, column=idx*2 + 1, padx=5, pady=5, sticky='w')
            if initial_values and idx < len(initial_values):
                entry.insert(0, initial_values[idx])
            entries.append(entry)

        # + 버튼과 - 버튼 추가
        button_frame = tk.Frame(row_frame)
        button_frame.grid(row=0, column=len(fields)*2, padx=5, pady=5)

        del_button = tk.Button(button_frame, text="-", command=lambda: self.remove_dynamic_row(row_frame, section))
        del_button.pack(side="left")

        add_button = tk.Button(button_frame, text="+", command=lambda: self.add_dynamic_row(parent, section, fields))
        add_button.pack(side="left", padx=(0, 2))

        

        # 해당 섹션의 리스트에 추가
        self.dynamic_sections[section].append(entries)

    def remove_dynamic_row(self, row_frame, section):
        # 해당 입력 행 제거
        row_frame.destroy()
        # dynamic_sections에서 해당 입력 필드 리스트 제거
        for entries in self.dynamic_sections[section]:
            if all(not entry.winfo_exists() for entry in entries):
                self.dynamic_sections[section].remove(entries)
                break

    def submit(self):
        try:
            # DRUG 정보
            db_id = self.entries["DRUG 정보_DrugBank ID"].get().strip()
            name = self.entries["DRUG 정보_Name"].get().strip()
            description = self.entries["DRUG 정보_Description"].get().strip()
            cas_number = self.entries["DRUG 정보_CAS Number"].get().strip()

            if not db_id or not name:
                messagebox.showwarning("경고", "DrugBank ID와 Name은 필수 입력 항목입니다.")
                return

            # CLASSIFICATION 정보
            kingdom = self.entries["CLASSIFICATION 정보_KINGDOM"].get().strip()
            superclass = self.entries["CLASSIFICATION 정보_SUPERCLASS"].get().strip()
            class_field = self.entries["CLASSIFICATION 정보_CLASS"].get().strip()
            subclass = self.entries["CLASSIFICATION 정보_SUBCLASS"].get().strip()

            if subclass and not (class_field and superclass and kingdom):
                messagebox.showwarning("경고", "Subclass를 입력하려면 Class, Superclass, Kingdom을 모두 입력해야 합니다.")
                return
            if class_field and not (superclass and kingdom):
                messagebox.showwarning("경고", "Class를 입력하려면 Superclass와 Kingdom을 모두 입력해야 합니다.")
                return
            if superclass and not kingdom:
                messagebox.showwarning("경고", "Superclass를 입력하려면 Kingdom을 입력해야 합니다.")
                return

            # TARGET 정보
            target_ids = []
            for entries in self.dynamic_sections["TARGET 정보"]:
                target_id = entries[0].get().strip()
                if target_id:
                    target_ids.append(target_id)

            if target_ids and not all(target_ids):
                messagebox.showwarning("경고", "Target ID는 비어 있을 수 없습니다.")
                return

            # ENZYME 정보
            enzyme_ids = []
            enzyme_actions = []
            for entries in self.dynamic_sections["ENZYME 정보"]:
                enzyme_id = entries[0].get().strip()
                enzyme_action = entries[1].get().strip()
                if enzyme_id or enzyme_action:
                    if not enzyme_id or not enzyme_action:
                        messagebox.showwarning("경고", "Enzyme ID와 Enzyme Action은 모두 입력해야 합니다.")
                        return
                    enzyme_ids.append(enzyme_id)
                    enzyme_actions.append(enzyme_action)

            # PATHWAY 정보
            pathways = []
            for entries in self.dynamic_sections["PATHWAY 정보"]:
                smpdb_id = entries[0].get().strip()
                uniprot_id = entries[1].get().strip()
                if smpdb_id or uniprot_id:
                    if not smpdb_id or not uniprot_id:
                        messagebox.showwarning("경고", "SMPDB ID와 UNIPROT ID는 모두 입력해야 합니다.")
                        return
                    pathways.append((smpdb_id, uniprot_id))

            # 데이터베이스 삽입
            self.db.execute_query(
                """
                INSERT INTO DRUG (DRUGBANK_ID, NAME, DESCRIPTION, CAS_NUMBER)
                VALUES (%s, %s, %s, %s)
                """,
                (db_id, name, description, cas_number)
            )

            if kingdom or superclass or class_field or subclass:
                self.db.execute_query(
                    """
                    INSERT INTO CLASSIFICATION (DRUGBANK_ID, KINGDOM, SUPERCLASS, CLASS, SUBCLASS)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (db_id, kingdom, superclass, class_field, subclass)
                )

            for target_id in target_ids:
                self.db.execute_query(
                    """
                    INSERT INTO DRUG_TARGET (DRUGBANK_ID, TARGET_ID)
                    VALUES (%s, %s)
                    """,
                    (db_id, target_id)
                )

            for enzyme_id, enzyme_action in zip(enzyme_ids, enzyme_actions):
                self.db.execute_query(
                    """
                    INSERT INTO DRUG_ENZYME_ACTION (DRUGBANK_ID, ENZYME_ID, ENZYME_ACTION)
                    VALUES (%s, %s, %s)
                    """,
                    (db_id, enzyme_id, enzyme_action)
                )

            for smpdb_id, uniprot_id in pathways:
                self.db.execute_query(
                    """
                    INSERT INTO DRUG_PATH_ASSOCIATION (DRUGBANK_ID, SMPDB_ID, UNIPROT_ID)
                    VALUES (%s, %s, %s)
                    """,
                    (db_id, smpdb_id, uniprot_id)
                )

            messagebox.showinfo("성공", "약물이 성공적으로 추가되었습니다.")
            self.refresh_callback()
            self.destroy()

        except IntegrityError as ie:
            self.db.connection.rollback()
            messagebox.showerror("추가 오류", f"약물 추가 중 오류가 발생했습니다.\n이미 존재하는 ID일 수 있습니다.\n오류 내용: {ie}")
        except Error as e:
            self.db.connection.rollback()
            messagebox.showerror("오류", f"오류: {e}")
