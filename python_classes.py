class User():

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.registered = False

    # class methods and properties:
    @property
    def is_registered(self):
        return self.registered
    

user_1 = User("Ann", "ann@gmail.com", 20)

print(user_1.name)
print(user_1.age)
print(user_1.email)

print(user_1.is_registered)


        
        
