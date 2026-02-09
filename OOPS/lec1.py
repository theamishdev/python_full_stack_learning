import selenium

class Dog:
    def set_name(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog()
dog1.set_name("dogesh bhai")

dog2 = Dog()
dog2.set_name("chintu bhai")


dog1.bark()
dog2.bark()