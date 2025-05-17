import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter.ttk import Combobox
from backend.CreateEmployeeFunction import CreateEmployeeFunction

sys.path.append(str(Path(__file__).parent.parent / "backend"))
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

backend = CreateEmployeeFunction()

window = Tk()
window.geometry("1440x706")
window.configure(bg="#FFB37F")

canvas = Canvas(
    window,
    bg="#FFB37F",
    height=706,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_text(
    516.0,
    128.0,
    anchor="nw",
    text="CREATE EMPLOYEE",
    fill="#040404",
    font=("Inter", 51, "bold")
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(565.0, 318.0, image=entry_image_1)
entry_1 = EntryWithPlaceholder(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    placeholder="First Name"
)
entry_1.place(x=423.0, y=298.0, width=284.0, height=39.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
canvas.create_image(719.5, 259.0, image=entry_image_2)
entry_2 = EntryWithPlaceholder(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    placeholder="Employee ID"
)
entry_2.place(x=423.0, y=239.0, width=593.0, height=39.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
canvas.create_image(719.5, 436.0, image=entry_image_3)
entry_3 = EntryWithPlaceholder(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    placeholder="Address"
)
entry_3.place(x=423.0, y=416.0, width=593.0, height=39.0)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
canvas.create_image(719.5, 495.0, image=entry_image_4)
entry_4 = EntryWithPlaceholder(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    placeholder="Phone Number"
)
entry_4.place(x=423.0, y=475.0, width=593.0, height=39.0)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
canvas.create_image(879.0, 318.0, image=entry_image_5)
entry_5 = EntryWithPlaceholder(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    placeholder="Last Name"
)
entry_5.place(x=742.0, y=298.0, width=274.0, height=39.0)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
canvas.create_image(719.5, 377.0, image=entry_image_6)

department_dropdown = Combobox(
    window,
    values=backend.get_all_departments(),
    font=("Inter", 13),
    foreground="#a9a9a9"
)

department_dropdown.place(x=425.0, y=357.0, width=591.0, height=39.0)
department_dropdown.set("Department")

def clear_form():
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
    entry_3.delete(0, "end")
    entry_4.delete(0, "end")
    entry_5.delete(0, "end")
    department_dropdown.set("Department")

def create_employee():
    employee_data = {
        'employee_id': entry_2.get(),
        'first_name': entry_1.get(),
        'last_name': entry_5.get(),
        'department': department_dropdown.get(),
        'address': entry_3.get(),
        'phone_number': entry_4.get()
    }
    success = backend.create_employee(employee_data)
    if success:
        clear_form()

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1_canvas = Canvas(window, width=72, height=72, bg="#FFB37F", highlightthickness=0)
button_1_canvas.place(x=417.0, y=123.0)
button_1_canvas.create_oval(0, 0, 72, 72, fill="#FFFFFF", outline="")
button_1_canvas.create_image(36, 36, image=button_image_1)

def button_1_click(event):
    print("button_1 clicked")

def on_enter(e):
    button_1_canvas.config(cursor="hand2")

def on_leave(e):
    button_1_canvas.config(cursor="")

button_1_canvas.bind("<Button-1>", button_1_click)
button_1_canvas.bind("<Enter>", on_enter)
button_1_canvas.bind("<Leave>", on_leave)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=create_employee,
    relief="flat"
)
button_2.place(x=936.0, y=534.0, width=86.0, height=48.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=clear_form,
    relief="flat"
)
button_3.place(x=831.0, y=534.0, width=90.0, height=48.0)

window.resizable(False, False)
window.mainloop()