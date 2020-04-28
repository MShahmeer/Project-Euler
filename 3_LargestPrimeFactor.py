# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
largest_prime_factor = 1


def is_prime(n: int) -> bool:
    flag = True
    for j in range(2, n):
        if n % j == 0:
            flag = False
            break
    return flag


while num != 1:
    for i in range(2, num + 1):
        if is_prime(i) and num % i == 0:
            largest_prime_factor = i
            num = num//i
            break

print(largest_prime_factor)
