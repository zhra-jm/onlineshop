class User:

    def __init__(self, username, fullname, password, email):
        self.username = username
        self.fullname = fullname
        self.password = password
        self.email = email

    def check_password(self, password):
        return self.password == password

    @classmethod
    def create(cls, username, fullname, password, email):
        if len(password) < 2:
            return 'too short'
        cls(username, fullname, password, email)


class Customer(User):

    def __init__(self, *args, **kwargs):
        super().__init__(username, fullname, password, email)
        self.wallet_amount = 0
        self.is_enable = False

    def __str__(self):
        return self.username

    def set_enable(self):
        self.is_enable = True


class Reseller(User):

    def __init__(self, logo, brand, *args, **kwargs):
        self.logo = logo
        self.brand = brand
        super().__init__(username, fullname, password, email)


class Product:
    product_list = list()

    def __init__(self, upc, name, price=0, description='', reseller=None):
        self.upc = upc
        self.name = name
        self.price = price
        self.description = description
        self.reseller = reseller
        Product.product_list.append(self)

    def __str__(self):
        return f"upc: {self.upc}\t price : {self.price}"

    def is_free(self):
        return self.price == 0
