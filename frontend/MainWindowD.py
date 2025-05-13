import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from backend.MainWindowFunction import AuthService  # Your backend class

# Keep your existing path setup
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Marites\Downloads\1 MainWindow-20250511T145919Z-1-001\1 MainWindow\frontend\MainWindow_Assets")  # Changed to relative path

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginWindow:
    def __init__(self):
        self.window = Tk()
        self.auth = AuthService()  # Initialize backend
        self.images = []  # To hold image references
        self.setup_ui()

    def setup_ui(self):
        self.window.geometry("1440x706")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Admin Login")

        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=706,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # --- Load images and store references ---
        self.image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.images.append(self.image_1)  # Prevent garbage collection
        canvas.create_image(321.0, 353.0, image=self.image_1)

        # --- Your existing UI elements ---
        canvas.create_text(768.0, 160.0, anchor="nw", text="WELCOME ADMIN", fill="#FF6900", font=("Inter Bold", 40 * -1))
        
        canvas.create_text(
        768.0,
        234.0,
        anchor="nw",
        text="Email",
        fill="#FF6900",
        font=("Inter Bold", 27 * -1)
        )

        canvas.create_text(
        768.0,
        354.0,
        anchor="nw",
        text="Password",
        fill="#FF6900",
        font=("Inter Bold", 27 * -1)
        )

        # Entries (now instance variables)
        self.entry_1 = Entry(bd=0, bg="#F4F4F4", font=("Inter Regular", 16))
        self.entry_1.place(x=793.0, y=272.0, width=502.0, height=63.0)

        self.entry_2 = Entry(bd=0, bg="#F4F4F4", show="*", font=("Inter Regular", 16))
        self.entry_2.place(x=793.0, y=387.0, width=502.0, height=63.0)

        # Modified buttons with backend commands
        self.button_img_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.images.append(self.button_img_1)
        Button(
            image=self.button_img_1,
            command=self.handle_login,  # Connected to backend
            relief="flat"
        ).place(x=768.0, y=481.0, width=164.0, height=64.0)

    def handle_login(self):
        """Handle login button click."""
        email = self.entry_1.get()
        password = self.entry_2.get()

        # Delegate login logic to the backend
        success, message = self.auth.login(email, password)

        if success:
            messagebox.showinfo("Success", message)
            self._open_dashboard(email)  # Pass the email (or user ID) to the dashboard
        else:
            messagebox.showerror("Error", message)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = LoginWindow()
    app.run()