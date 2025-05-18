import firebase_admin
from firebase_admin import credentials, firestore
from tkinter import messagebox

try:
    cred = credentials.Certificate("/Users/yenbvasquez/Downloads/jirahub-main 2/backend/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print(f"Firebase initialization error: {e}")

def get_employee_data(employee_id):

    try:
        doc_ref = db.collection("employees").document(employee_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch employee data: {e}")
        return None

def delete_employee(employee_id, window, entry_widget):

    if not employee_id or employee_id == "Employee ID":
        messagebox.showwarning("Warning", "Please enter an Employee ID")
        return
    
    try:
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            "Are you sure you want to delete this employee? This action cannot be undone."
        )
        
        if not confirm:
            return
            
        doc_ref = db.collection("employees").document(employee_id)
        doc = doc_ref.get()
        
        if doc.exists:
            doc_ref.delete()
            messagebox.showinfo("Success", "Employee deleted successfully")
            entry_widget.delete(0, "end") 
            entry_widget.insert(0, "Employee ID")  
           
        else:
            messagebox.showerror("Error", "Employee ID not found")
            
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete employee: {e}")

def search_employee(employee_id, canvas):

    if not employee_id or employee_id == "Employee ID":
        messagebox.showwarning("Warning", "Please enter an Employee ID")
        return
    
    employee_data = get_employee_data(employee_id)
    
    if employee_data:
        # Update the GUI with employee data
        canvas.itemconfig(2, text=employee_data.get("name", "N/A"))  # Employee Full Name
        canvas.itemconfig(3, text=employee_data.get("department", "N/A"))  # Employee Department
        canvas.itemconfig(4, text=employee_data.get("email", "N/A"))  # Employee Email
        canvas.itemconfig(5, text=employee_data.get("phone", "N/A"))  # Employee Phone Number
    else:
        messagebox.showerror("Error", "Employee not found")

        canvas.itemconfig(2, text="{Employee Full Name}")
        canvas.itemconfig(3, text="{Employee Department}")
        canvas.itemconfig(4, text="{Employee Email}")
        canvas.itemconfig(5, text="{Employee Phone Number}")