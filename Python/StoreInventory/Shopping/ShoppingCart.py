from Shopping.Store import StoreItem


class ShoppingCart:
    """ class to hold items the user wants to buy """

    # items the user decided to buy
    items: list[StoreItem] = []

    def addItem(self, item: StoreItem):
        """ adds item to cart """

        copy = StoreItem(item.product)
        for itm in self.items:
            if itm.product.productName == item.product.productName:
                itm.count += 1
                return

        self.items.append(copy)

    def removeItem(self, item: StoreItem):
        """removes item from cart"""

        copy = self.getItem(item)
        if copy is not None:
            copy.count -= 1

    def getItem(self, item: StoreItem) -> StoreItem:
        """retrieves item from cart"""

        for itm in self.items:
            if itm.product.productName == item.product.productName:
                return itm

    def getTotalPrice(self) -> str:
        """loops through all items in cart and returns their cumulative cost"""

        totalPrice = 0
        for item in self.items:
            totalPrice += (item.product.price * item.count)

        return "${:.2f}".format(totalPrice / 100)
