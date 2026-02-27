with open("rosalind_fib.txt", "r") as file:
	cycle, pair_offspring = (int(num) for num in file.read().split(" "))


def fib_rabbit(n, k):
	#base case
	if n <= 1:
		return 1
	#initialize array
	dp = [0] * (n+1)
	dp[1] = 1
	#build up
	for i in range(2, n+1):
		dp[i] = dp[i-1] + dp[i-2]*k
	return dp[n]

result = fib_rabbit(cycle, pair_offspring)

with open("rosalind_fib_result.txt", "w") as solution:
	print(result)
	solution.write(str(result))