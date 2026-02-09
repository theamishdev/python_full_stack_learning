""" 
Student Table
attributes
name(public)
__attendance(private)

Methods
mark_present()
mark_absent()
get_attendance()
is_eligible()
"""

class Student:
    def __init__(self, name):
        self.name = name
        self.__attendance = 0
        self.total_classes = 0

    def mark_present(self):
        self.__attendance += 1
        self.total_classes += 1

    def mark_absent(self):
        self.total_classes += 1

    def get_attendance(self):
        if self.total_classes == 0:
            return 0
        return (self.__attendance / self.total_classes) * 100

    def is_eligible(self):
        return self.get_attendance() >= 75

if __name__ == "__main__":
    s1 = Student("Amish")
    s1.mark_present()
    s1.mark_present()
    s1.mark_present()
    s1.mark_absent() 
    
    print(f"Name: {s1.name}")
    print(f"Attendance: {s1.get_attendance()}%")
    print(f"Eligible: {s1.is_eligible()}")