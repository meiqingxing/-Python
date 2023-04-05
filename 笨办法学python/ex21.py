def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b   #return返回加和后的值

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLY {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just function!")

age = add(30,5)  #将调用add函数后返回的值赋给age
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
# 上面的程序，需要注意的是python不是从后往前工作，而是从里向外工作
print("That become: ", what, "Can you do it by hand?")