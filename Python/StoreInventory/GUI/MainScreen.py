from tkinter import *

from Controllers.MVC import ScreenView


class MainScreen(Frame):
    def __init__(self, view: ScreenView):
        super().__init__(view.root)
        self.view = view
        self.view.set_current_screen(self)
        self.setup()

    def setup(self):
        startupFrame = Frame(self.view.root, bg="pink")
        startupFrame.grid(row=0, column=0, sticky='nsew')

        label = Label(startupFrame, text="Welcome to RETAIL STORE!")
        label.pack(pady=100)

        customerButton = Button(startupFrame, text="Shop as customer", command=self.view.create_storescreen)
        customerButton.pack(pady=20)

        adminButton = Button(startupFrame, text="Edit product data", command=self.view.create_adminscreen)
        adminButton.pack(pady=20)
