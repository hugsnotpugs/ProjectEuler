''' Find the difference between the sum of the squares of the first one hundred natural numbers 
    and the square of the sum '''

def square_diff(max_int):
    sum_value = 0
    squared_value = 0
    for i in range(max_int+1):
        sum_value += i
        squared_value += i**2
    
    return (sum_value**2 - squared_value)


print square_diff(100)
