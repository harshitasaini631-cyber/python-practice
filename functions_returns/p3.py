def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):   
        # n**0.5 means square root of n. n = 6 , 36**0.5 = 6
        if n % i == 0:
            return False
    
    return True



num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")



# After 6 (which is √36), the factors start repeating in reverse.

# So if a number has a factor bigger than √n,
# it must also have one smaller than √n.

# That means:
#  If no number ≤ √n divides n,
# then no number greater than √n will divide it either.

# So we save time.

# Why int(n**0.5) + 1?

# Because:

# range() stops before the last number.

# We add +1 to include the square root value.

# Example:
# If n = 25

# √25 = 5

# range(2, 5) → checks 2, 3, 4 (misses 5 )

# So we write:
# range(2, 6) → checks 2, 3, 4, 5 