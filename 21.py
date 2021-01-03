a = float(input())
b = float(input())

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b ):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions")

age = add(a, b)
height = subtract(a, b)
weight = multiply(a, b)
iq = divide(a, b)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it anyway

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
