var sumOfSquares = Int()
var squareOfSums = Int()

for i in 1...100 {
    sumOfSquares += i*i
}

for i in 1...100 {
    squareOfSums += i
}

squareOfSums = squareOfSums * squareOfSums

print(squareOfSums - sumOfSquares)
