# prime number checker

def is_prime(num):
    if num < 2:
        return False

    # Check divisibility up to the square root of n
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Example usage:
print(is_prime(75))

