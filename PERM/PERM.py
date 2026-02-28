with open("rosalind_perm.txt") as file:
	n = int(file.read())
	nums = [number for number in range(1,n+1)]

ans, sol = [], []

def backtrack():
	if len(sol) == n:
		ans.append(sol[:])
		return

	for x in nums:
		if x not in sol:
			sol.append(x)
			backtrack()
			sol.pop()


backtrack()


with open("rosalind_perm_result.txt", "w") as solution:
	print(len(ans), file=solution)
	for perm in ans:
		print(*perm, file=solution)
