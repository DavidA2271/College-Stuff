import os

from pandas import DataFrame, read_csv

from Products.Product import *


class ProductDatabase:
    """ database of all products

        uses the pandas module to make dataframes which can get and alter data
    """

    # dynamic list of departments in store taken from txt files in Data directory
    productDepartments: list[str] = []

    dbs: dict[str, DataFrame] = {}

    def registerProducts(self):
        """ reads txt files in Data directory, generates Product based off the files content and stores each product
        in a dictionary """

        self.productDepartments.clear()
        self.dbs.clear()

        files = os.listdir("Data")
        for file in files:
            dptName = file.replace(".txt", "")
            # adds name of file to the list of departments
            self.productDepartments.append(dptName)
            data = read_csv(filepath_or_buffer=os.path.join("Data", file), header=[0])
            self.dbs[dptName] = data

    def getDepartment(self, product: Product) -> int:
        """ gets department from product

            will most likely remove in future
        """

        for dept in range(len(self.productDepartments)):
            if product.department == self.productDepartments[dept]:
                return dept

    def saveChanges(self, index: int, current_dept: str, product: Product):
        """ saves changes to product back to csv """

        data = self.dbs[current_dept]

        if current_dept == product.department:
            data.loc[index, 'Product'] = product.productName
            data.loc[index, 'Price'] = product.price
        else:
            new_data = data.drop(index=index)
            self.dbs[current_dept] = new_data
            new_data.to_csv(os.path.join('Data', current_dept + '.txt'), index=False)
            data = self.dbs[product.department]
            data.loc[len(data.index)] = [product.productName, product.price]

        data.to_csv(os.path.join('Data', product.department + '.txt'), index=False)

    def make_new_dept(self, dept: str):
        self.productDepartments.append(dept)
        self.dbs[dept] = DataFrame(columns=['Product', 'Price'])
        file = open(os.path.join('Data', dept + '.txt'), 'w')
        file.write('Product,Price')
        file.close()
