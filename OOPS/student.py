class Student:
    def __init__(self, name, roll_no, marks, subject):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.subject = subject

    def __str__(self):
        return f"Roll No: {self.roll_no} | Name: {self.name} | Subject: {self.subject} | Marks: {self.marks}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def display_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("\nList of Students:")
            for student in self.students:
                print(student)

# Demonstration
if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Create students
    s1 = Student("Amish", 101, 85, "Python")
    s2 = Student("Rahul", 102, 90, "Data Science")
    s3 = Student("Rohit", 103, 78, "Web Dev")

    # Add students to system
    sms.add_student(s1)
    sms.add_student(s2)
    sms.add_student(s3)

    # Display all students
    sms.display_all_students()
