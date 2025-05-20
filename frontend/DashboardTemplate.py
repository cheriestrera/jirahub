import tkinter as tk
from tkinter import Frame, Canvas, Button, PhotoImage
from pathlib import Path
from frontend.EmployeeWidget import EmployeeWidget
from backend.DashboardWindowFunction import (
    get_all_employees, get_employees_by_department
)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "DashboardTemplate_Assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DashboardTemplate(Frame):
    def __init__(self, master, scene_manager=None, user_data=None):
        super().__init__(master)
        self.scene_manager = scene_manager
        self.user_data = user_data
        self.images = []
        self.setup_ui()

    def setup_ui(self):
        self.master.geometry("1440x706")
        self.master.title("JIRAH ENTERPRISES - Employee Management")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=706,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill="both", expand=True)

        # Load and store all images
        self.load_images()
        
        # Create UI elements
        self.create_text_elements()
        self.create_buttons()

        # --- Scrollable Employees Area ---
        self.employees_canvas = tk.Canvas(self, bg="#FFF4ED", highlightthickness=0)
        self.employees_canvas.place(x=265, y=250, width=1100, height=400)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.employees_canvas.yview)
        self.scrollbar.place(x=1365, y=250, height=400)

        self.employees_frame = tk.Frame(self.employees_canvas, bg="#FFF4ED")
        self.employees_frame.bind(
            "<Configure>",
            lambda e: self.employees_canvas.configure(
                scrollregion=self.employees_canvas.bbox("all")
            )
        )

        self.employees_canvas.create_window((0, 0), window=self.employees_frame, anchor="nw")
        self.employees_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Mousewheel scrolling support
        def _on_mousewheel(event):
            self.employees_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.employees_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.view_all_employees()
        
        # Set welcome message with actual admin name if available
        if self.user_data and 'name' in self.user_data:
            welcome_text = f"WELCOME {self.user_data['name']}!"
        else:
            welcome_text = "WELCOME ADMIN!"
            
        self.canvas.create_text(
            903.0, 22.0,
            anchor="nw",
            text=welcome_text,
            fill="#040404",
            font=("Inter Bold", 30 * -1)
        )

    def load_images(self):
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.images.append(self.image_image_1)
        self.canvas.create_image(112.0, 401.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.images.append(self.image_image_2)
        self.canvas.create_image(720.0, 40.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.images.append(self.image_image_3)
        self.canvas.create_image(1424.0, 552.0, image=self.image_image_3)

    def create_text_elements(self):
        self.canvas.create_text(
            265.0, 198.0,
            anchor="nw",
            text="ALL EMPLOYEES",
            fill="#040404",
            font=("Inter Bold", 30 * -1)
        )

        self.canvas.create_text(
            37.0, 23.0,
            anchor="nw",
            text="JIRAH ENTERPRISES",
            fill="#040404",
            font=("Inter Bold", 30 * -1)
        )

        self.canvas.create_text(
            37.0, 198.0,
            anchor="nw",
            text="🏢 COMPANY",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            37.0, 284.0,
            anchor="nw",
            text="🏢 DEPARTMENT",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

    def create_buttons(self):
        # DELETE EMPLOYEE BUTTON
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.images.append(self.button_image_1)
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.delete_employees,
            relief="flat",
            cursor="hand2"
        )
        self.button_1.place(x=265.0, y=113.0, width=247.0, height=42.0)

        # UPDATE EMPLOYEE BUTTON
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.images.append(self.button_image_2)
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.update_employees,
            relief="flat",
            cursor="hand2"
        )
        self.button_2.place(x=534.0, y=113.0, width=247.0, height=42.0)

        # CREATE EMPLOYEE BUTTON
        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.images.append(self.button_image_3)
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.create_employees,
            relief="flat",
            cursor="hand2"
        )
        self.button_3.place(x=37.0, y=113.0, width=161.151, height=41.804)

        # LOGOUT BUTTON
        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.images.append(self.button_image_4)
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_logout,
            relief="flat",
            cursor="hand2"
        )
        self.button_4.place(x=37.0, y=623.0, width=161.0, height=45.0)  

        # ALL EMPLOYEES VIEW
        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.images.append(self.button_image_5)
        self.button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.view_all_employees,
            relief="flat",
            cursor="hand2"
        )
        self.button_5.place(x=37.0, y=228.0, width=141.0, height=24.0)

        # SECRETARIAT VIEW
        self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.images.append(self.button_image_6)
        self.button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.view_secretariat,
            relief="flat",
            cursor="hand2"
        )
        self.button_6.place(x=30.0, y=312.0, width=121.0, height=28.0)

        # LOGISTICS VIEW
        self.button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        self.images.append(self.button_image_7)
        self.button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.view_logistics,
            relief="flat",
            cursor="hand2"
        )
        self.button_7.place(x=37.0, y=346.0, width=85.0, height=24.0)

        # SALES VIEW
        self.button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
        self.images.append(self.button_image_8)
        self.button_8 = Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.view_sales,
            relief="flat",
            cursor="hand2"
        )
        self.button_8.place(x=37.0, y=377.0, width=51.0, height=24.0)

        # LABOR VIEW
        self.button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
        self.images.append(self.button_image_9)
        self.button_9 = Button(
            self,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.view_labor,
            relief="flat",
            cursor="hand2"
        )
        self.button_9.place(x=37.0, y=405.0, width=55.0, height=24.0)

        # PROPRIETOR VIEW
        self.button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
        self.images.append(self.button_image_10)
        self.button_10 = Button(
            self,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=self.view_proprietor,
            relief="flat",
            cursor="hand2"
        )
        self.button_10.place(x=37.0, y=432.0, width=95.0, height=24.0)

    def handle_logout(self):
        """Handle logout action"""
        if self.scene_manager:
            self.scene_manager.show_scene("login")
        else:
            self.master.destroy() 

    def update_employees(self):
        self.scene_manager.show_scene("update_employee")
    
    def delete_employees(self):
        self.scene_manager.show_scene("delete_employee")

    def create_employees(self):
        self.scene_manager.show_scene("create_employee")

    def view_all_employees(self):
        """Fetch all employees and display them as widgets in a row/grid."""
        # Clear previous widgets
        for widget in self.employees_frame.winfo_children():
            widget.destroy()

        employees = get_all_employees()  # This should return a list of dicts
        if not employees:
            tk.Label(self.employees_frame, text="No employees found.", bg="#FFF4ED").pack()
            return

        # Arrange in a grid, e.g., 3 per row
        columns = 3
        for idx, emp in enumerate(employees):
            row = idx // columns
            col = idx % columns
            widget = EmployeeWidget(self.employees_frame, employee_data=emp)
            widget.grid(row=row, column=col, padx=20, pady=20)

    def view_department(self, department_name):
        """Fetch and display employees by department."""
        # Clear previous widgets
        for widget in self.employees_frame.winfo_children():
            widget.destroy()
        employees = get_employees_by_department(department_name)
        print(f"Viewing department: {department_name}, found: {len(employees)} employees")
        if not employees:
            tk.Label(self.employees_frame, text=f"No employees found in {department_name}.", bg="#FFF4ED").pack()
            return
        columns = 3
        for idx, emp in enumerate(employees):
            row = idx // columns
            col = idx % columns
            widget = EmployeeWidget(self.employees_frame, employee_data=emp)
            widget.grid(row=row, column=col, padx=20, pady=20)
    
    def view_secretariat(self):
        self.view_department("Secretariat")

    def view_logistics(self):
        self.view_department("Logistics")
    
    def view_sales(self):
        self.view_department("Sales")
    
    def view_labor(self):
        self.view_department("Labor")
    
    def view_proprietor(self):
        self.view_department("Proprietor")
    
    def destroy(self):
        """Clean up resources when destroyed"""
        # Clear image references to help with garbage collection
        self.images.clear()
        super().destroy()

if __name__ == "__main__":

    root = tk.Tk()
    app = DashboardTemplate(root)
    root.mainloop()