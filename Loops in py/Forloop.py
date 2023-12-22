#for loop repeats a number of statements a specified number of times

fruits = ["Apple","Orange","Grape"]

for fruit in fruits:
    print("current fruit is: ",fruit)
print("you are welcome")    


#Find factorial using for loop

num = int(input("NUmber: "))

factorial = 1

if num < 0:
    print("Number must be in positive")
elif num == 0:
    print("fatorial = 1")
else:
    for i in range(1,num + 1):
        factorial = factorial * i
        print(factorial)
print("Factorial of",num,"is",factorial)                
