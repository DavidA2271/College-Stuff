from tkinter import *

from Controllers.MVC import ScreenView
from GUI.ButtonFrame import ButtonFrame


class StoreScreen(ButtonFrame):
    def __init__(self, view: ScreenView, btn_per_row: int):
        super().__init__(master=view.root, btn_per_row=btn_per_row)
        self.config(bg='blue')

        self.view = view
        self.view.set_current_screen(self)

        aisles = view.store_controller.store.aisles

        buyLabel = Label(self, text="What are you looking to buy?")
        buyLabel.grid(row=0, columnspan=len(aisles), pady=50)

        # generates buttons for each aisle
        super().make_button_grid(count=len(aisles), btn_text=aisles)

    def on_btn_click(self, btn_index: int):
        self.view.store_controller.set_current_aisle(btn_index)
        self.makeAisle()

    def makeAisle(self):
        """ generates a frame that shows shopping cart and products in aisle """

        aisle = AisleScreen(self)
        aisle.grid(row=0, column=0, sticky='nsew')

    def goBack(self):
        """ destroys frame and goes back to previous frame """

        self.destroy()


class AisleScreen(Frame):
    def __init__(self, owner: StoreScreen):
        super().__init__(master=owner.view.root)
        self.owner = owner
        self.owner.view.set_current_screen(self)
        self.config(bg='pink')

        self.aisle = owner.view.store_controller.current_aisle
        # self.stock = owner.view.store_controller.current_stock
        self.cart = owner.view.store_controller.cart
        self.cart_frame = CartFrame(self, 1)
        self.store_frame = StoreFrame(self, 1)

        self.cart_frame.grid(column=0, row=0, pady=50, padx=50, sticky='nw')
        self.store_frame.grid(row=0, column=2, sticky='ne', pady=50, padx=50)

        go_back_btn = Button(self, text="Go Back", command=self.go_back)
        go_back_btn.grid(column=1, row=1, sticky='s', pady=50, padx=50)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def go_back(self):
        self.owner.view.set_current_screen(self.owner)
        self.destroy()


class StoreFrame(ButtonFrame):
    def __init__(self, master: AisleScreen, btn_per_row: int):
        super().__init__(master=master, btn_per_row=btn_per_row)
        self.owner = master

        super().make_button_grid(len(master.aisle), master.aisle)

        for i in range(len(self.buttons)):
            self.update_button(i)

    def on_btn_click(self, btn_index: int):
        self.owner.owner.view.store_controller.purchase_item(btn_index)

    def update_button(self, btn_index: int, text: str = ''):
        store_item = self.owner.aisle[btn_index]

        super().update_button(btn_index, str(store_item))

        if store_item.count <= 0:
            self.buttons[btn_index].grid_forget()
        elif store_item.count > 0:
            self.buttons[btn_index].grid(row=btn_index)


class CartFrame(ButtonFrame):
    def __init__(self, master: AisleScreen, btn_per_row: int):
        super().__init__(master=master, btn_per_row=btn_per_row)
        self.owner = master

        super().make_button_grid(len(master.cart.items), master.cart.items)

        self.totalLabel = Label(self, text="Total Price = " + master.cart.getTotalPrice())
        self.totalLabel.grid(pady=10, padx=10, sticky='s')

        for i in range(len(self.buttons)):
            self.update_button(i)

    def on_btn_click(self, btn_index: int):
        self.owner.owner.view.store_controller.return_item(btn_index)

    def update_button(self, btn_index: int, text: str = None):
        self.totalLabel.grid_forget()
        cart_item = self.owner.owner.view.store_controller.cart.items[btn_index]

        super().update_button(btn_index, str(cart_item))

        if cart_item.count <= 0:
            self.buttons[btn_index].grid_forget()
        elif cart_item.count > 0:
            self.buttons[btn_index].grid(row=btn_index)

        self.totalLabel.config(text="Total Price = " + self.owner.cart.getTotalPrice())
        self.totalLabel.grid()
