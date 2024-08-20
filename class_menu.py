from class_dish import Dish


class Menu:
    def __init__(self, name= "NA", number_of_dishes= 0, dishes=[]):
        self.name = name
        self.number_of_dishes = number_of_dishes
        self.dishes = dishes
    
    def show(self):
        print("Menu:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Menu: {} | {} ".format(self.name, self.number_of_dishes))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("Dishes:")
        for idx in range(len(self.dishes)):
            self.dishes[idx].show() 


#menu = Menu("Kings foodie", 3)
#menu.show()
        

#dishes = [Dish(), Dish("Dal Makhani", 250, 3), Dish("Shahi Paneer", 150, 4)]
