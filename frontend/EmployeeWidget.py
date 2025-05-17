from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\EmployeeWidget_Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("352x215")
window.configure(bg = "#FFF4ED")


canvas = Canvas(
    window,
    bg = "#FFF4ED",
    height = 215,
    width = 352,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    165.0,
    146.0,
    image=image_image_1
)

canvas.create_text(
    34.0,
    65.0,
    anchor="nw",
    text="{{Full Name}}",
    fill="#040404",
    font=("Inter Bold", 17 * -1)
)

canvas.create_text(
    34.0,
    89.0,
    anchor="nw",
    text="{{Department}}",
    fill="#737373",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    85.0,
    125.0,
    anchor="nw",
    text="{{Email}}",
    fill="#212121",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    85.0,
    151.0,
    anchor="nw",
    text="{{Phone Number}}",
    fill="#212121",
    font=("Inter Bold", 12 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    64.0,
    133.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    64.0,
    159.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
