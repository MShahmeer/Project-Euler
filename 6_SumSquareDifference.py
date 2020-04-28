"""The sum of the squares of the first ten natural numbers is 385.
The square of the sum of the first ten natural numbers is 3025.

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""

square_sum = 0
sum = 0

for i in range(1, 101):
    square_sum += i**2
    sum += i

print(abs(square_sum - sum**2))
