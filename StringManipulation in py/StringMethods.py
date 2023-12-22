a = "alan raj"
print(a.capitalize())#The first character is the upper case.
print(a.title())#The first character in every word of the string is an upper case.
print(a.upper())#All the characters in a given string are uppers case.
a = "Alan RAj"
print(a.casefold())#To Converts string into lower case.
print(a.center(18))#To center align the string.
print(a.center(18, "_"))#Using the "_" as the padding character.
a = "25","85","65","25","25","65"
print(a.count("25"))#Returns the number of times a specified value occurs in a string.
a = "Hello, Welcome to my world"
print(a.endswith("my world"))#Flase if didn't end with my world("IT WAS TRUE").
print(a.endswith("my"))#("IT WAS FLASE")
a = "H\te\te\tl\tl\to"
print(a.expandtabs(8))#Set the tab size to 8 whitespaces.
a = "Hello Hello"
print(a.find("e"))#	Searches the string for a specified value and returns the position of where it was found.
print(a.find("e",3))#it will search after array of 3.
print(a.replace("o","u"))#Replaces a specified phrase with another specified phrase.
a = "AlanRaj"
print(a.isalpha())#Check if all the characters in the text are letters.
a = "Alan001"
print(a.isalnum())#Checks whether all the characters in a given string is alphanumeric or not meaning alphabet letter (a-z) and numbers (0-9).
                  #Example of characters that are not alphanumeric: (space)!#%&? etc.
a = "alan raj"
print(a.isupper())#To Checks if all characters in the string are uppercase   
print(a.islower())#TO Checks if all characters in the string are lowercase      
x = "         its        "
y = x.strip()
print("hai",y,"me")#Remove spaces at the beginning and at the end of the string.
print(len(x.lstrip()))#Remove spaces to the left of the string and give its len.
print(len(x.rstrip()))#Remove spaces to the right of the string.
s = "its my world"
print(s.partition("my"))





