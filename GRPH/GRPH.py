def load_fasta(filename):

	seqs = {}
	current_id = ""

	with open(filename, "r") as f:
		for line in f:
			line = line.strip()

			if not line:
				continue

			if line.startswith(">"):
				current_id = line[1:]
				seqs[current_id] = ""
			else:
				seqs[current_id] += line

	return seqs


def find_overlap(seq_dict: dict, k=3) -> list:

	prefix_map = {}

	for seq_id, sequence in seq_dict.items():
		prefix = sequence[:k]
		
		if prefix not in prefix_map:
			prefix_map[prefix] = []
		
		prefix_map[prefix].append(seq_id)

	adj_list = []

	for suffix_id, sequence in seq_dict.items():
		suffix = sequence[-k:]
		if suffix in prefix_map:
			for prefix_id in prefix_map[suffix]:
				if suffix_id != prefix_id:
					adj_list.append((suffix_id, prefix_id))

	return adj_list


fasta_seqs = load_fasta("rosalind_grph.txt")

results = find_overlap(fasta_seqs)

print(results)
with open("rosalind_grph_result.txt", "w") as solution:
	for s, t in results:
		print(f"{s} {t}", file=solution)

		