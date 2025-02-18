from tkinter import *
import pyqrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
import os

class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False, False)

        title = Label(self.root, text="QR Code Generator", font=("times new roman", 30), bg='#053246', fg="white", anchor='w')
        title.place(x=0, y=0, relwidth=1)

        # Employee Details Variables
        self.var_emp_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        emp_Frame.place(x=50, y=100, width=500, height=450)

        emp_title = Label(emp_Frame, text="Employee Details", font=("goudy old style", 20), bg='#043256', fg="white")
        emp_title.place(x=0, y=0, relwidth=1)

        Label(emp_Frame, text="Employee ID", font=("times new roman", 15, "bold"), bg='white').place(x=20, y=60)
        Label(emp_Frame, text="Name", font=("times new roman", 15, "bold"), bg='white').place(x=20, y=100)
        Label(emp_Frame, text="Department", font=("times new roman", 15, "bold"), bg='white').place(x=20, y=140)
        Label(emp_Frame, text="Designation", font=("times new roman", 15, "bold"), bg='white').place(x=20, y=200)

        Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_code, bg='lightyellow').place(x=200, y=60)
        Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_name, bg='lightyellow').place(x=200, y=100)
        Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_department, bg='lightyellow').place(x=200, y=140)
        Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_designation, bg='lightyellow').place(x=200, y=200)

        Button(emp_Frame, text='QR Generate', command=self.generate, font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=250, width=180, height=30)
        Button(emp_Frame, text='Clear', command=self.clear, font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=282, y=250, width=120, height=30)

        self.lbl_msg = Label(emp_Frame, text='', font=("times new roman", 20), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=300)

        Label(qr_Frame, text="Employee QR Code", font=("goudy old style", 20), bg='#043256', fg="white").place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text='No QR\nAvailable', font=('times new roman', 15), bg='#3f51b5', fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.lbl_msg.config(text='')

    def generate(self):
        if not all([self.var_emp_code.get(), self.var_name.get(), self.var_department.get(), self.var_designation.get()]):
            self.lbl_msg.config(text='All Fields are Required!!!!', fg='red')
        else:
            qr_data = f"Employee ID: {self.var_emp_code.get()}\nEmployee Name: {self.var_name.get()}\nDepartment: {self.var_department.get()}\nDesignation: {self.var_designation.get()}"
            qr = pyqrcode.create(qr_data)

            # Ensure the Employee_QR folder exists
            if not os.path.exists("Employee_QR"):
                os.makedirs("Employee_QR")

            qr_file_name = f"Employee_QR/Emp_{self.var_emp_code.get()}.png"
            qr.png(qr_file_name, scale=10)

            # Load and display the QR code image
            self.qr_image = Image.open(qr_file_name)
            self.qr_image = resizeimage.resize_cover(self.qr_image, [180, 180])
            self.qr_image = ImageTk.PhotoImage(self.qr_image)

            self.qr_code.config(image=self.qr_image)
            self.lbl_msg.config(text='QR Generated Successfully!!!', fg='green')


root = Tk()
obj = Qr_Generator(root)
root.mainloop()
