#dict:Dictionaries are used to store data values in key:value pairs.
      #A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


#1)
d = {
    "name" : "Alan",
    "age" : 18,
    "year" : 2015
}
print(d)


#2)
d  = {
    "name" : "Raj",
    "age" : 21,
    "year" : 2014,
    "year" : 2016
}
print(d)#Duplicate values will overwrite existing values



#3)

d  = {
    "name" : "Raj",
    "age" : 21,
    "year" : 2014,
    "year" : 2016
}

print(len(d))



#4)value in dict can be any data types:

d  = {
    "name" : "AlanRaj",
    "married" : False,
    "year" : 1500,
    "JobPlace" : ["chennai", "pondy", "karanathaka"]
}
print(d)


#5)

d  = {
    "name" : "AlanRaj",
    "married" : False,
    "year" : 1500,
    "JobPlace" : ["chennai", "pondy", "karanathaka"]
}
print(type(d))


#6)dict() method to make a dictionary.

d = dict(name = "Alan", age = 18, year = "1992")
print(d)


#7)To get the value of "year" key


d  = {
    "name" : "AlanRaj",
    "married" : False,
    "year" : 1500,
    "JobPlace" : ["chennai", "pondy", "karanathaka"]
}

x = d["year"]
print(x)#or use get() method

x = d.get("year")
print(x)

x  =d.keys()
print(x)#To get list of all keys in dict

d["color"] = "unknown"
print(d)#to add new item in orginal dict

x = d.values()
print(x)#Return list of all values in dict



#8)pop() to remove item with specified key name


p  = {
    "name" : "AlanRaj",
    "married" : False,
    "year" : 1500,
    "JobPlace" : ["chennai", "pondy", "karanathaka"]
}

p.pop("year")
print(p)

p.popitem()
print(p)#remove last item

