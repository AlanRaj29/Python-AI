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


