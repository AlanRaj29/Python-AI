                                  #String Manipulation in py


 #1)strings in Python are arrays of bytes representing unicode characters.
 #2)However, Python does not have a character data type, a single character is simply a string with a length of 1.
 #3)Square brackets can be used to access elements of the string.


#Program:

#1)Strings are array:(Array always start from 0)

a = "Alan RAJ"
print(a[3])#n



#2)Looping through a String:(Since strings are arrays, we can loop through the characters in a string, with a for loop.)

for i in "wallet":
    print(i)



#3)String Lengths:(use len() function to get the length of the string)    

b = "Its Me"#len always start from 1
print(len(b))#6



#4)Check String:(To check if a character is present in a string, we can use the keyword in.)

txt = "Am checking the code now"
print("code" in txt)#True

#Use it in an if statement:

if "code" in txt:
    print("yes, 'code' was here")#yes, 'code' was here
else:
    print("no, 'code' was not here")  

#Check if NOT:(To check if a character is not present in a string, we can use the keyword not in.)

print("code" not in txt)#Flase

#Use it in an if statement:

if "database" not in txt:
    print("yes, 'database' is not persent in txt")#
else:
    print("yes, It was here")    





      




  

  




