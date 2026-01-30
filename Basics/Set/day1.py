#mutable
list1=(4,4,12,34,53)
set3=set(list1)
print("Set conversion",set3)
set1={4,5,12,34,54,0}
set2={4,12,42,0,122}
print("Union of set 1 and 2: ",set1.union(set2))
print("checks if set1 is disjoint of set2: ",set1.isdisjoint(set2))
print("check if subset or not: ",set1.issubset(set2))
print("find intersection: ",set1.intersection(set2))
set4=set(dir(set))
print("prints list of inbuilt methods: ",set4)