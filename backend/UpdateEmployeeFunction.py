from firebase_admin import firestore
from tkinter import messagebox

class UpdateEmployeeService:
    def __init__(self, db: firestore.Client):
        """Initialize the service with a Firestore client."""
        self.db = db

    def update_employee(self, employee_id: str, updated_data: dict) -> bool:
        """
        Update an employee's record in Firestore.

        Args:
            employee_id (str): The unique ID of the employee.
            updated_data (dict): A dictionary containing the updated employee data.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        try:
            # Reference to the employee document
            employee_ref = self.db.collection('employees').document(employee_id)

            # Check if the employee exists
            if not employee_ref.get().exists:
                messagebox.showerror("Error", "Employee record not found")
                return False

            # Update the employee record
            employee_ref.update(updated_data)
            messagebox.showinfo("Success", "Employee record updated successfully")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update employee: {str(e)}")
            return False