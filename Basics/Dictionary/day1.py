#mutable
print(dir(dict))
student={
    "name": "Amish",
    "Regd No.": 23,
    "Age": 22,
    "Semester": 6,
    "Roll No.": 2,
}
print(student)
print(student["name"])
print(student.get("favo"))

#---------------------------------------------
list1=[]
list1.extend(student.keys())
print(list1)
print("\n")
list2=[]
list2.extend(student.values())
print(list2)
#----------------------------------------------------
#nested dictionary
dict2 = {
    "languages": {
        "1": "Hindi", 
        "2": "English"
    }, 
    "Technical": {
        "1": "Python", 
        "2": "MERN"
    }
}
print(dict2)
