#dictionary - collection of key-value pairs, it is mutable type data structure, every key value seperated by colon, the combination of key and value is known as item and every item seperated by comma - all item enclosed by curly braces.

#my_dict={"Name":"kritika","College":"Shoolini"}
        # key1      value1   key2    value2


my_dict = {"Name":"kritika","College":"Shoolini"}
print(my_dict["College"])

#method in dictionary
#keys() -- this method return keys of dictionary
print(my_dict.keys())
print(my_dict.values())

# items()-- this method return item of the dictionary
print(my_dict.items())

#gat()-- this method find value and take key as a argument
print(my_dict.get("Class","Hahahahaha"))

#update()-- this method update dictionary and take dictionary as argument
my_dict.update({"Age":20})
print(my_dict)

my_dict.update({"Name":"Aditya"})
print(my_dict)

#conditional statement
#if-- this statement execute when condition is true
#elif-- this statement execute when condition is true
#else-- this statement execute when if and elif are not executed

age = int(input("enter your age: "))
if age>70:
    print("You are too old for marry")
elif age<18:
    print("You are too young for marry")
else:
    print("We will find perfect match for you")
