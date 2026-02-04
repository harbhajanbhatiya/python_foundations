def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return factorial(n-1) * n
        
num=int(input("Enter a number to compute its factorial: "))
print(f"The factorial of {num} is {factorial(num)}") 

#Test with 5,0,-3
# Expected Output:
# The factorial of 5 is 120
# The factorial of 0 is 1
# Factorial is not defined for negative numbers
num1=5
print(f"Factorial of {num1} is {factorial(num1)}")
num2=0
print(f"Factorial of {num2} is {factorial(num2)}")
num3=-3
print(factorial(num3))