from firebase_admin import firestore
from tkinter import messagebox

class UpdateEmployeeService:
    def __init__(self, db: firestore.Client):
        self.db = db

    def update_employee(self, employee_id: str, updated_data: dict) -> bool:
        try:
            employee_ref = self.db.collection('employees').document(employee_id)
            if not employee_ref.get().exists:
                messagebox.showerror("Error", "Employee record not found")
                return False
            employee_ref.update(updated_data)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update employee: {str(e)}")
            return False