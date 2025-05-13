from pathlib import Path
from tkinter import Frame, Tk, Canvas, Entry, Button, PhotoImage, messagebox
from backend.MainWindowFunction import AuthService

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\SignUpAdmin_Assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SignUpAdminWindow(Frame):
    def __init__(self, master, scene_manager):
        super().__init__(master)
        self.scene_manager = scene_manager
        #self.auth_service = AuthService()
        self.keep_images_reference = []
        self.setup_ui()
    
    def setup_ui(self):
        self.master.geometry("1440x706")
        self.master.configure(bg="#FFFFFF")
        self.master.title("Admin Registration")

        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=706,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        # Load and store images
        self.load_images()
        
        # Create UI elements
        self.create_text_elements()
        self.create_entry_fields()
        self.create_buttons()
        pass
    
    def load_images(self):
        """Load all images and keep references"""
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.keep_images_reference.append(self.image_image_1)
        self.canvas.create_image(321.0, 353.0, image=self.image_image_1)

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.keep_images_reference.append(self.entry_image_1)
        
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.keep_images_reference.append(self.entry_image_2)
        
        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        self.keep_images_reference.append(self.entry_image_3)
        
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.keep_images_reference.append(self.button_image_1)
    
    def create_text_elements(self):
        """Create all text elements on the canvas"""
        self.canvas.create_text(
            777.0, 94.0,
            anchor="nw",
            text="CREATE YOUR ACCOUNT",
            fill="#FF6900",
            font=("Inter Bold", 40 * -1)
        )
        
        self.canvas.create_text(
            777.0, 160.0,
            anchor="nw",
            text="Name",
            fill="#FF6900",
            font=("Inter Bold", 27 * -1)
        )
        
        self.canvas.create_text(
            777.0, 279.0,
            anchor="nw",
            text="Email",
            fill="#FF6900",
            font=("Inter Bold", 27 * -1)
        )
        
        self.canvas.create_text(
            777.0, 398.0,
            anchor="nw",
            text="Password",
            fill="#FF6900",
            font=("Inter Bold", 27 * -1)
        )
    
    def create_entry_fields(self):
        """Create all entry fields"""
        # Name Entry
        self.entry_bg_3 = self.canvas.create_image(
            1053.0, 230.5,
            image=self.entry_image_3
        )
        self.name_entry = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            font=("Inter Bold", 20 * -1)
        )
        self.name_entry.place(
            x=802.0,
            y=198.0,
            width=502.0,
            height=63.0
        )
        
        # Email Entry
        self.entry_bg_1 = self.canvas.create_image(
            1053.0, 349.5,
            image=self.entry_image_1
        )
        self.email_entry = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            font=("Inter Bold", 20 * -1)
        )
        self.email_entry.place(
            x=802.0,
            y=317.0,
            width=502.0,
            height=63.0
        )
        
        # Password Entry
        self.entry_bg_2 = self.canvas.create_image(
            1053.0, 463.5,
            image=self.entry_image_2
        )
        self.password_entry = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            show="*",
            font=("Inter Bold", 20 * -1)
        )
        self.password_entry.place(
            x=802.0,
            y=431.0,
            width=502.0,
            height=63.0
        )
    
    def create_buttons(self):
        """Create all buttons"""
        self.register_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_register,
            relief="flat",
            cursor="hand2"
        )
        self.register_button.place(
            x=777.0,
            y=548.0,
            width=324.0,
            height=64.0
        )
    
    def handle_register(self):
        """Handle the registration button click"""
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        
        # Validate inputs
        if not all([name, email, password]):
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return
        
        if len(password) < 8:
            messagebox.showwarning("Input Error", "Password must be at least 8 characters")
            return
        
        # Ask for admin code (in a real app, this would be more secure)
        admin_code = messagebox.askstring(
            "Admin Verification",
            "Enter admin registration code:",
            parent=self.root
        )
        
        if not admin_code:
            return
        
        # Attempt registration
        success, message = self.auth_service.register_admin(name, email, password, admin_code)
        
        if success:
            messagebox.showinfo("Success", message)
            self.scene_manager.show_scene("login")  # Return to login # Close the registration window
        else:
            messagebox.showerror("Registration Failed", message)

if __name__ == "__main__":
    root = Tk()
    app = SignUpAdminWindow(root)
    root.resizable(False, False)
    root.mainloop()