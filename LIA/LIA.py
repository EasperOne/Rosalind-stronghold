with open("rosalind_lia.txt", "r") as file:
	k, n = (int(num) for num in file.read().split(" "))

import math
p = 0.25
binom_cumulative = 0
max = 2**k
for i in range(n, max + 1):
	binom_cumulative += math.comb(max, i) * p**i * (1-p)**(max - i)
result = binom_cumulative


with open("rosalind_lia_result.txt", "w") as solution:
	print(result)
	solution.write(str(result))