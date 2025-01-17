li = input("enter space sepetared elemets")
print(li, type(li))
li = li.split()
print(li)
li = list(map(int,li))
print(li)



# tup = tuple(map(int,input("enter space seperated elements").split()))
# print(tup)


li = list(map(int,input().split()))
print([i for i in li if i%2 == 0])

