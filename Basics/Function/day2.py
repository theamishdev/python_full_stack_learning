x=23
def check():
    global a                #to call global value in function
    a=a-2
    print(a)    

check()
def add(a,b):
    return (a+b)

def mul(a,b):
    return a*b
def div(a,b):               #function taking placeholder is called Parameter
    return a/b
def sub(a,b):
    return abs(a-b)

print(add(10,2))           #value being passed is known as Arguement
print(mul(24,22))
print(div(12,8))
print(sub(8,16))
a=add(12,24)
print(a)