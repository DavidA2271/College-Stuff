from tkinter import *

from pandas import DataFrame

from DB.ProductDatabase import ProductDatabase
from Products.Product import Product
from Shopping.ShoppingCart import ShoppingCart
from Shopping.Store import Store


class ScreenView:
    """ holds the root tk of the app. responsible for making screens """

    def __init__(self, root: Tk):
        self.root = root
        self.current_screen = None

        from GUI.MainScreen import MainScreen
        mainscreen = MainScreen(self)
        mainscreen.grid()

        self.base_controller = None
        self.store_controller = None
        self.admin_controller = None

    def set_controller(self, controller):
        self.base_controller = controller

    def set_current_screen(self, frame: Frame):
        """ sets current screen so it can be accessed more easily """

        self.current_screen = frame

    def create_storescreen(self):
        """ creates the store screen """

        self.store_controller = StoreController(self.base_controller)
        self.store_controller.setup()

        from GUI.StoreScreens import StoreScreen
        storescreen = StoreScreen(self, 3)
        storescreen.grid(row=0, column=0, sticky='nsew')

    def create_adminscreen(self):
        """ creates the admin screen """

        self.admin_controller = AdminController(self.base_controller)

        from GUI.AdminScreens import AdminScreen
        adminscreen = AdminScreen(self, 3)
        adminscreen.grid(row=0, column=0, sticky='nsew')


class Controller:
    """ base class that holds the view and model (database) """

    def __init__(self, db: ProductDatabase, view: ScreenView):
        self.db = db
        self.db.registerProducts()
        self.view = view


class StoreController(Controller):
    """ controller for store logic """

    def __init__(self, controller: Controller):
        super().__init__(controller.db, controller.view)

        self.store = None
        self.cart = None

        self.current_aisle = None

    def setup(self):
        self.store = Store(self.db)
        self.store.generateStore()
        self.cart = ShoppingCart()

    def reset(self):
        self.store = None
        self.cart = None

    def get_aisles(self) -> list[str]:
        return self.store.aisles

    def set_current_aisle(self, index: int):
        self.current_aisle = self.store.stock[index]

    def get_cart_item_from_store(self, store_index: int) -> int:
        item = self.current_aisle[store_index]
        cart_item = self.cart.getItem(item)
        index = self.cart.items.index(cart_item)
        return index

    def get_store_item_from_cart(self, cart_index: int) -> int:
        item = self.cart.items[cart_index]
        store_item = self.store.getItem(item)
        try:
            index = self.current_aisle.index(store_item)
        except ValueError:
            index = -1
        return index

    def purchase_item(self, store_index: int):
        item = self.current_aisle[store_index]
        self.store.removeItem(item)
        self.cart.addItem(item)

        from GUI.StoreScreens import AisleScreen
        if type(self.view.current_screen) is AisleScreen:
            cart_index = self.get_cart_item_from_store(store_index)
            self.view.current_screen.cart_frame.update_button(cart_index)
            self.view.current_screen.store_frame.update_button(store_index)
        else:
            print(type(self.view.current_screen))

    def return_item(self, cart_index: int):
        item = self.cart.items[cart_index]
        self.store.addItem(item.product)
        self.cart.removeItem(item)

        from GUI.StoreScreens import AisleScreen
        if type(self.view.current_screen) is AisleScreen:
            store_index = self.get_store_item_from_cart(cart_index)
            self.view.current_screen.cart_frame.update_button(cart_index)
            if store_index >= 0:
                self.view.current_screen.store_frame.update_button(store_index)
        else:
            print(type(self.view.current_screen))


class AdminController(Controller):
    """ controller for admin logic """

    def __init__(self, controller: Controller):
        super().__init__(controller.db, controller.view)

        self.current_dept = None

    def set_current_dept(self, dept: str):
        self.current_dept = dept

    def get_current_dept_data(self) -> DataFrame:
        return self.db.dbs[self.current_dept]

    def save_product_data(self, index: int, product: Product):
        destroy = self.current_dept != product.department
        self.db.saveChanges(index, self.current_dept, product)

        from GUI.AdminScreens import DepartmentScreen
        if type(self.view.current_screen) is DepartmentScreen:
            self.view.current_screen.update_button(index, product.productName, destroy)
        else:
            print(type(self.view.current_screen))

    def make_new_dept(self, dept: str):
        if not self.db.productDepartments.__contains__(dept):
            self.view.current_screen.update_button(0, dept)
            self.db.make_new_dept(dept)
