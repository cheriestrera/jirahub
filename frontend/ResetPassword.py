from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\ResetPassword_Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    533.0,
    94.0,
    anchor="nw",
    text="RESET PASSWORD",
    fill="#040404",
    font=("Inter Bold", 51 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    cursor="hand2"
)
button_1.place(
    x=434.0,
    y=86.0,
    width=72.0,
    height=72.0
)

canvas.create_text(
    434.0,
    185.0,
    anchor="nw",
    text="Email",
    fill="#040404",
    font=("Inter Bold", 27 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    720.0,
    259.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=459.0,
    y=227.0,
    width=522.0,
    height=63.0
)

canvas.create_text(
    434.0,
    310.0,
    anchor="nw",
    text="Old Password",
    fill="#040404",
    font=("Inter Bold", 27 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    720.0,
    384.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=459.0,
    y=352.0,
    width=522.0,
    height=63.0
)

canvas.create_text(
    434.0,
    435.0,
    anchor="nw",
    text="New Password",
    fill="#040404",
    font=("Inter Bold", 27 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    720.0,
    509.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=459.0,
    y=477.0,
    width=522.0,
    height=63.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    cursor="hand2"
)

button_2.place(
    x=627.0,
    y=576.0,
    width=185.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
