# edit_drug.py
import tkinter as tk
from tkinter import ttk, messagebox
from mysql.connector import Error


class EditDrug(tk.Toplevel):
    def __init__(self, master, db, drug_id, refresh_callback):
        super().__init__(master)
        self.db = db
        self.drug_id = drug_id
        self.refresh_callback = refresh_callback
        self.title(f"약물 정보 수정 - {drug_id}")
        self.resizable(True, True)
        self.set_window_size()
        self.create_widgets()
        self.load_data()

    def set_window_size(self):
        self.update_idletasks()
        main_width = self.master.winfo_width()
        main_height = self.master.winfo_height()

        new_width = int(main_width * 0.8)
        new_height = int(main_height * 0.8)

        main_x = self.master.winfo_x()
        main_y = self.master.winfo_y()

        new_x = main_x + (main_width - new_width) // 2
        new_y = main_y + (main_height - new_height) // 2

        self.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")

    def create_widgets(self):
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a Canvas with Scrollbars
        canvas = tk.Canvas(main_frame)
        v_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        h_scrollbar = ttk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar.pack(side="bottom", fill="x")

        # Define sections
        self.sections = {
            "DRUG 정보": ["DrugBank ID", "Name", "Description", "CAS Number"],
            "CLASSIFICATION 정보": ["KINGDOM", "SUPERCLASS", "CLASS", "SUBCLASS"],
            "TARGET 정보": ["Target ID"],
            "ENZYME 정보": ["Enzyme ID", "Enzyme Action"],
            "PATHWAY 정보": ["SMPDB ID", "UNIPROT ID"]
        }

        # Initialize dictionaries to hold Entry widgets and dynamic section frames
        self.entries = {}
        self.dynamic_section_frames = {}
        self.dynamic_entries = {
            "TARGET 정보": [],
            "ENZYME 정보": [],
            "PATHWAY 정보": []
        }

        # Create widgets for each section
        for section, fields in self.sections.items():
            if section in self.dynamic_entries:
                # Create dynamic section
                frame = tk.LabelFrame(scrollable_frame, text=section)
                frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                # Create a sub-frame to hold dynamic rows
                rows_frame = tk.Frame(frame)
                rows_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

                # Add button to add new rows
                add_button = tk.Button(frame, text="+", command=lambda s=section: self.add_dynamic_row(s))
                add_button.pack(anchor="ne", padx=5, pady=5)

                # Store reference to rows_frame
                self.dynamic_section_frames[section] = rows_frame
            else:
                # Create single-entry section
                frame = tk.LabelFrame(scrollable_frame, text=section)
                frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                for idx, field in enumerate(fields):
                    label = tk.Label(frame, text=f"{field}:")
                    label.grid(row=idx, column=0, sticky="e", padx=5, pady=2)
                    entry = tk.Entry(frame, width=50)
                    entry.grid(row=idx, column=1, padx=5, pady=2)
                    if field == "DrugBank ID":
                        entry.config(state='readonly')  # Assuming DrugBank ID is not editable
                    self.entries[f"{section}_{field}"] = entry

        # Register button
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        register_button = tk.Button(button_frame, text="등록", command=self.submit)
        register_button.pack()

    def add_dynamic_row(self, section, initial_values=None):
        fields = self.sections[section]
        rows_frame = self.dynamic_section_frames[section]

        row_frame = tk.Frame(rows_frame)
        row_frame.pack(fill=tk.X, pady=2)

        entries = []
        for idx, field in enumerate(fields):
            label = tk.Label(row_frame, text=f"{field}:")
            label.grid(row=0, column=idx*2, padx=5, pady=5, sticky='e')
            entry = tk.Entry(row_frame, width=30)
            entry.grid(row=0, column=idx*2 + 1, padx=5, pady=5, sticky='w')
            if initial_values and idx < len(initial_values):
                entry.insert(0, initial_values[idx] if initial_values[idx] is not None else "")
            entries.append(entry)

        # Remove button
        remove_button = tk.Button(row_frame, text="-", command=lambda s=section, rf=row_frame: self.remove_dynamic_row(s, rf))
        remove_button.grid(row=0, column=len(fields)*2, padx=5, pady=5)

        # Add to dynamic_entries
        self.dynamic_entries[section].append(entries)

    def remove_dynamic_row(self, section, row_frame):
        # Remove the row frame
        row_frame.destroy()
        # Remove from dynamic_entries
        for entries in self.dynamic_entries[section]:
            if all(not entry.winfo_exists() for entry in entries):
                self.dynamic_entries[section].remove(entries)
                break

    def load_data(self):
        try:
            # DRUG 정보 로드
            drug_query = "SELECT * FROM DRUG WHERE DRUGBANK_ID = %s"
            drug_data = self.db.execute_query(drug_query, (self.drug_id,), fetch=True)
            if drug_data:
                for field in self.sections["DRUG 정보"]:
                    entry_key = f"DRUG 정보_{field}"
                    if entry_key in self.entries:
                        entry = self.entries[entry_key]
                        if isinstance(entry, tk.Entry):
                            entry.config(state='normal')
                            entry.delete(0, tk.END)
                            # 데이터가 None일 경우 빈 문자열로 대체
                            value = drug_data.get(field.upper().replace(" ", "_"), "") or ""
                            entry.insert(0, str(value))
                            if field == "DrugBank ID":
                                entry.config(state='readonly')
            else:
                messagebox.showwarning("경고", f"DrugBank ID {self.drug_id}에 해당하는 약물이 없습니다.")
                self.destroy()
                return

            # CLASSIFICATION 정보 로드
            classification_query = "SELECT * FROM CLASSIFICATION WHERE DRUGBANK_ID = %s"
            classification_data = self.db.execute_query(classification_query, (self.drug_id,), fetch=True)
            if classification_data:
                for field in self.sections["CLASSIFICATION 정보"]:
                    entry_key = f"CLASSIFICATION 정보_{field}"
                    if entry_key in self.entries:
                        entry = self.entries[entry_key]
                        if isinstance(entry, tk.Entry):
                            entry.config(state='normal')
                            entry.delete(0, tk.END)
                            # 데이터가 None일 경우 빈 문자열로 대체
                            value = classification_data.get(field.upper(), "") or ""
                            entry.insert(0, str(value))
            else:
                # CLASSIFICATION 데이터가 없을 경우 빈 문자열로 설정
                for field in self.sections["CLASSIFICATION 정보"]:
                    entry_key = f"CLASSIFICATION 정보_{field}"
                    if entry_key in self.entries:
                        entry = self.entries[entry_key]
                        if isinstance(entry, tk.Entry):
                            entry.config(state='normal')
                            entry.delete(0, tk.END)
                            entry.insert(0, "")

            # TARGET 정보 로드
            target_query = """
                SELECT DRUG_TARGET.TARGET_ID
                FROM DRUG_TARGET
                WHERE DRUG_TARGET.DRUGBANK_ID = %s
            """
            targets = self.db.execute_query(target_query, (self.drug_id,), fetchall=True)
            # 기존 동적 입력 행 삭제
            self.clear_dynamic_entries("TARGET 정보")
            for target in targets:
                target_id = target.get("TARGET_ID", "") or ""
                if target_id:
                    self.add_dynamic_row("TARGET 정보", initial_values=[str(target_id)])

            # ENZYME 정보 로드
            enzyme_query = """
                SELECT DRUG_ENZYME_ACTION.ENZYME_ID, DRUG_ENZYME_ACTION.ENZYME_ACTION
                FROM DRUG_ENZYME_ACTION
                WHERE DRUG_ENZYME_ACTION.DRUGBANK_ID = %s
            """
            enzymes = self.db.execute_query(enzyme_query, (self.drug_id,), fetchall=True)
            # 기존 동적 입력 행 삭제
            self.clear_dynamic_entries("ENZYME 정보")
            for enzyme in enzymes:
                enzyme_id = enzyme.get("ENZYME_ID", "") or ""
                enzyme_action = enzyme.get("ENZYME_ACTION", "") or ""
                if enzyme_id and enzyme_action:
                    self.add_dynamic_row("ENZYME 정보", initial_values=[str(enzyme_id), str(enzyme_action)])

            # PATHWAY 정보 로드
            pathway_query = """
                SELECT DRUG_PATH_ASSOCIATION.SMPDB_ID, DRUG_PATH_ASSOCIATION.UNIPROT_ID
                FROM DRUG_PATH_ASSOCIATION
                WHERE DRUG_PATH_ASSOCIATION.DRUGBANK_ID = %s
            """
            pathways = self.db.execute_query(pathway_query, (self.drug_id,), fetchall=True)
            # 기존 동적 입력 행 삭제
            self.clear_dynamic_entries("PATHWAY 정보")
            for pathway in pathways:
                smpdb_id = pathway.get("SMPDB_ID", "") or ""
                uniprot_id = pathway.get("UNIPROT_ID", "") or ""
                if smpdb_id and uniprot_id:
                    self.add_dynamic_row("PATHWAY 정보", initial_values=[str(smpdb_id), str(uniprot_id)])

        except Error as e:
            messagebox.showerror("오류", f"데이터를 로드하는 중 오류가 발생했습니다.\n오류 내용: {e}")
            self.destroy()
        except Exception as ex:
            messagebox.showerror("오류", f"예상치 못한 오류가 발생했습니다.\n오류 내용: {ex}")
            self.destroy()

    def clear_dynamic_entries(self, section):
        for entries in self.dynamic_entries[section]:
            # Destroy each row's widgets
            for entry in entries:
                entry.master.destroy()
        # Clear the list
        self.dynamic_entries[section].clear()

    def submit(self):
        try:
            cursor = self.db.connection.cursor()

            # DRUG 정보 업데이트
            name = self.entries["DRUG 정보_Name"].get().strip()
            description = self.entries["DRUG 정보_Description"].get().strip()
            cas_number = self.entries["DRUG 정보_CAS Number"].get().strip()

            if not name:
                messagebox.showwarning("경고", "Name은 필수 입력 항목입니다.")
                return

            # CLASSIFICATION 정보 업데이트 또는 삽입
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

            # DRUG 테이블 업데이트
            update_drug_query = """
                UPDATE DRUG
                SET NAME = %s, DESCRIPTION = %s, CAS_NUMBER = %s
                WHERE DRUGBANK_ID = %s
            """
            cursor.execute(update_drug_query, (name, description, cas_number, self.drug_id))

            # CLASSIFICATION 테이블 업데이트 또는 삽입
            if kingdom or superclass or class_field or subclass:
                # Check if classification exists
                check_class_query = "SELECT COUNT(*) FROM CLASSIFICATION WHERE DRUGBANK_ID = %s"
                cursor.execute(check_class_query, (self.drug_id,))
                exists = cursor.fetchone()[0]

                if exists:
                    # Update existing classification
                    update_class_query = """
                        UPDATE CLASSIFICATION
                        SET KINGDOM = %s, SUPERCLASS = %s, CLASS = %s, SUBCLASS = %s
                        WHERE DRUGBANK_ID = %s
                    """
                    cursor.execute(update_class_query, (kingdom, superclass, class_field, subclass, self.drug_id))

                else:
                    # Insert new classification
                    insert_class_query = """
                        INSERT INTO CLASSIFICATION (DRUGBANK_ID, KINGDOM, SUPERCLASS, CLASS, SUBCLASS)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_class_query, (self.drug_id, kingdom, superclass, class_field, subclass))


            # TARGET 정보 업데이트
            # Delete existing entries
            delete_target_query = "DELETE FROM DRUG_TARGET WHERE DRUGBANK_ID = %s"
            cursor.execute(delete_target_query, (self.drug_id,))

            # Insert new entries
            target_entries = self.dynamic_entries["TARGET 정보"]
            for entries in target_entries:
                target_id = entries[0].get().strip()
                if target_id:
                    insert_target_query = "INSERT INTO DRUG_TARGET (DRUGBANK_ID, TARGET_ID) VALUES (%s, %s)"
                    cursor.execute(insert_target_query, (self.drug_id, target_id))

            # ENZYME 정보 업데이트
            # Delete existing entries
            delete_enzyme_query = "DELETE FROM DRUG_ENZYME_ACTION WHERE DRUGBANK_ID = %s"
            cursor.execute(delete_enzyme_query, (self.drug_id,))

            # Insert new entries
            enzyme_entries = self.dynamic_entries["ENZYME 정보"]
            for entries in enzyme_entries:
                enzyme_id = entries[0].get().strip()
                enzyme_action = entries[1].get().strip()
                if enzyme_id and enzyme_action:
                    insert_enzyme_query = "INSERT INTO DRUG_ENZYME_ACTION (DRUGBANK_ID, ENZYME_ID, ENZYME_ACTION) VALUES (%s, %s, %s)"
                    cursor.execute(insert_enzyme_query, (self.drug_id, enzyme_id, enzyme_action))

            # PATHWAY 정보 업데이트
            # Delete existing entries
            delete_pathway_query = "DELETE FROM DRUG_PATH_ASSOCIATION WHERE DRUGBANK_ID = %s"
            cursor.execute(delete_pathway_query, (self.drug_id,))

            # Insert new entries
            pathway_entries = self.dynamic_entries["PATHWAY 정보"]
            for entries in pathway_entries:
                smpdb_id = entries[0].get().strip()
                uniprot_id = entries[1].get().strip()
                if smpdb_id and uniprot_id:
                    insert_pathway_query = "INSERT INTO DRUG_PATH_ASSOCIATION (DRUGBANK_ID, SMPDB_ID, UNIPROT_ID) VALUES (%s, %s, %s)"
                    cursor.execute(insert_pathway_query, (self.drug_id, smpdb_id, uniprot_id))

            # Commit
            self.db.connection.commit()
            cursor.close()

            messagebox.showinfo("성공", "약물 정보 성공적으로 갱신")
            self.refresh_callback()
            self.destroy()

        except Error as e:
            self.db.connection.rollback()
            messagebox.showerror("오류", f"데이터를 갱신하는 중 오류가 발생.\n오류 내용: {e}")
        except Exception as ex:
            self.db.connection.rollback()
            messagebox.showerror("오류", f"예상치 못한 오류가 발생.\n오류 내용: {ex}")

