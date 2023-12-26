#Nested For Loop in Python:
#Allows use a loop inside another loop
#1
for i in range(3):
    for j in range(2):
        print(i,j)


rows = 3
columns = 4


#2
for row in range(rows):
    for col in range(columns):
        print(f"({row},{col})")#f is used to create f-strings
        #which is a formatted string literal that allows you to embed Python expressions inside string literals.
        #The f-string evaluates the expressions inside the curly braces {} and replaces them with their values.
        #ex:
name = "Alice"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")



#3

size = 5

for i in range(size):
    for j in  range(i + 1):
        print("*",end=" ")#end parameter is used to what to print at the end of the output.
    print()               #By default, the end parameter is set to a newline character (\n) means after print it move to next line.
#However, if you change the end parameter to a space character (" "), then the print function will print a space after the output, instead of moving to the next line.



#4)Multiplecation table
    
for i in  range(1,11):
    for j in range(1,11):
        #print(i * j,end="\t") 
        print(i,"*",j,"=", i*j)   
    print()    





                  ##########################Nested while loop ################################

# A nested while loop that prints a pattern of stars

i = 1
while i <= 5:

    j = 1
    while j <= i:
        print("*",end=" ")
        j+=1
    print()
    i+=1   




                 ##########################Nested while loop ################################
       

rows = int(input("Enter the number of rows:"))

for i in range(rows):
    
    j = 0
    while j < i+1:
        print("*",end=" ")
        j+=1
    print()    

