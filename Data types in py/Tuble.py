#Same as list but this was unchangable or immutabe


#1)Tuble are immutable but we can convert the tuble into list ,thn change the list, and convert the list back to tuble

x = (55,25,85)
y = list(x)
y[0] = 66
z = tuple(y)
print(z)

#2)Add tuble to tuble

x = (55,25,85)
y = (65,)
x +=y
print(x)



#3)Tubles are immutable so we cant change values from it but we can by turning it into list

x = (55,25,85)
y = list(x)
y.remove(x[1])
z = tuple(y)
print(z)



#4)unpacking the tuble

x = (55,25,85)

(num1, num2, num3) = x

print(num1)
print(num2)
print(num3)




#5)using Asterisk*:
   #If the number of variables is less than the number of values add an * to the variable name and the values will be assigned to the variable as a list:

x = (55,25,85,65,45,32)

(num1, num2, *num3) = x

print(num1)
print(num2)
print(num3)

#Add a list of values to num2:

x = (55,25,85,65,45,32)
(num1, *num2, num3) = x
print(num1)
print(num2)
print(num3)



#6)index() Method:Use to found the given value of index where it was found

x = (55,25,85,65,45,32)
y = x.index(85)
print(y)



#7)count() Method-Returns the number of times a specified value occurs in a tuple

x = (55,25,85,65,45,32,55)
y = x.count(55)
print(y)





#)del keyword:delete the tuble completely

x = (55,25,85)
del x
print(x)#this will raise an error because the tuple no longer exists








