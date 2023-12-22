# this_list = ["apple", 1 , True , "apple"]
# [print(x) for x in this_list]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple" and x != "banana"]

print(newlist)

new_list = [x for x in range(10) if x <= 5]
print(new_list)

thislist = ["orange", "mango", "kiwi", "Pineapple", "banana"]
thislist.sort()
print(thislist)