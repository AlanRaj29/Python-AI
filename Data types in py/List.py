a = [1,2,3]
print(a)#ordered
a[0] = 3
print(a)#changeable
a = [1,2,3,1]
print(a)#allow dupicate value
print(len(a))#list length
print(a[1])#Access items



#List items (str,int,bool)

l1 = ["Alan","Raj"]
l2 = [78,24,52]
l3 = [True,False,False]
print(l1,l2,l3)


#A list can contain different data types:

l1 = ["Alan", 3, True, 55, "Hai"]
print(l1)
print(type(l1))

#in key in list:

l = ["its", "me"]

if "its" in l:
    print("yes,'its' was here")
else:
    print("no,not here")   


#Insert methos():To insert new item without replacing existing values
       
l.insert(2, "AlanRaj")    
print(l)

#Append() method:To add an item to end of the list

l.append("Da")
print(l)

#extend() method:To append elements from one list to another

a = ["Apple","orange"]
b = ["mango",]
a.extend(b)
print(a)

#Remove() method:

a.remove("orange")
print(a)

#If there are more than one item with the specified value, the remove() method removes the first occurance:

c = ["Apple","orange","Apple","Kiwi"]
c.remove("Apple")
print(c)

#pop() method: removes the specified index.

c.pop(2)
print(c)

#Remove the last item:


ed = ["Apple","orange","Apple","Kiwi"]
ed.pop()
print(ed)

#clear() method: empties the list.

ed.clear()
print(ed)


#sort() method that will sort the list alphanumerically, ascending, by default:

ed = ["Apple","orange","Apple","Kiwi"]
ed.sort()
print(ed)


d = [100, 50, 65, 82, 23]
d.sort()
print(d)


#sort descending, use the keyword argument reverse = True.

d.sort(reverse = True)
print(d)