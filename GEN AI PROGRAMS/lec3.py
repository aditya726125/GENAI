my_list = [8, 9 , 20 , 27, 7, 5, 2 , 4, 1, 6, 3]
print(sorted(my_list, reverse= True))

#sort - this method convert list in increasing order or decreasing order.

list1 = [8, 9 , 20 , 27, 7, 5, 2 , 4, 1, 6, 3]
my_list.sort(reverse= True)
print(my_list)

#Append() - This method add item at end of list and item take as a argument.
my_list.append(726)
print(my_list)

#extend() - This method merge the list with another list.
list1 = [8, 9 , 20 , 27, 7, 5, 2 , 4, 1, 6, 3, 45 , 67]
list2 = [45, 67, 89]
list1.extend(list2)
print(list1)

#Pop()- This method remove the item from the list and return the removed item.
my_list = [ 69, 47, 49, 29]
print(my_list.pop(2))

#Remove() - This method remove the item from the list but it does not return the removed item.
list3 = [89, 45, 67, 45, 90]
print(list3.remove(89))