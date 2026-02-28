def read_fasta(filename="rosalind_cons.txt"):
	with open(filename, "r") as file:
		current = []
		for line in file:
			line = line.strip()
			if line.startswith(">"):
				if current:
					yield "".join(current[:])
					current = []
			else:
				current.append(line)

		if current:
			yield"".join(current[:])


seqs = list(read_fasta())
seq_len = len(seqs[0])

profile_matrix = [[0]*seq_len for i in range(4)]

cons = []
bases = "ACGT"

for i, col in enumerate(zip(*seqs)):
	# this was the old version
	# a,c,g,t = col.count("A"), col.count("C"), col.count("G"), col.count("T")

	current_count = [col.count(base) for base in bases]

	for base_idx in range(4):
		profile_matrix[base_idx][i] = current_count[base_idx]
	
	cons.append(bases[current_count.index(max(current_count))])

with open("rosalind_cons_result.txt", "w") as solution:
	print(*cons, file=solution, sep="")
	for i in range(4):
		print(f"{bases[i]}:", *profile_matrix[i], file=solution)
