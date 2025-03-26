from tkinter import *

from DB.ProductDatabase import ProductDatabase


class App(Tk):
    def __init__(self):
        super().__init__()
        self.setupRoot()

        db = ProductDatabase()

        from Controllers.MVC import ScreenView, Controller
        view = ScreenView(self)
        controller = Controller(db, view)

        view.set_controller(controller)

    def setupRoot(self):
        self.state('zoomed')
        self.title("Retail Store")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()
