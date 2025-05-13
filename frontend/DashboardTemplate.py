from tkinter import Frame, Canvas, Button, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\DashboardTemplate_Assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DashboardTemplate(Frame):
    def __init__(self, master, scene_manager=None, user_data=None):
        super().__init__(master)
        self.scene_manager = scene_manager
        self.user_data = user_data
        self.images = []  # To store PhotoImage references
        self.setup_ui()

    def setup_ui(self):
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
        """Load and store all image references"""
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
        """Create all text elements on the canvas"""
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
        """Create and place all buttons"""
        # Button 1
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.images.append(self.button_image_1)
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            cursor="hand2"
        )
        self.button_1.place(x=265.0, y=113.0, width=247.0, height=42.0)

        # Button 2
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.images.append(self.button_image_2)
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
            cursor="hand2"
        )
        self.button_2.place(x=534.0, y=113.0, width=247.0, height=42.0)

        # Button 3 (Navigation)
        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.images.append(self.button_image_3)
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.navigate_home,
            relief="flat",
            cursor="hand2"
        )
        self.button_3.place(x=37.0, y=113.0, width=161.15109252929688, height=41.803955078125)

        # Button 4 (Logout)
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

    # Button 5
        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.images.append(self.button_image_5)
        self.button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_department_view,  # Example functionality
            relief="flat",
            cursor="hand2"
        )
        self.button_5.place(x=37.0, y=228.0, width=141.0, height=24.0)

        # Button 6
        self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.images.append(self.button_image_6)
        self.button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_employee_directory,  # Example functionality
            relief="flat",
            cursor="hand2"
        )
        self.button_6.place(x=30.0, y=312.0, width=121.0, height=28.0)

    # Button 7
        self.button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        self.images.append(self.button_image_7)
        self.button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_attendance,  # Example functionality
            relief="flat",
            cursor="hand2"
        )
        self.button_7.place(x=37.0, y=346.0, width=85.0, height=24.0)

        # Button 8
        self.button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
        self.images.append(self.button_image_8)
        self.button_8 = Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_payroll,  # Example functionality
            relief="flat",
            cursor="hand2"
        )
        self.button_8.place(x=37.0, y=377.0, width=51.0, height=24.0)

        # Button 9
        self.button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
        self.images.append(self.button_image_9)
        self.button_9 = Button(
            self,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_settings,  # Example functionality
            relief="flat",
            cursor="hand2"
        )
        self.button_9.place(x=37.0, y=405.0, width=55.0, height=24.0)

        # Button 10
        self.button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
        self.images.append(self.button_image_10)
        self.button_10 = Button(
            self,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_reports,  # Example functionality
            relief="flat",
            cursor="hand2"
        )
        self.button_10.place(x=37.0, y=432.0, width=95.0, height=24.0)

    def navigate_home(self):
        """Handle navigation to home/dashboard"""
        if self.scene_manager:
            self.scene_manager.show_scene("dashboard", user_data=self.user_data)

    def handle_logout(self):
        """Handle logout action"""
        if self.scene_manager:
            self.scene_manager.show_scene("login")
        else:
            self.master.destroy()  # Fallback if no scene manager

    def handle_department_view(self):
        """Handle department view button click"""
        if self.scene_manager:
            self.scene_manager.show_scene("departments")
        else:
            print("Department view clicked")

    def handle_employee_directory(self):
        """Handle employee directory button click"""
        if self.scene_manager:
            self.scene_manager.show_scene("employees")
        else:
            print("Employee directory clicked")

    def handle_attendance(self):
        """Handle attendance button click"""
        if self.scene_manager:
            self.scene_manager.show_scene("attendance")
        else:
            print("Attendance clicked")

    def handle_payroll(self):
        """Handle payroll button click"""
        if self.scene_manager:
            self.scene_manager.show_scene("payroll")
        else:
            print("Payroll clicked")

    def handle_settings(self):
        """Handle settings button click"""
        if self.scene_manager:
            self.scene_manager.show_scene("settings")
        else:
            print("Settings clicked")

    def handle_reports(self):
        """Handle reports button click"""
        if self.scene_manager:
            self.scene_manager.show_scene("reports")
        else:
            print("Reports clicked")

    def destroy(self):
        """Clean up resources when destroyed"""
        # Clear image references to help with garbage collection
        self.images.clear()
        super().destroy()