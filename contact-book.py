class Contact:
    def __init__(self, name, number, phone_type):
        self.name = name
        self.number = number
        self.phone_type = phone_type


frank = Contact('Frank Gallow', 8887857777, 'Work')

print(vars(frank))