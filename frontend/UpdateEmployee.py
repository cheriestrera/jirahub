from pathlib import Path
from tkinter import messagebox

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
from tkinter.ttk import Combobox

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

class UpdateEmployee:
    # Simulated database as a class-level attribute
    simulated_database = {
        "12345": {
            "first_name": "John",
            "last_name": "Doe",
            "address": "123 Elm St",
            "phone_number": "555-1234",
            "department": "Sales"
        },
        "67890": {
            "first_name": "Jane",
            "last_name": "Smith",
            "address": "456 Elm St",
            "phone_number": "555-5678",
            "department": "Logistics"
        }
    }

    def __init__(self, master, scene_manager):
        self.master = master
        self.scene_manager = scene_manager

        print("Initializing UpdateEmployee...")  # Debugging

        # Add Employee ID first
        Label(master, text="Employee ID", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=150.0)
        self.entry_2 = Entry(master, font=("Inter", 12))
        self.entry_2.place(x=423.0, y=180.0, width=400.0, height=46.0)

        # Add SEARCH EMPLOYEE BUTTON
        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))  # Ensure the image file exists
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.verify_employee_id,
            relief="flat",
            cursor="hand2",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_4.image = button_image_4  # Keep a reference to avoid garbage collection
        self.button_4.place(
            x=840.0,
            y=180.0,
            width=182.0,
            height=48.0
        )
        print("Button 4 created and placed.")

        # Add First Name
        Label(master, text="First Name", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=250.0)
        self.entry_1 = Entry(master, font=("Inter", 12), state="disabled")
        self.entry_1.place(x=423.0, y=280.0, width=284.0, height=39.0)

        # Add Last Name
        Label(master, text="Last Name", font=("Inter", 12), bg="#FFB37F").place(x=742.0, y=250.0)
        self.entry_5 = Entry(master, font=("Inter", 12), state="disabled")
        self.entry_5.place(x=742.0, y=280.0, width=274.0, height=39.0)

        # Add Address
        Label(master, text="Address", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=320.0)
        self.entry_3 = Entry(master, font=("Inter", 12), state="disabled")
        self.entry_3.place(x=423.0, y=350.0, width=593.0, height=39.0)

        # Add Phone Number
        Label(master, text="Phone Number", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=400.0)
        self.entry_4 = Entry(master, font=("Inter", 12), state="disabled")
        self.entry_4.place(x=423.0, y=430.0, width=593.0, height=39.0)

        # Add Department
        Label(master, text="Department", font=("Inter", 12), bg="#FFB37F").place(x=423.0, y=480.0)
        self.department_dropdown = Combobox(
            master,
            values=["Secretariat", "Logistics", "Sales", "Labor", "Proprietor"],
            font=("Inter", 13),
            foreground="#a9a9a9",
            state="disabled"  # Disable dropdown by default
        )
        self.department_dropdown.place(x=423.0, y=510.0, width=593.0, height=39.0)
        self.department_dropdown.set("Department")  # Set default text

        # Add (<) BUTTON
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))  # Ensure the image file exists
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            cursor="hand2",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_1.image = button_image_1  # Keep a reference to avoid garbage collection
        self.button_1.place(
            x=417.00,  # Adjust the x-coordinate as needed
            y=50.0,  # Adjust the y-coordinate as needed
            width=100.0,  # Adjust the width as needed
            height=100  # Adjust the height as needed
        )
        print("Button 1 created and placed.")

        # Add Clear button
        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.clear_fields,  # Bind the clear_fields method
            relief="flat",
            cursor="hand2",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_3.image = button_image_3  # Keep a reference to avoid garbage collection
        self.button_3.place(
            x=740.0,
            y=580.0,
            width=90.0,
            height=48.0
        )

        # Add Update Employee Button
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.update_employee_data(self.entry_2.get()),  # Bind the update_employee_data method
            relief="flat",
            cursor="hand2",
            bg="#FFB37F",
            activebackground="#FFB37F"
        )
        self.button_2.image = button_image_2  # Keep a reference to avoid garbage collection
        self.button_2.place(
            x=840.0,
            y=580.0,
            width=182.0,
            height=48.0
        )

        print("Initializing UpdateEmployee...")  # Debugging

    def verify_employee_id(self):
        """Verify the Employee ID, populate fields, and allow updates to the record."""
        employee_id = self.entry_2.get()
        if not employee_id:
            messagebox.showerror("Error", "Please enter an Employee ID")
            return

        # Simulate checking the employee ID in the database
        employee_data = self.get_employee_data(employee_id)

        if employee_data:
            # Enable all other fields
            self.entry_1.config(state="normal")
            self.entry_3.config(state="normal")
            self.entry_4.config(state="normal")
            self.entry_5.config(state="normal")
            self.department_dropdown.config(state="readonly")

            # Populate the fields with employee data
            self.entry_1.delete(0, 'end')
            self.entry_1.insert(0, employee_data["first_name"])

            self.entry_5.delete(0, 'end')
            self.entry_5.insert(0, employee_data["last_name"])

            self.entry_3.delete(0, 'end')
            self.entry_3.insert(0, employee_data["address"])

            self.entry_4.delete(0, 'end')
            self.entry_4.insert(0, employee_data["phone_number"])

            self.department_dropdown.set(employee_data["department"])

            messagebox.showinfo("Success", "Employee found! Fields populated. Make changes and click 'Update Employee' to save.")

            # Add functionality to save changes
            self.button_2.config(command=lambda: self.update_employee_data(employee_id))
        else:
            messagebox.showerror("Error", "Employee not found. Please try again.")

    def get_employee_data(self, employee_id):
        """Retrieve employee data from the simulated database."""
        return UpdateEmployee.simulated_database.get(employee_id)

    def clear_fields(self):
        """Clear all text fields and reset the dropdown."""
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

    def update_employee_data(self, employee_id):
        """Update the employee data with the values from the text fields."""
        # Collect updated data from the text fields
        updated_data = {
            "first_name": self.entry_1.get(),
            "last_name": self.entry_5.get(),
            "address": self.entry_3.get(),
            "phone_number": self.entry_4.get(),
            "department": self.department_dropdown.get()
        }

        # Simulate updating the database
        success = self.save_employee_data(employee_id, updated_data)

        if success:
            messagebox.showinfo("Success", "Employee record updated successfully!")
            # Reset the button to call clear_fields after updating
            self.button_2.config(command=self.clear_fields)
            # Explicitly call clear_fields to clear the fields immediately
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Failed to update employee record. Please try again.")

    def save_employee_data(self, employee_id, updated_data):
        """Save updated employee data to the simulated database."""
        if employee_id in UpdateEmployee.simulated_database:
            UpdateEmployee.simulated_database[employee_id] = updated_data  # Update the record
            return True
        return False

#####################

window = Tk()

window.geometry("1440x706")
window.configure(bg = "#FFB37F")

canvas = Canvas(
    window,
    bg = "#FFB37F",
    height = 706,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    516.0,
    65.0,
    anchor="nw",
    text="UPDATE EMPLOYEE",
    fill="#040404",
    font=("Inter", 40, "bold")
)
app = UpdateEmployee(window, None)
window.resizable(False, False)
window.mainloop()