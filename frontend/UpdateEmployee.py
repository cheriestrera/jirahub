import firebase_admin
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, Frame, messagebox
from tkinter.ttk import Combobox
from firebase_admin import credentials, firestore
from backend.UpdateEmployeeFunction import UpdateEmployeeService

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\UpdateEmployee_Assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", font=("Inter", 12), *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.default_fg_color = self["fg"]
        self.font = font
        self["font"] = font
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self["fg"] = self.default_fg_color

    def _add_placeholder(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self["fg"] = self.placeholder_color

class UpdateEmployeeWindow(Frame):
    def __init__(self, master, scene_manager=None):
        super().__init__(master)
        self.master = master
        self.scene_manager = scene_manager

        # Initialize Firestore and backend service
        if not firebase_admin._apps:
            cred = credentials.Certificate(r"C:\Users\Marites\Downloads\CC15project\backend\serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.update_service = UpdateEmployeeService(self.db)

        self.configure(bg="#FFB37F")
        self.place_widgets()

    def place_widgets(self):
        # Canvas and title
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
            65.0,
            anchor="nw",
            text="UPDATE EMPLOYEE",
            fill="#040404",
            font=("Inter", 40, "bold")
        )

        # Employee ID
        Label(self, text="Employee ID", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=150.0)
        self.entry_2 = Entry(self, font=("Inter", 12))
        self.entry_2.place(x=423.0, y=180.0, width=400.0, height=46.0)

        # Search Employee Button
        try:
            button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        except Exception:
            button_image_4 = None
        self.button_4 = Button(
            self,
            image=button_image_4,
            text="Search" if not button_image_4 else "",
            borderwidth=0,
            highlightthickness=0,
            command=self.verify_employee_id,
            relief="flat",
            cursor="hand2",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_4.image = button_image_4
        self.button_4.place(x=840.0, y=180.0, width=182.0, height=48.0)

        # First Name
        Label(self, text="First Name", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=250.0)
        self.entry_1 = Entry(self, font=("Inter", 12), state="disabled")
        self.entry_1.place(x=423.0, y=280.0, width=284.0, height=39.0)

        # Last Name
        Label(self, text="Last Name", font=("Inter", 12), bg="#FFB37F").place(x=742.0, y=250.0)
        self.entry_5 = Entry(self, font=("Inter", 12), state="disabled")
        self.entry_5.place(x=742.0, y=280.0, width=274.0, height=39.0)

        # Address
        Label(self, text="Address", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=320.0)
        self.entry_3 = Entry(self, font=("Inter", 12), state="disabled")
        self.entry_3.place(x=423.0, y=350.0, width=593.0, height=39.0)

        # Phone Number
        Label(self, text="Phone Number", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=400.0)
        self.entry_4 = Entry(self, font=("Inter", 12), state="disabled")
        self.entry_4.place(x=423.0, y=430.0, width=593.0, height=39.0)

        # Department
        Label(self, text="Department", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=480.0)
        self.department_dropdown = Combobox(
            self,
            values=["Secretariat", "Logistics", "Sales", "Labor", "Proprietor"],
            font=("Inter", 13),
            foreground="#a9a9a9",
            state="disabled"
        )
        self.department_dropdown.place(x=423.0, y=510.0, width=593.0, height=39.0)
        self.department_dropdown.set("Department")

        # Back Button
        try:
            button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        except Exception:
            button_image_1 = None
        self.button_1 = Button(
            self,
            image=button_image_1,
            text="<" if not button_image_1 else "",
            borderwidth=0,
            highlightthickness=0,
            command=self.go_back,
            relief="flat",
            cursor="hand2",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_1.image = button_image_1
        self.button_1.place(x=417.0, y=50.0, width=100.0, height=100)

        # Clear Button
        try:
            button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        except Exception:
            button_image_3 = None
        self.button_3 = Button(
            self,
            image=button_image_3,
            text="Clear" if not button_image_3 else "",
            borderwidth=0,
            highlightthickness=0,
            command=self.clear_fields,
            relief="flat",
            cursor="hand2",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_3.image = button_image_3
        self.button_3.place(x=740.0, y=580.0, width=90.0, height=48.0)

        # Update Employee Button
        try:
            button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        except Exception:
            button_image_2 = None
        self.button_2 = Button(
            self,
            image=button_image_2,
            text="Update" if not button_image_2 else "",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.update_employee_data(self.entry_2.get()),
            relief="flat",
            cursor="hand2",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_2.image = button_image_2
        self.button_2.place(x=840.0, y=580.0, width=182.0, height=48.0)

    def verify_employee_id(self):
        employee_id = self.entry_2.get()
        if not employee_id:
            messagebox.showerror("Error", "Please enter an Employee ID")
            return

        employee_ref = self.db.collection('employees').document(employee_id)
        doc = employee_ref.get()
        if doc.exists:
            employee_data = doc.to_dict()
            self.entry_1.config(state="normal")
            self.entry_3.config(state="normal")
            self.entry_4.config(state="normal")
            self.entry_5.config(state="normal")
            self.department_dropdown.config(state="readonly")

            self.entry_1.delete(0, 'end')
            self.entry_1.insert(0, employee_data.get("first_name", ""))

            self.entry_5.delete(0, 'end')
            self.entry_5.insert(0, employee_data.get("last_name", ""))

            self.entry_3.delete(0, 'end')
            self.entry_3.insert(0, employee_data.get("address", ""))

            self.entry_4.delete(0, 'end')
            self.entry_4.insert(0, employee_data.get("phone_number", ""))

            self.department_dropdown.set(employee_data.get("department", "Department"))

            messagebox.showinfo("Success", "Employee found! Fields populated. Make changes and click 'Update Employee' to save.")
            self.button_2.config(command=lambda: self.update_employee_data(employee_id))
        else:
            messagebox.showerror("Error", "Employee not found. Please try again.")

    def clear_fields(self):
        self.entry_1.delete(0, 'end')
        self.entry_2.delete(0, 'end')
        self.entry_3.delete(0, 'end')
        self.entry_4.delete(0, 'end')
        self.entry_5.delete(0, 'end')
        self.department_dropdown.set("Department")
        self.department_dropdown.config(state="disabled")
        self.entry_1.config(state="disabled")
        self.entry_3.config(state="disabled")
        self.entry_4.config(state="disabled")
        self.entry_5.config(state="disabled")

    def go_back(self):
        if self.scene_manager:
            self.scene_manager.show_scene("dashboard")

    def update_employee_data(self, employee_id):
        updated_data = {
            "first_name": self.entry_1.get(),
            "last_name": self.entry_5.get(),
            "address": self.entry_3.get(),
            "phone_number": self.entry_4.get(),
            "department": self.department_dropdown.get()
        }
        success = self.update_service.update_employee(employee_id, updated_data)
        if success:
            messagebox.showinfo("Success", "Employee record updated successfully!")
            self.button_2.config(command=self.clear_fields)
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Failed to update employee record. Please try again.")

    def verify_employee_id(self):
        employee_id = self.entry_2.get()
        if not employee_id:
            messagebox.showerror("Error", "Please enter an Employee ID")
            return

        employee_ref = self.db.collection('employees').document(employee_id)
        doc = employee_ref.get()
        if doc.exists:
            employee_data = doc.to_dict()
            self.entry_1.config(state="normal")
            self.entry_3.config(state="normal")
            self.entry_4.config(state="normal")
            self.entry_5.config(state="normal")
            self.department_dropdown.config(state="readonly")

            self.entry_1.delete(0, 'end')
            self.entry_1.insert(0, employee_data.get("first_name", ""))

            self.entry_5.delete(0, 'end')
            self.entry_5.insert(0, employee_data.get("last_name", ""))

            self.entry_3.delete(0, 'end')
            self.entry_3.insert(0, employee_data.get("address", ""))

            self.entry_4.delete(0, 'end')
            self.entry_4.insert(0, employee_data.get("phone_number", ""))

            self.department_dropdown.set(employee_data.get("department", "Department"))

            messagebox.showinfo("Success", "Employee found! Fields populated. Make changes and click 'Update Employee' to save.")
            self.button_2.config(command=lambda: self.update_employee_data(employee_id))
        else:
            messagebox.showerror("Error", "Employee not found. Please try again.")

if __name__ == "__main__":
    root = Tk()
    root.geometry("1440x706")
    root.configure(bg="#FFB37F")
    app = UpdateEmployeeWindow(root)
    app.pack(fill="both", expand=True)
    root.resizable(False, False)
    root.mainloop()