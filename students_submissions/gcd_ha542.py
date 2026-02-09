def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here and no loops allowed
    
    if type(a) != int or type(b) != int:
        print("Error: both input should be integers")
        return None

    #undefined case
    if a == 0 and b == 0:
        print("Error: GCD is undefined when both inputs are zero.")
        return None

    #make values positive
    a = abs(a)
    b = abs(b)

    #base case
    if b == 0:
        return a

    #recursive step
    return gcd(b, a % b)

print(gcd(54, 24))    # 6
print(gcd(48, 18))    # 6
print(gcd(101, 10))   # 1
print(gcd(-24, 18))   # 6
print(gcd(0, 5))      # 5
print(gcd("x", 10))   # Error + None