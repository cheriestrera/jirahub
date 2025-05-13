from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\PasswordResetSuccessDialogBox_Assets")


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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    719.5,
    256.0,
    image=image_image_1
)

canvas.create_text(
    357.0,
    404.0,
    anchor="nw",
    text="YOUR PASSWORD HAS BEEN RESET!",
    fill="#040404",
    font=("Inter Medium", 40 * -1),
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
    x=666.0,
    y=486.0,
    width=108.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
