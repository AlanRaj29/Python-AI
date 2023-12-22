#Local & Gobal variable:
              
              ###If you create a variable with the same name inside a function, this variable will be local, 
              # and can only be used inside the function. The global variable with the same name will remain as it was, 
              # global and with the original value.


x = "Raj"

def func():
    x = "Alan"
    print("My Name is " + x)
func()

print("My Name Is " + x)