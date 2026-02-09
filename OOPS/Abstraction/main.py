from abc import ABC, abstractmethod

class Thor_hammer(ABC):
    @abstractmethod
    def worthy(self):
        pass

    def fly(self):
        print(f"rotate and fly")

    def thunder(self):
        print(f"throw thunder")

class Thor(Thor_hammer):
    def worthy(self):
        print(f"I'm worthy")

class CaptainAmerica(Thor_hammer):
    def worthy(self):
        print(f"I'm also worthy")

class Hulk(Thor_hammer):
    def worthy(self):
        print("I'm not worthy")  # Hulk cannot lift it

if __name__ == "__main__":
    objects = [Thor(), CaptainAmerica(), Hulk()]
    
    for obj in objects:
        print(f"--- Can {type(obj).__name__} lift the hammer? ---")
        obj.worthy()
        if type(obj).__name__ != "Hulk":  # Only worthy ones can use powers
            obj.fly()
            obj.thunder()
        else:
            print("Cannot fly or use thunder.")
        print()