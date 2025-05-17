import tkinter as tk
from tkinter import ttk, messagebox

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("JIRAH ENTERPRISES - Employee Management")
        self.root.geometry("900 x 600")

        self.create_frames()
        self.create_widgets()
        self.load_employees()

    def create_frames(self):
        self.top_frame = ttk.Frame(self.root, padding = "10")
        self.top_frame.pack(fill = tk.X)

        self.middle_frame = ttk.Frame(self.root)
        self.middle_frame.pack(fill = tk.BOTH, expand = True)

        self.bottom_frame = ttk.Frame(self.root, padding = "10")
        self.bottom_frame.pack(fill = tk.X)

def create_widgets(self):
    ttk.Button(self.top_frame, text = "Add Employee", command = self.add_employee).pack(side = tk.LEFT, padx = 5)
    ttk.Button(self.top_frame, text = "Update Employee", command = self.update_employee).pack(side = tk.LEFT, padx = 5)
    ttk.Button(self.top_frame, text = "Delete Employee", command = self.delete_employee).pack(side = tk.LEFT, padx = 5)

# Department filter
    self.dept_var = tk.StringVar()
    self.dept_var.set("All Employees")
    departments = ["All Employees", "Secretariat", "Logistics", "Sales", "Labor", "Proprietor", "Manager"]
    ttk.OptionMenu(self.bottom_frame, self.dept_var, *departments, command=self.filter_employees).pack(side=tk.LEFT)
        
# Employee Treeview
    self.tree = ttk.Treeview(self.middle_frame, columns=("Name", "Department", "Email", "Phone"), show="headings")
    self.tree.heading("Name", text="Name")
    self.tree.heading("Department", text="Department")
    self.tree.heading("Email", text="Email")
    self.tree.heading("Phone", text="Phone")
    self.tree.pack(fill=tk.BOTH, expand=True)
        
def load_employees(self):
        try:
            employees = db.child("employees").get().val()
            self.tree.delete(*self.tree.get_children())
            
            if employees:
                for emp_id, emp_data in employees.items():
                    self.tree.insert("", tk.END, values=(
                        emp_data.get("Name", ""),
                        emp_data.get("Department", ""),
                        emp_data.get("Email", ""),
                        emp_data.get("Phone", "")
                    ), iid=emp_id)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load employees: {e}")
    
def filter_employees(self, *args):
        department = self.dept_var.get()
        if department == "All Employees":
            self.load_employees()
        else:
            try:
                employees = db.child("employees").order_by_child("Department").equal_to(department).get().val()
                self.tree.delete(*self.tree.get_children())
                
                if employees:
                    for emp_id, emp_data in employees.items():
                        self.tree.insert("", tk.END, values=(
                            emp_data.get("Name", ""),
                            emp_data.get("Department", ""),
                            emp_data.get("Email", ""),
                            emp_data.get("Phone", "")
                        ), iid=emp_id)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to filter employees: {e}")
    
def add_employee(self):
        self.employee_form("Add Employee")
    
def update_employee(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an employee to update")
            return
        self.employee_form("Update Employee", selected[0])
    
def delete_employee(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an employee to delete")
            return
        
        if messagebox.askyesno("Confirm", "Delete selected employee?"):
            try:
                db.child("employees").child(selected[0]).remove()
                self.load_employees()
                messagebox.showinfo("Success", "Employee deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete employee: {e}")
    
def employee_form(self, title, emp_id=None):
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("400x300")
        
        # Form fields
        ttk.Label(form, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        name_entry = ttk.Entry(form)
        name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        ttk.Label(form, text="Department:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        dept_var = tk.StringVar()
        departments = ["Secretariat", "Logistics", "Sales", "Labor", "Proprietor", "Manager"]
        ttk.OptionMenu(form, dept_var, *departments).grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
        ttk.Label(form, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        email_entry = ttk.Entry(form)
        email_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        
        ttk.Label(form, text="Phone:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        phone_entry = ttk.Entry(form)
        phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Pre-fill for update
        if emp_id:
            try:
                emp_data = db.child("employees").child(emp_id).get().val()
                name_entry.insert(0, emp_data.get("Name", ""))
                dept_var.set(emp_data.get("Department", ""))
                email_entry.insert(0, emp_data.get("Email", ""))
                phone_entry.insert(0, emp_data.get("Phone", ""))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load employee data: {e}")
                form.destroy()
                return
        
        # Submit button
        def submit():
            data = {
                "Name": name_entry.get(),
                "Department": dept_var.get(),
                "Email": email_entry.get(),
                "Phone": phone_entry.get()
            }
            
            if not all(data.values()):
                messagebox.showwarning("Warning", "All fields are required")
                return
            
            try:
                if title == "Add Employee":
                    db.child("employees").push(data)
                    messagebox.showinfo("Success", "Employee added successfully")
                else:
                    db.child("employees").child(emp_id).update(data)
                    messagebox.showinfo("Success", "Employee updated successfully")
                form.destroy()
                self.load_employees()
            except Exception as e:
                messagebox.showerror("Error", f"Operation failed: {e}")
        
        ttk.Button(form, text="Submit", command=submit).grid(row=4, column=1, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeDirectory(root)
    root.mainloop()