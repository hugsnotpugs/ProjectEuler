''' Project Euler #4:
    Find the largest palindrome that is the product of two 3 digit numbers '''

### The factor range is inclusive
def max_palindrome(min_factor, max_factor):
    palindrome = 0
    for i in range(min_factor, max_factor+1): 
        for j in range(min_factor, max_factor+1):
            product = i*j
            length = len(str(product))
            loc = int(round(length/float(2), 0))
            if str(product)[:loc] == str(product)[loc:][::-1]:
                if product >= palindrome:
                    palindrome = product
                    factor1 = i
                    factor2 = j
                    
    return (palindrome, factor1, factor2)

max_palindrome(100, 999)
