#Gobal Keyword:

            ###To create a global variable inside a function, you can use the global keyword.


def myfunc():
    global x
    x = "Alan Raj"
myfunc()
print("My Name Is "+ x)    



           ###Also, use the global keyword if you want to change a global variable inside a function.

x = "Raj"
def func():
    global x
    x = "Alan"
func()
print("My Name Is " + x)     