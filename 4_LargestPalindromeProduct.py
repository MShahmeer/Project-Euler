threeDigitNumbers1 = []
threeDigitNumbers2 = []
palindromes = []


def reverse_int(i):
    return int(str(i)[::-1])


for number in range(100, 1000):
    threeDigitNumbers1.append(number)

threeDigitNumbers2 = threeDigitNumbers1

for number in threeDigitNumbers1:
    for num in threeDigitNumbers2:
        potentialPalindrome = number * num
        reverseOfPotentialPalindrome = reverse_int(potentialPalindrome)
        if potentialPalindrome == reverseOfPotentialPalindrome:
            palindromes.append(potentialPalindrome)

largestPalindrome = max(palindromes)
print(largestPalindrome)
