list1 = [9, 3, 4, 8, 8]
list2 = [4, 5, 7, 2, 10]
print("list 1 : " + str(list1))
print("list 2 : " + str(list2))
list3 = []
for i in range(0, len(list1)):
    list3.append(list1[i] + list2[i])
print("Resultant list: " + str(list3))