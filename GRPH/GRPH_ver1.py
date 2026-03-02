import copy

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

K_OVERLAP = 3

fasta_seqs = load_fasta("sample.txt")
# trimmed_seqs = {
# 					key: value[:K_OVERLAP] + value[-K_OVERLAP:] if len(value) > 2*K_OVERLAP else value
# 					for key, value in fasta_seqs.items()

# 					}

bases = "ATCG"
suff_collection = {f + s + t : [] for f in bases for s in bases for t in bases}
pref_collection = copy.deepcopy(suff_collection)


for seq_id, seq_sequence in fasta_seqs.items():
	

	seq_prefix = seq_sequence[:K_OVERLAP]
	seq_suffix = seq_sequence[-K_OVERLAP:]
	
	for p, p_list in pref_collection.items():
		if seq_prefix == p:
			p_list.append(seq_id)


	for s, s_list in suff_collection.items():
		if seq_suffix == s:
			s_list.append(seq_id)


adj_list = []

for p, p_list in pref_collection.items():
	s_list = suff_collection[p]
	for p in p_list:
		for s in s_list:
			if p != s:
				adj_list.append([p,s])

print(adj_list)
		