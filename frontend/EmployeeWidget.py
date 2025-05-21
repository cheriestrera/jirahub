from pathlib import Path
from tkinter import Frame, Canvas, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "EmployeeWidget_Assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class EmployeeWidget(Frame):
    def __init__(self, master, employee_data=None, *args, **kwargs):
        super().__init__(master, bg="#FFF4ED", *args, **kwargs)
        self.employee_data = employee_data or {}
        self.images = []
        self.width = 327
        self.height = 215
        self.radius = 20  
        self.border_color = "#FFB37F"
        self.bg_color = "#FFF4ED"
        self.place_widgets()

    def place_widgets(self):
        canvas = Canvas(
            self,
            width=self.width,
            height=self.height,
            bg=self.bg_color,
            highlightthickness=0,
            bd=0,
            relief="flat"
        )
        canvas.pack(fill="both", expand=True)

        self._draw_rounded_rect(
            canvas,
            5, 5, self.width-5, self.height-5,
            self.radius,
            outline=self.border_color,
            fill=self.bg_color,
            width=3
        )

        def safe_photoimage(path):
            try:
                img = PhotoImage(file=relative_to_assets(path))
                self.images.append(img)
                return img
            except Exception:
                return None

        image_image_1 = safe_photoimage("image_1.png")
        if image_image_1:
            canvas.create_image(150.0, 120.0, image=image_image_1)

        canvas.create_text(
            24.0,
            25.0,
            anchor="nw",
            text=f"{self.employee_data.get('first_name', '')} {self.employee_data.get('last_name', '')}",
            fill="#040404",
            font=("Inter", 17, "bold")
        )

        canvas.create_text(
            24.0,
            56.0,
            anchor="nw",
            text=self.employee_data.get("department", ""),
            fill="#737373",
            font=("Inter", 14, "bold")
        )

        canvas.create_text(
            70.0,
            99.0,
            anchor="nw",
            text=self.employee_data.get("address", ""),
            fill="#212121",
            font=("Inter", 12, "bold")
        )

        canvas.create_text(
            70.0,
            125.0,
            anchor="nw",
            text=self.employee_data.get("phone_number", ""),
            fill="#212121",
            font=("Inter", 12, "bold")
        )

        image_image_2 = safe_photoimage("image_2.png")
        if image_image_2:
            canvas.create_image(49.0, 107.0, image=image_image_2)

        image_image_3 = safe_photoimage("image_3.png")
        if image_image_3:
            canvas.create_image(49.0, 133.0, image=image_image_3)

    def _draw_rounded_rect(self, canvas, x1, y1, x2, y2, r, outline, fill, width=1):
        points = [
            x1+r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y1+r,
            x1, y1
        ]
        canvas.create_polygon(points, smooth=True, outline=outline, fill=fill, width=width)