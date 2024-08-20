class Dish:
    def __init__(self, name="NA", price= 0, rating=1.5):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Dishes: {} | {} | {} ".format(self.name, self.price, self.rating))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
       

#dishes = [Dish(), Dish("Dal Makhani", 250, 3), Dish("Shahi Paneer", 150, 4)]     
"""

print("Dishes:")
for idx in range(len(dishes)):      
     dishes[idx].show() 


"""
