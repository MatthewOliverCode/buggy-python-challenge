# Find the bug
def fibonacci(a,b):
    for i in range(0,10):
        a,b = b,a+1
        print(a)

num1 = 0
num2 = 1
fibonacci(num1,num2)
