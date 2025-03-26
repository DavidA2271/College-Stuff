import tkinter
from tkinter import *

from pandas import Series

from Controllers.MVC import ScreenView
from GUI.ButtonFrame import ButtonFrame


class AdminScreen(ButtonFrame):
    def __init__(self, view: ScreenView, btn_per_row: int):
        super().__init__(master=view.root, btn_per_row=btn_per_row)
        self.config(bg='green')

        self.view = view
        self.view.set_current_screen(self)

        editDeptLbl = Label(self, text="What department do you want to edit?")
        editDeptLbl.grid(row=0, columnspan=3, pady=50)

        self.departments = self.view.admin_controller.db.productDepartments
        super().make_button_grid(count=len(self.departments), btn_text=self.departments)

        last_row = int(len(self.buttons)/3) + 2
        self.grid_rowconfigure(index=last_row, weight=1)
        operation_frame = Frame(self)
        operation_frame.grid(row=last_row, column=0, columnspan=3, pady=20, padx=20, sticky='sew')
        operation_frame.grid_rowconfigure(0, weight=1)
        operation_frame.grid_columnconfigure(0, weight=1)
        operation_frame.grid_columnconfigure(2, weight=1)

        new_dept_button = Button(operation_frame, text='New Department',
                                 command=self.make_new_dept_window)
        new_dept_button.grid(row=0, column=0, pady=20, sticky='s')

        goBackButton = Button(operation_frame, text="Go Back", command=self.destroy)
        goBackButton.grid(row=0, column=2, pady=20, sticky='s')

    def on_btn_click(self, btn_index: int):
        self.view.admin_controller.set_current_dept(self.departments[btn_index])
        self.make_department_screen()

    def update_button(self, btn_index: int, text: str):
        btn_index = len(self.buttons)
        super().update_button(btn_index, text)

    def make_department_screen(self):
        dept_screen = DepartmentScreen(self, 3)
        dept_screen.grid(row=0, column=0, sticky='nsew')

    def make_new_dept_window(self):
        NewDeptTextWindow(self)

    def make_new_dept(self, dept: str):
        self.view.admin_controller.make_new_dept(dept)


class DepartmentScreen(ButtonFrame):
    def __init__(self, owner: AdminScreen, btn_per_row: int):
        super().__init__(master=owner.view.root, btn_per_row=btn_per_row)
        self.config(bg='gray')

        self.owner = owner
        self.owner.view.set_current_screen(self)

        editProdLabel = Label(self, text="What product do you want to edit?")
        editProdLabel.grid(row=0, columnspan=3, pady=50)

        data = owner.view.admin_controller.get_current_dept_data()
        super().make_button_grid(count=len(data['Product'].tolist()), btn_text=data['Product'].tolist())

        last_row = int(len(self.buttons) / 3) + 2

        self.new_prod_btn = Button(self, text='New Product', command=self.make_new_product)
        self.new_prod_btn.grid(row=last_row, column=0, pady=20, sticky='s')

        self.goBackButton = Button(self, text="Go Back", command=self.go_back)
        self.goBackButton.grid(row=last_row, column=2, pady=20, sticky='s')

    def on_btn_click(self, btn_index: int):
        self.make_product_window(btn_index)

    def update_button(self, btn_index: int, text: str, destroy: bool = False):
        super().update_button(btn_index, text)

        if destroy:
            self.buttons[btn_index].destroy()
            del self.buttons[btn_index]

        last_row = int(len(self.buttons) / 3) + 2
        self.new_prod_btn.grid_forget()
        self.new_prod_btn.grid(row=last_row, column=0, pady=20, sticky='s')
        self.goBackButton.grid_forget()
        self.goBackButton.grid(row=last_row, column=2, pady=20, sticky='s')

    def go_back(self):
        self.owner.view.set_current_screen(self.owner)
        self.destroy()

    def make_new_product(self):
        data = {'Product': 'Name', 'Price': 000}
        series = Series(data)
        ProductWindow(self, series, len(self.buttons))

    def make_product_window(self, btn_index: int):
        product_data = self.owner.view.admin_controller.get_current_dept_data().iloc[btn_index]
        ProductWindow(self, product_data, btn_index)


class NewDeptTextWindow(Toplevel):
    def __init__(self, owner: AdminScreen):
        super().__init__(owner.view.root)
        self.owner = owner

        self.text_box = Text(self, height=1, width=20)
        self.text_box.insert(tkinter.END, 'New Department')
        self.text_box.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        save_btn = Button(self, text='Save', command=self.save_dept)
        save_btn.grid(row=1, column=0, padx=20, pady=10)

        close_btn = Button(self, text='Close', command=self.destroy)
        close_btn.grid(row=1, column=1, pady=10, padx=20)

    def save_dept(self):
        dept = self.text_box.get(1.0, "end-1c")
        self.owner.make_new_dept(dept)
        self.destroy()


class ProductWindow(Toplevel):
    def __init__(self, owner: DepartmentScreen, product_data: Series, index: int):
        super().__init__(master=owner.owner.view.root)
        self.geometry('300x200')

        self.owner = owner

        self.index = index

        from Products.Product import Product
        self.product = Product(dept=owner.owner.view.admin_controller.current_dept,
                               pName=product_data['Product'],
                               price=product_data['Price'])

        frame = Frame(self)
        frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.dept_text = StringVar()
        self.name_box = Text()
        self.price_box = Text()
        self.set_product_view(frame)

        save_button = Button(self, text='Save', command=self.save_data)
        save_button.grid(row=3, column=0)

        cancel_button = Button(self, text='Cancel', command=self.destroy)
        cancel_button.grid(row=3, column=1)

    def set_product_view(self, frame: Frame):
        options = self.owner.owner.view.admin_controller.db.productDepartments
        self.dept_text.set(self.product.department)
        dept_label = Label(frame, text='Department:')
        dept_label.grid(row=0, column=0, padx=10, pady=10)
        dept_box = OptionMenu(frame, self.dept_text, *options)
        dept_box.grid(row=0, column=1, pady=10, padx=10)

        name_label = Label(frame, text='Name:')
        name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_box = Text(frame, height=1, width=20)
        self.name_box.insert(tkinter.END, self.product.productName)
        self.name_box.grid(row=1, column=1, pady=10, padx=10)

        price_label = Label(frame, text='Price:')
        price_label.grid(row=2, column=0, padx=10, pady=10)
        self.price_box = Text(frame, height=1, width=20)
        self.price_box.insert(tkinter.END, "${:.2f}".format(self.product.price/100))
        self.price_box.grid(row=2, column=1, pady=10, padx=10)

    def save_data(self):
        self.product.department = self.dept_text.get()
        self.product.productName = self.name_box.get(1.0, "end-1c")
        price_str = self.price_box.get(1.0, "end-1c")
        price = price_str.replace('$', '').replace('.', '')
        self.product.price = int(price)

        self.owner.owner.view.admin_controller.save_product_data(self.index, self.product)

        self.destroy()
