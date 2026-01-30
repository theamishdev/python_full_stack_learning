#LIST Learning(Mutable) 
print(dir(list))
a=[1,2,3]
print(id(a))
help(a.extend)


#merge list
b=[2,3,4,5]
c=[10,2,4,5]
d=b+c
print(b+c) 

#print element at specific index
d=['mobile','hii','byee']
print((d[1][0]))
d.pop(2)
print(d)

#reverse and limit based in loop
d = dir(list)
d.reverse()                  
for item in d[:11]:
    print(item)


#count method
e=[100,200,300,400]
count=0
for item in e:
    if(item==200):                       #wlse use count method print(e.count(200))
        count+=1
print(count)



#sort
e.sort(reverse=True)           #descending
print(e)
e.sort(reverse=False)          #ascending
print(e)

list1=[1,23,4,53,56]
print(max(list1))
list1.reverse()
print(list1)
print(min(list1))