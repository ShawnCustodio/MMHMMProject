def load_fasta(path):
    sequence = []
    with open(path, "r") as f:
        for line in f:
            if line.startswith(">"):
                continue          # skip FASTA header
            sequence.append(line.strip().upper())
    return "".join(sequence)

seq = load_fasta(r"C:\Users\shawn\OneDrive\Github Repo\MMHMMProject\Sequences Files\ecolik12.fasta")

print("Genome length:", len(seq))
print("First 100 bases:", seq[:100])

from collections import Counter

counts = Counter(seq)
total = len(seq)

freqs = {base: counts[base] / total for base in ["A", "C", "G", "T"]}

print("Base counts:", counts)
print("Base frequencies:", freqs)
