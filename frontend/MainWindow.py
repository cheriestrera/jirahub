import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from backend.SceneManager import SceneManager
from tkinter import Frame, Tk, Canvas, Entry, Button, PhotoImage, messagebox, simpledialog
from backend.MainWindowFunction import AuthService

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\CC15project\frontend\MainWindow_Assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginWindow(Frame):  # Inherit from Frame
    def __init__(self, master, scene_manager):
        super().__init__(master)
        self.scene_manager = scene_manager  # Store the SceneManager instance
        self.auth_service = AuthService()
        self.images = []
        self.setup_ui()
    
    def setup_ui(self):
        self.master.geometry("1440x706")
        self.master.configure(bg="#FFFFFF")

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
        
        # Background image
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(321.0, 353.0, image=image_image_1)
        
        # Texts
        self.canvas.create_text(
            765.0, 122.0,
            anchor="nw",
            text="WELCOME ADMIN",
            fill="#FF6900",
            font=("Inter Bold", 40 * -1)
        )
        
        self.canvas.create_text(
            765.0, 196.0,
            anchor="nw",
            text="Email",
            fill="#FF6900",
            font=("Inter Bold", 27 * -1)
        )
        
        self.canvas.create_text(
            765.0, 316.0,
            anchor="nw",
            text="Password",
            fill="#FF6900",
            font=("Inter Bold", 27 * -1)
        )
        
        # Email Entry
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(1041.0, 266.5, image=entry_image_1)
        self.email_entry = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            font=("Inter Regular", 20 * -1)
        )
        self.email_entry.place(x=790.0, y=234.0, width=502.0, height=63.0)
        
        # Password Entry
        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(1041.0, 381.5, image=entry_image_2)
        self.password_entry = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            show="*",
            font=("Inter Regular", 20 * -1)
        )
        self.password_entry.place(x=790.0, y=349.0, width=502.0, height=63.0)
        
        # Login Button
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.login_button = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_login,
            relief="flat",
            cursor="hand2"
        )
        self.login_button.place(x=1053.0, y=443.0, width=264.0, height=64.0)
        
        # Register Button
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.images.append(button_image_1)
        self.register_button = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_register,
            relief="flat",
            cursor="hand2"
        )
        self.register_button.place(x=765.0, y=443.0, width=264.0, height=64.0)
        
        # Forgot Password Button
        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.forgot_button = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_forgot_password,
            relief="flat",
            cursor="hand2"
        )
        self.forgot_button.place(x=765.0, y=520.0, width=552.0, height=64.0)
        
        # Keep references to images
        self.images = [
            image_image_1, entry_image_1, entry_image_2,
            button_image_1, button_image_2, button_image_3
        ]
    
    def handle_login(self):
        print("Login button clicked")

        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showwarning("Input Error", "Please enter both email and password")
            return

        user = self.auth_service.login(email, password)
        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.scene_manager.show_scene("dashboard", user=user)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
    
    def handle_register(self):
        print("Sign Up button clicked")
        self.scene_manager.show_scene("signup_admin")
    
    def handle_forgot_password(self):
        email = self.email_entry.get()
        if not email:
            messagebox.showwarning("Input Error", "Please enter your email")
            return
        
        self.auth_service.reset_password(email)

if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.resizable(False, False)
    root.mainloop()