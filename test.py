#this page is for codeware challenges 

def dig_pow(n, p):
    # Convert n to a string to access each digit
    digits = str(n)
    # Initialize the sum
    total = 0
    # Calculate the sum of digits raised to consecutive powers starting from p
    for i, digit in enumerate(digits):
        total += int(digit) ** (p + i)
    # Check if total is divisible by n
    if total % n == 0:
        return total // n
        print(total // n)
        print(total )
    else:
        return -1

# Test cases
print(dig_pow(89, 1))     # Output: 1
print(dig_pow(92, 1))     # Output: -1
print(dig_pow(695, 2))    # Output: 2
print(dig_pow(46288, 3))

print(24//5)