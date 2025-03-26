import random

from Products.Product import Product


# make list product with own product stats
class StoreItem:
    """ object to hold multiple products and their count """

    def __init__(self, product: Product):
        self.product = product
        self._count = 1

    def get_count(self):
        return self._count

    def set_count(self, value):
        self._count = max(0, value)

    count: int = property(fget=get_count, fset=set_count)

    def __repr__(self) -> str:
        """ returns a formatted string consisting of the product's name, price, and quantity """

        return self.product.productName + " " + "${:.2f}".format(self.product.price/100) + " x" + str(self.count)


class Store:
    """ class that generates products in the store """

    def __init__(self, db):
        self.db = db
        self.stock: list[list[StoreItem]] = []
        self.aisles: list[str] = []

    def generateStore(self):
        """ generates all aisles in the store

            gets Product from database and creates a random amount of them
        """

        self.generateDepartments()
        for key, value in self.db.dbs.items():
            dept: list[StoreItem] = []
            self.stock.append(dept)

            dbLen = len(value.index)
            for prod in range(0, dbLen - 1):
                amtInStock = random.randint(1, 4)
                for i in range(0, amtInStock):
                    newProd = Product(dept=key, pName=value['Product'].iloc[prod], price=value['Price'].iloc[prod])
                    self.addItem(newProd)

    def generateDepartments(self):
        """ populates list of aisles """

        for dept in self.db.productDepartments:
            self.aisles.append(dept)

    def getAisle(self, aisle: str) -> list[StoreItem] | None:
        """ gets list of items based on aisle param """

        index = self.aisles.index(aisle)
        if index > len(self.stock):
            return None
        return self.stock[index]

    def addItem(self, product: Product):
        """ adds item to stock """

        dept = self.db.getDepartment(product)
        inStock, index = self.inStock(product)
        if inStock:
            self.stock[dept][index].count += 1
        else:
            self.stock[dept].append(StoreItem(product))

    def removeItem(self, item: StoreItem):
        """ removes item from stock """

        dept = self.db.getDepartment(item.product)
        inStock, index = self.inStock(item.product)
        if inStock:
            self.stock[dept][index].count -= 1

    def getItem(self, item: StoreItem) -> StoreItem:
        """ gets item from stock """

        dept = self.db.getDepartment(item.product)
        for storeItem in self.stock[dept]:
            if storeItem.product == item.product:
                return storeItem

    def inStock(self, product: Product) -> (bool, int):
        """ checks if item is in stock. returns a bool and Product|None """

        dept = self.db.getDepartment(product)
        for storeItem in self.stock[dept]:
            if storeItem.product.productName == product.productName:
                return True, self.stock[dept].index(storeItem)

        return False, None
