"""
Employee sal system
Requirement => create a class employee
Attributes => name, sal, emp_id
Methods => add_bonu(amount), add bouns to the sal, is_high_earner(), returns True if sal >= 100,000 else False
display() => prints emp_id, name, sal, High Earner status(yes/no)
"""
class Employee:
    def __init__(self, emp_id, name, sal):
        self.emp_id = emp_id
        self.name = name
        self.sal = sal

    def add_bonus(self, amount):
        self.sal += amount

    def is_high_earner(self):
        return self.sal >= 100000

    def display(self):
        status = "Yes" if self.is_high_earner() else "No"
        print(f"ID: {self.emp_id} | Name: {self.name} | sal: {self.sal} | High Earner Status: {status}")

if __name__ == "__main__":
    emp1 = Employee(101, "Amish", 110000)
    emp2 = Employee(102, "Bittu", 80000)

    print("Before Bonus")
    emp1.display()
    emp2.display()

    print("\nAfter Bonus")
    emp2.add_bonus(25000)  
    emp2.display()