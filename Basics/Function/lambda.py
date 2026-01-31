add=lambda a,b:a+b
sub= lambda a,b: abs(a-b)
mul= lambda a,b: a*b
div= lambda a,b:abs(a/b)
a=5
b=5
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
#condition in lambda function
cond= lambda a: "Even" if a%2==0 else "Odd"
print(cond(3)) 