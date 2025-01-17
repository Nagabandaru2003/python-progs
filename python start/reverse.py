
#reverse() will reverse the original object

li = [10,5,20,7,40]
print("before reverse: ",li)
li.reverse()
print("After reverse: ",li)

#reversed(iterable_object): 
li2 = [11,6,8,22]
reversed_li2=list(reversed(li2))
print(li2) 
print(reversed_li2)

li3 = [1,5,2,9]
new_reverse_li3 = list(reversed(li3))
li3.reverse()
print(new_reverse_li3)