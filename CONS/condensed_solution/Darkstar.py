with open("../sample.txt", "r") as f:
    strands = [x.strip() for x in f.readlines()]

# except from the parsing which gotta have to be improved to handle FASTA line-ending
# the code is itself pretty good

matrix = zip(*strands)

# here the matrix is the col matrix

profile_data = [dict((base, col.count(base)) for base in "ACGT") for col in matrix]
# return a list where each column is now count dictionary of 4 bases [{A:, C:, G:, T:}, ...]


"""
When you use max("ACGT", key=col.count), Python is doing this:

Check 'A': how many in col? (Let's say 5)

Check 'C': how many in col? (Let's say 2)

... and so on.
it returns the letter with the max count
"""
consensus = "".join(max(d, key=d.get) for d in profile_data)
print(consensus)

# 2. Print Profile Matrix
for base in "ACGT":
    # Get the count of 'base' from every dictionary in the list
    counts = [d[base] for d in profile_data]
    print(f"{base}: {' '.join(map(str, counts))}")