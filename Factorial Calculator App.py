import math

print("Welcome to the Factorial Calculator App")
num = int(input("What number would you like to compute the factorial of? "))

print(str(num), "!=", end=" ")

for x in range(1,num):
    print(x, end="*")
print(str(num))

#USING MATH LIB TO GET FACT
factorial = math.factorial(num)
print("\n\nHere is the result from the math library:")
print("The factorial of", num, "is", factorial)

#USING OWN LOGIC TO GET FACT
fact = 1
for y in range(1, num+1):
    fact = fact * y

print("\n\nHere is the result from my own algorithm:")
print("The factorial of",num, "is", fact)
