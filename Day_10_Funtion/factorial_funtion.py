def factorial_funtion(n):
    factorial = 1
    if n <= 1:
        return 1
    else: 
        for i in range(1,n+1,1):
            factorial *= i
        return factorial
n = int(input())
print('Factorial of', n,'is:',factorial_funtion(n))
        
