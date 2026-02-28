with open("rosalind_fibd.txt", "r") as file:
	n, m = (int(number) for number in file.read().split(" "))


def fib_mortal(n, m):
	if n <= 2:
		return 1
	#initialize
	newborn = [0] * (n+1)
	adults = [0] * (n+1)
	
	#base case
	newborn[1] = 1
	adults[2] = 1

	#here we build up from 3 because the first two month no rabbits were born
	for i in range(3, n+1):
		
		newborn[i] = adults[i-1]	
		adults[i] = adults[i-1] + newborn[i-1] - newborn[i-m]

	return (newborn[n] + adults[n])


result = str(fib_mortal(n, m))
print(result)

with open("rosalind_fibd_result.txt", "w") as solution:
	solution.write(result)
