"""Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum."""


def phi(n: int) -> [int]:
    output = []
    for i in range(1, n):
        relative_prime = True
        for j in range(2, i + 1):
            if i % j == 0 and n % j == 0:
                relative_prime = False
        if relative_prime:
            output.append(i)
    return output


maximum = 0
value = 2

for num in range(2, 1000001):
    phi_num = phi(num)
    n_div_phi = num / len(phi_num)
    print("n: " + str(num) + ", phi(n): " + str(len(phi_num)) + ", n/phi(n): "
          + str(n_div_phi))
    if n_div_phi > maximum:
        maximum = n_div_phi
        value = num

print(maximum, value)
