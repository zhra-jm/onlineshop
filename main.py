from Models import User, Customer, Reseller, Product


if __name__ == '__main__':
    c1 = Reseller.create('z', 'zahra', '1', 'zahra@email.com')
    print(c1)