
class Product:
    """ class to hold product data """

    department = ""
    productName = "GenericProduct"
    price = 0

    def __init__(self, dept: str, pName: str, price: int):
        self.department = dept
        self.productName = pName
        self.price = price

    def __repr__(self) -> str:
        """ converts the product into an easier to read string

        returns a string that contains the quality, name, and price of the product
        """

        return self.productName + "   " + "${:.2f}".format(self.price/100)
