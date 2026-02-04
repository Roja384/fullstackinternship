#program for an Online Shopping System using Multilevel Inheritance
class product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price
    def display_product(self):
        print("product name:",self.product_name)
        print("product price:",self.price)
class ElectronicProduct(product):
    def __init__(self,brand,warranty,product_name,price):
        self.brand=brand
        self.warranty=warranty
        super().__init__(product_name,price)
    def display_electronic_product(self):
        self.display_product()
        print("brand:",self.brand)
        print("warranty:",self.warranty)
class mobilephone(ElectronicProduct):
    def __init__(self,product_name,price,brand,warranty,ram,storage):
        super().__init__(product_name,price,brand,warranty)
        self.ram=ram
        self.storage=storage
    def display_mobilephone(self):
        self.display_electronic_product()
        print("ram:",self.ram)
        print("storage:",self.storage)
mobile=mobilephone("samsung galaxy",20000,"samsung","1 year","8GB","128GB")
mobile.display_mobilephone()
