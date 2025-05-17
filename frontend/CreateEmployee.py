from pathlib import Path
from tkinter import Frame, Canvas, Entry, Button, PhotoImage, messagebox
from tkinter.ttk import Combobox
from backend.CreateEmployeeFunction import CreateEmployeeFunction

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\CreateEmployee_Assets")

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

class CreateEmployeeWindow(Frame):
    def __init__(self, master, scene_manager, user_data=None):
        super().__init__(master, bg="#FFB37F")
        self.scene_manager = scene_manager
        self.user_data = user_data
        self.backend = CreateEmployeeFunction()
        self.setup_ui()

    def setup_ui(self):
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
            128.0,
            anchor="nw",
            text="CREATE EMPLOYEE",
            fill="#040404",
            font=("Inter", 51, "bold")
        )

        # Load images (optional, remove if not using images)
        try:
            self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
            self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
            self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
            self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
            self.entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
            self.entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
            self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
            self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        except Exception:
            self.entry_image_1 = self.entry_image_2 = self.entry_image_3 = None
            self.entry_image_4 = self.entry_image_5 = self.entry_image_6 = None
            self.button_image_2 = self.button_image_3 = None

        # Entry fields with placeholders
        if self.entry_image_1:
            self.canvas.create_image(565.0, 318.0, image=self.entry_image_1)
        self.entry_1 = EntryWithPlaceholder(
            self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, placeholder="First Name"
        )
        self.entry_1.place(x=423.0, y=298.0, width=284.0, height=39.0)

        if self.entry_image_2:
            self.canvas.create_image(719.5, 259.0, image=self.entry_image_2)
        self.entry_2 = EntryWithPlaceholder(
            self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, placeholder="Employee ID"
        )
        self.entry_2.place(x=423.0, y=239.0, width=593.0, height=39.0)

        if self.entry_image_3:
            self.canvas.create_image(719.5, 436.0, image=self.entry_image_3)
        self.entry_3 = EntryWithPlaceholder(
            self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, placeholder="Address"
        )
        self.entry_3.place(x=423.0, y=416.0, width=593.0, height=39.0)

        if self.entry_image_4:
            self.canvas.create_image(719.5, 495.0, image=self.entry_image_4)
        self.entry_4 = EntryWithPlaceholder(
            self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, placeholder="Phone Number"
        )
        self.entry_4.place(x=423.0, y=475.0, width=593.0, height=39.0)

        if self.entry_image_5:
            self.canvas.create_image(879.0, 318.0, image=self.entry_image_5)
        self.entry_5 = EntryWithPlaceholder(
            self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, placeholder="Last Name"
        )
        self.entry_5.place(x=742.0, y=298.0, width=274.0, height=39.0)

        # Department dropdown
        if self.entry_image_6:
            self.canvas.create_image(719.5, 377.0, image=self.entry_image_6)
        self.department_dropdown = Combobox(
            self,
            values=self.backend.get_all_departments(),
            font=("Inter", 13),
            foreground="#a9a9a9"
        )
        self.department_dropdown.place(x=425.0, y=357.0, width=591.0, height=39.0)
        self.department_dropdown.set("Department")

        # Create Employee button
        self.create_button = Button(
            self,
            image=self.button_image_2 if self.button_image_2 else None,
            text="Create Employee" if not self.button_image_2 else "",
            borderwidth=0,
            highlightthickness=0,
            command=self.create_employee,
            relief="flat",
            bg="#FFB37F"
        )
        self.create_button.place(x=936.0, y=534.0, width=86.0, height=48.0)

        # Clear Form button
        self.clear_button = Button(
            self,
            image=self.button_image_3 if self.button_image_3 else None,
            text="Clear" if not self.button_image_3 else "",
            borderwidth=0,
            highlightthickness=0,
            command=self.clear_form,
            relief="flat",
            bg="#FFB37F"
        )
        self.clear_button.place(x=831.0, y=534.0, width=90.0, height=48.0)

    def clear_form(self):
        self.entry_1.delete(0, "end")
        self.entry_2.delete(0, "end")
        self.entry_3.delete(0, "end")
        self.entry_4.delete(0, "end")
        self.entry_5.delete(0, "end")
        self.department_dropdown.set("Department")
        # Reset placeholders
        self.entry_1._on_focus_out(None)
        self.entry_2._on_focus_out(None)
        self.entry_3._on_focus_out(None)
        self.entry_4._on_focus_out(None)
        self.entry_5._on_focus_out(None)

    def create_employee(self):
        employee_data = {
            'employee_id': self.entry_2.get() if self.entry_2.get() != "Employee ID" else "",
            'first_name': self.entry_1.get() if self.entry_1.get() != "First Name" else "",
            'last_name': self.entry_5.get() if self.entry_5.get() != "Last Name" else "",
            'department': self.department_dropdown.get(),
            'address': self.entry_3.get() if self.entry_3.get() != "Address" else "",
            'phone_number': self.entry_4.get() if self.entry_4.get() != "Phone Number" else ""
        }
        success = self.backend.create_employee(employee_data)
        if success:
            self.clear_form()