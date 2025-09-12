#create arrays: 1d array
import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)

#2d array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2) #output: [[1 2 3] [4 5 6]]

#calculate sum of all elements in array
print(np.sum(arr1)) #output: 15
mean_value = np.mean(arr2)
print(mean_value) #output: 3.5
print(np.sum(arr2)) #output: 21

#calculate area of circle
def circle_area(radius):
    pi = 3.14159
    area = pi * radius**2
    return area
area = circle_area(5)
print(area) #output: 78.53975

#calculate factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 
      
print(factorial(5)) #output: 120

#calculate fibonacci sequence
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
print(fibonacci(10)) #output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]