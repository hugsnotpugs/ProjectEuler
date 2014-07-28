''' Find the smallest positive number that is evenly divisible by all numbers 1 through 20 '''

### Range is inclusive of range_max
def smallest_divisor(range_min, range_max):
    factors = [i for i in range(range_min, range_max+1)][::-1] # descending order
    for i in range(len(factors)):
        for factor in factors[i+1:]:
            if factors[i]%factor == 0:
                factors.remove(factor) # remove smaller factors that are components of larger ones
    
    divisor = max(factors)
    i = 0
    while i < len(factors): # < and not <= since indexing starts from 0
        if divisor%factors[i] != 0:
            divisor += max(factors) # step up by largest factor
            i = 0
        else:
            i += 1
    
    return divisor
    
print smallest_divisor(1, 20)
