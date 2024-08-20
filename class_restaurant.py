from class_dish import Dish
from class_menu import Menu


class Restaurant:
    def __init__(self, name = "NA", phone="NA", email="NA", address="NA", operating_hours=" 10:30 to 12:00", ratings= 1.5, menu=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.operating_hours = operating_hours
        self.ratings = ratings
        self.menu = menu

    def show(self):
        print("RESTAURANT")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Restaurant: {} | {} | {}".format(self.name, self.phone, self.email))
        print("Address: {} | {} | {}".format(self.address, self.operating_hours, self.ratings))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        self.menu.show()


            

restaurant = Restaurant("Ludhiana Veggie Delight", "+91 99999 11111", "veggies@abc.com", 4.5, menu= Menu("Indian Veggie Delight", 3, dishes= [Dish(), Dish("Dal Makhani", 250, 4.5)]))
restaurant.show()





"""
restaurant = Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            dishes=[
                                    Dish(), 
                                    Dish("Dal Makhani", 250, 4.5),
                                    Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        )

restaurant.show()
"""

