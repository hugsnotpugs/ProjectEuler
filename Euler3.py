''' This solution is based on the fundamental theorem of arithmetic:
    Each integer > 1 is either prime or a unique product of primes

    Methodology:
    1. Factors n into 2 components: current_factor and n/current_facto s.t. current_factor >= 2
    2. Reduces n by current_factor until current_factor is no longer a factor
    3. Incrementally increases current_factor and repeats steps 1-2 until n is prime '''


def max_pfactor(n): 
    if type(n) != type(1) or int(n) <= 1:
        return None
    
    current_factor = 2
    while n > current_factor:
        # Reduce n until n isn't divisble by current_factor
        if n%current_factor == 0:
            n = n/current_factor
            current_factor = 2
            
        # Step up current_factor, then repeat n reduction process
        else:
            if current_factor == 2:
                current_factor += 1
            else: 
                current_factor += 2
    return n

print max_pfactor(600851475143)
