from tkinter import Tk
from backend.SceneManager import SceneManager
from frontend.CreateEmployee import CreateEmployeeWindow
from frontend.DeleteEmployee import DeleteEmployeeWindow
from frontend.UpdateEmployee import UpdateEmployeeWindow
from frontend.MainWindow import LoginWindow
from frontend.SignUpAdmin import SignUpAdminWindow
from frontend.DashboardTemplate import DashboardTemplate
from frontend.ResetPassword import ResetPasswordWindow

def main():
    root = Tk()
    root.title("Jirahub")

    scene_manager = SceneManager(root)

    scene_manager.register_scene("login", lambda master: LoginWindow(master, scene_manager))
    scene_manager.register_scene("signup_admin", lambda master: SignUpAdminWindow(master, scene_manager))
    scene_manager.register_scene("reset_password", lambda master: ResetPasswordWindow(master, scene_manager))
    scene_manager.register_scene("dashboard", lambda master, user=None: DashboardTemplate(master, scene_manager, user_data=user))
    scene_manager.register_scene("create_employee", lambda master, user=None: CreateEmployeeWindow(master, scene_manager, user_data=user))
    scene_manager.register_scene("update_employee", lambda master, user=None: UpdateEmployeeWindow(master, scene_manager))
    scene_manager.register_scene("delete_employee", lambda master: DeleteEmployeeWindow(master, scene_manager))

    scene_manager.show_scene("login")

    root.mainloop()

if __name__ == "__main__":
    main()