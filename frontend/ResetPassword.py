from pathlib import Path
from tkinter import Frame, Tk, Canvas, Entry, Button, PhotoImage, messagebox
import threading
from backend.ResetPasswordFunction import ResetPasswordFunction

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "ResetPassword_Assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ResetPasswordWindow(Frame):
    def __init__(self, master, scene_manager=None):
        super().__init__(master)
        self.scene_manager = scene_manager
        self.keep_images_reference = []
        self.backend = ResetPasswordFunction()
        self.setup_ui()

    def setup_ui(self):
        self.master.title("Password Reset")
        self.master.geometry("1440x706")
        self.master.configure(bg="#FFB37F")

        self.canvas = Canvas(
            self,
            bg="#FFB37F",
            height=706,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.load_images()

        # Title
        self.canvas.create_text(
            533.0,
            186.0,
            anchor="nw",
            text="RESET PASSWORD",
            fill="#040404",
            font=("Inter Bold", 51 * -1)
        )

        # Email label
        self.canvas.create_text(
            434.0,
            287.0,
            anchor="nw",
            text="Please enter your email:",
            fill="#040404",
            font=("Inter Bold", 27 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            720.0,
            361.5,
            image=entry_image_1
        )

        # Email entry
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter Regular", 24 * -1)
        )
        self.entry_1.place(
            x=459.0,
            y=329.0,
            width=522.0,
            height=63.0
        )

        # Cancel button
        self.button_1 = Button(
            self,
            image=self.button_image_1 if hasattr(self, "button_image_1") else None,
            text="Back" if not hasattr(self, "button_image_1") else "",
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_cancel,
            relief="flat",
            cursor="hand2",
            activebackground="#FFB37F",
            bg="#FFB37F"
        )
        self.button_1.place(
            x=434.0,
            y=175.0,
            width=72.0,
            height=72.0
        )

        self.button_2 = Button(
            self,
            image=self.button_image_2 if hasattr(self, "button_image_2") else None,
            text="Send Reset Link" if not hasattr(self, "button_image_2") else "",
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_reset_password,
            relief="flat",
            cursor="hand2",
            activebackground="#FFB37F",
            bg="#FFB37F"
        )
        self.button_2.place(
            x=627.0,
            y=434.0,
            width=185.0,
            height=48.0
        )

    def load_images(self):
        try:
            self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
            self.keep_images_reference.append(self.button_image_1)
        except Exception:
            self.button_image_1 = None
        try:
            self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
            self.keep_images_reference.append(self.button_image_2)
        except Exception:
            self.button_image_2 = None
        try:
            self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
            self.keep_images_reference.append(self.entry_image_1)
        except Exception:
            self.entry_image_1 = None

    def handle_reset_password(self):
        email = self.entry_1.get().strip()
    
        # Validate email format
        if not email:
            messagebox.showwarning("Input Error", "Please enter your email address.")
            return
        if "@" not in email or "." not in email:
            messagebox.showwarning("Input Error", "Please enter a valid email address.")
            return

        # Disable button during processing
        self.button_2.config(state="disabled")
        self.button_2.config(text="Sending...")
    
        def do_reset():
            try:
                success, message = self.backend.send_reset_email(email)
            
                self.after(0, lambda: self.handle_reset_result(success, message))
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                self.after(0, lambda: self.handle_reset_result(False, error_message))

        # Start the thread properly
        reset_thread = threading.Thread(target=do_reset, daemon=True)
        reset_thread.start()

    def handle_reset_result(self, success, message):
        # Re-enable button
        self.button_2.config(state="normal")
        self.button_2.config(text="Send Reset Link")
    
        if success:
            messagebox.showinfo("Success", "If an account exists with this email, a password reset link has been sent.")
            if self.scene_manager:
                self.scene_manager.show_scene("login")
        else:
            messagebox.showerror("Error", message)

    def handle_cancel(self):
        if self.scene_manager:
            self.scene_manager.show_scene("login")
        self.entry_1.delete(0, 'end')

if __name__ == "__main__":
    root = Tk()
    app = ResetPasswordWindow(root)
    app.pack(fill="both", expand=True)
    root.resizable(False, False)
    root.mainloop()