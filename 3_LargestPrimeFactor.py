# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

numberToFindPrimeFactorsOf = 600851475143
factorsOfNum = []
primeFactorsOfNum = []

def checkIfNumIsPrime(factor):
	if factor == 1:
		return False
	else:
		return all(factor % num for num in xrange(2, factor))

for number in xrange(1, numberToFindPrimeFactorsOf + 1):
    if numberToFindPrimeFactorsOf % number == 0:
        factorsOfNum.append(number)

for factor in factorsOfNum:
    print factor
    if checkIfNumIsPrime(factor):
        primeFactorsOfNum.append(factor)

print "The largest prime factor of " + str(numberToFindPrimeFactorsOf) + " is " + str(primeFactorsOfNum[-1])
