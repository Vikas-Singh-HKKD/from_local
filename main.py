# write a python code to print prime numbers from 1 to 100
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def print_primes(limit):
    primes = []
    for num in range(1, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
if __name__ == "__main__":
    prime_numbers = print_primes(100)
    print("Prime numbers from 1 to 100:", prime_numbers)
# This code defines a function to check if a number is prime and another function to print all prime numbers up to a specified limit.
# The main block calls the function to print prime numbers from 1 to 100.
# The output will be a list of prime numbers in that range.
# The code is complete and will print the prime numbers from 1 to 100 when executed.
# Output:
# Prime numbers from 1 to 100: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# The code is complete and will print the prime numbers from 1 to 100 when executed.

# The code is complete and will print the prime numbers from 1 to 100 when executed.