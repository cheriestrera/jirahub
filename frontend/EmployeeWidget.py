from pathlib import Path
from tkinter import Frame, Canvas, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "EmployeeWidget_Assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class EmployeeWidget(Frame):
    def __init__(self, master, employee_data=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.employee_data = employee_data or {}

        self.configure(bg="#FFF4ED", width=327, height=215)
        self.pack_propagate(False)

        self.images = []
        self.place_widgets()

    def place_widgets(self):
        canvas = Canvas(
            self,
            bg="#FFF4ED",
            height=215,
            width=327,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        def safe_photoimage(path):
            try:
                img = PhotoImage(file=relative_to_assets(path))
                self.images.append(img)
                return img
            except Exception:
                return None

        image_image_1 = safe_photoimage("image_1.png")
        if image_image_1:
            canvas.create_image(164.0, 139.0, image=image_image_1)

        canvas.create_text(
            33.0,
            44.0,
            anchor="nw",
            text=f"{self.employee_data.get('first_name', '')} {self.employee_data.get('last_name', '')}",
            fill="#040404",
            font=("Inter", 17, "bold")
        )

        canvas.create_text(
            33.0,
            75.0,
            anchor="nw",
            text=self.employee_data.get("department", ""),
            fill="#737373",
            font=("Inter", 14, "bold")
        )

        canvas.create_text(
            84.0,
            118.0,
            anchor="nw",
            text=self.employee_data.get("address", ""),
            fill="#212121",
            font=("Inter", 12, "bold")
        )

        canvas.create_text(
            84.0,
            144.0,
            anchor="nw",
            text=self.employee_data.get("phone_number", ""),
            fill="#212121",
            font=("Inter", 12, "bold")
        )

        image_image_2 = safe_photoimage("image_2.png")
        if image_image_2:
            canvas.create_image(63.0, 126.0, image=image_image_2)

        image_image_3 = safe_photoimage("image_3.png")
        if image_image_3:
            canvas.create_image(63.0, 152.0, image=image_image_3)