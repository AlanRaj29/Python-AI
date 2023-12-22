#Sets: are used to store multiple items in a single variable.
#Set items are unchangeable, but we can remove items and add new items.

#1)

s = {1,2,3}
print(s)#unordered
s = {1,2,3,1}
print(s)#Not allowed duplicates value
s = {1,2,3,"Alan","Raj",True}
print(s)#Considered 1 and True as same
s = {1,2,3,"Alan","Raj",True,0,False}
print(s)#Considered 0 and False as same
print(len(s))
s.add("Orange")
print(s)#Add() method


#2)update() method:To add two set

a = {1,2,3}
b = {4, 5, 6}
a.update(b)
print(a)

#Add Any Iterable:update() method does not have to be a set it can be any iterable object (tuples, lists, dictionaries etc.).

a = {1,2,3}
b = [4, 5, 6]
a.update(b)
print(a)
a.remove(5)#If the item to remove does not exist, discard() will raise an error.
print(a)#Remove() method
a.discard(5)#If the item to remove does not exist, discard() will NOT raise an error.
print(a)#Remove using discard()
a.pop()
print(a)#pop() to remove random method


#union():returns a new set with all items from both sets.

s1 = {1, 2 , 3}
s2 = {4, 5, 6}
s3 = s1.union(s2)
print(s3)


#intersection_update():Keep only dupicate value

s1 = {1, 2 , 3}
s2 = {4, 5, 6, 3}
s1.intersection_update(s2)
print(s1)

#symmetric_difference_update():Keep only the element not present in both sets.

s1 = {1, 2 , 3}
s2 = {4, 5, 6, 3}
s1.symmetric_difference_update(s2)
print(s1)





