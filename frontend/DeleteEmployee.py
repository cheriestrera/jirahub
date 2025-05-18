from pathlib import Path
import threading
from tkinter import Frame, Canvas, Entry, Button, PhotoImage, messagebox, Label
import firebase_admin
from firebase_admin import credentials, firestore
from backend.DeleteEmployeeFunction import get_employee_data, delete_employee


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\DeleteEmployee_Assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="", color="#a9a9a9", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        self._on_focus_out(None)

    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self["fg"] = self.default_fg_color

    def _on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self["fg"] = self.placeholder_color

class DeleteEmployeeWindow(Frame):
    def __init__(self, master, scene_manager=None):
        super().__init__(master)
        self.scene_manager = scene_manager

        # Firestore init (only once)
        if not firebase_admin._apps:
            cred = credentials.Certificate(r"C:\Users\Marites\Downloads\CC15project\backend\serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        self.configure(bg="#FFB37F")
        self.place_widgets()

    def place_widgets(self):
        self.images = []
        self.canvas = Canvas(
            self,
            bg="#FFB37F",
            height=706,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            516.0,
            196.0,
            anchor="nw",
            text="DELETE EMPLOYEE",
            fill="#040404",
            font=("Inter", 51, "bold")
        )

        # Images
        def safe_photoimage(path):
            try:
                img = PhotoImage(file=relative_to_assets(path))
                self.images.append(img)
                return img
            except Exception:
                return None

        self.button_image_1 = safe_photoimage("button_1.png")
        self.button_image_2 = safe_photoimage("button_2.png")
        self.button_image_3 = safe_photoimage("button_3.png")
        self.entry_image_1 = safe_photoimage("entry_1.png")
        self.image_image_1 = safe_photoimage("image_1.png")
        self.image_image_2 = safe_photoimage("image_2.png")
        self.image_image_3 = safe_photoimage("image_3.png")
        self.image_image_4 = safe_photoimage("image_4.png")

        # Back Button (as a Button for easier command)
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_back,
            relief="flat",
            bg="#FFB37F",
            activebackground="#FFB37F",
            cursor="hand2"
        )
        self.button_1.place(x=417.0, y=191.0, width=72, height=72)

        # Entry for Employee ID
        self.entry_bg_1 = self.canvas.create_image(892.0, 320.0, image=self.entry_image_1)
        self.entry_1 = EntryWithPlaceholder(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            placeholder="Employee ID"
        )
        self.entry_1.place(x=770.0, y=300.0, width=244.0, height=38.0)

        # Info Labels
        self.label_fullname = Label(self, text="{Employee Full Name}", bg="#FFB37F", fg="#040404", font=("Inter", 17, "bold"))
        self.label_fullname.place(x=451.0, y=365.0)
        self.label_department = Label(self, text="{Employee Department}", bg="#FFB37F", fg="#737373", font=("Inter", 14, "bold"))
        self.label_department.place(x=451.0, y=389.0)
        self.label_email = Label(self, text="{Employee Email}", bg="#FFB37F", fg="#212121", font=("Inter", 12, "bold"))
        self.label_email.place(x=502.0, y=425.0)
        self.label_phone = Label(self, text="{Employee Phone Number}", bg="#FFB37F", fg="#212121", font=("Inter", 12, "bold"))
        self.label_phone.place(x=502.0, y=451.0)

        # Search Button
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_employee,
            relief="flat",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_3.place(x=764.0, y=354.0, width=182.0, height=48.0)

        # Delete Button
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.delete_employee_ui,
            relief="flat",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_2.place(x=764.0, y=413.0, width=182.0, height=48.0)

        # Decorative Images
        self.image_1 = self.canvas.create_image(580.0, 407.0, image=self.image_image_1)
        self.image_2 = self.canvas.create_image(582.0, 446.0, image=self.image_image_2)
        self.image_3 = self.canvas.create_image(481.0, 433.0, image=self.image_image_3)
        self.image_4 = self.canvas.create_image(481.0, 459.0, image=self.image_image_4)

    def go_back(self):
        if self.scene_manager:
            self.scene_manager.show_scene("dashboard")

    def search_employee(self):
        emp_id = self.entry_1.get().strip()
        if not emp_id or emp_id == self.entry_1.placeholder:
            messagebox.showwarning("Warning", "Please enter an Employee ID")
            return
        data = get_employee_data(emp_id)
        if data:
            self.label_fullname.config(text=f"{data.get('first_name', '')} {data.get('last_name', '')}")
            self.label_department.config(text=data.get('department', ''))
            self.label_email.config(text=data.get('address', ''))
            self.label_phone.config(text=data.get('phone_number', ''))
            messagebox.showinfo("Found", "Employee found. You can now delete.")
        else:
            self.label_fullname.config(text="{Employee Full Name}")
            self.label_department.config(text="{Employee Department}")
            self.label_email.config(text="{Employee Address}")
            self.label_phone.config(text="{Employee Phone Number}")
            messagebox.showerror("Error", "Employee not found.")
        threading.Thread(target=self.update_employee_labels, args=(data,), daemon=True).start()
        
    def update_employee_labels(self, data):
        self.label_fullname.config(text=f"{data.get('first_name', '')} {data.get('last_name', '')}")
        self.label_department.config(text=data.get('department', ''))
        self.label_email.config(text=data.get('address', ''))
        self.label_phone.config(text=data.get('phone_number', ''))

    def reset_employee_labels(self):
        self.label_fullname.config(text="{Employee Full Name}")
        self.label_department.config(text="{Employee Department}")
        self.label_email.config(text="{Employee Address}")
        self.label_phone.config(text="{Employee Phone Number}")

    def delete_employee_ui(self):
        emp_id = self.entry_1.get().strip()
        if not emp_id or emp_id == self.entry_1.placeholder:
            messagebox.showwarning("Warning", "Please enter an Employee ID")
            return
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this employee? This action cannot be undone.")
        if not confirm:
            return
        if delete_employee(emp_id):
            self.label_fullname.config(text="{Employee Full Name}")
            self.label_department.config(text="{Employee Department}")
            self.label_email.config(text="{Employee Address}")
            self.label_phone.config(text="{Employee Phone Number}")
            self.entry_1.delete(0, "end")
            messagebox.showinfo("Success", "Employee deleted successfully")
        else:
            messagebox.showerror("Error", "Employee ID not found")