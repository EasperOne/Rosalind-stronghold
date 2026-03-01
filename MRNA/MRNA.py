# Number of codons for each amino acid
codon_counts = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, # Phe, Leu, Ser, Tyr, Cys, Trp
    'P': 4, 'H': 2, 'Q': 2, 'R': 6,                # Pro, His, Gln, Arg
    'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2,          # Ile, Met, Thr, Asn, Lys
    'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4,          # Val, Ala, Asp, Glu, Gly
    'STOP': 3                                       # UAA, UAG, UGA
}

with open("rosalind_mrna.txt", "r") as file:
    aa_string = file.read().strip()


total_codon = 1
for aa in aa_string:
    total_codon *= codon_counts[aa] % 1000000

total_codon = total_codon * 3 % 1000000

with open("rosalind_mrna_result.txt", "w") as solution:
    print(total_codon, file=solution)