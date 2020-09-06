class User:
    def __init__(self, name, user_choice):
        self.user_tacos = 5
        self.name = name
        self.default_points = 0
        self.user_choice = user_choice

    def give_taco(self):
        if self.user_choice == 'y':
            self.user_tacos -= 1
        return self.user_tacos

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.default_points, self.user_tacos)


user1 = User("Jamie", input("Would you like to give a Taco? "))
print(user1)
