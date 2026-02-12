from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print("Dog sound:")
    dog.sound()
    print("\nCat sound:")
    cat.sound() 