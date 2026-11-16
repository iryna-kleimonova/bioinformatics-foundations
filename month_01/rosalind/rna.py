
with open('rna.txt', 'r') as f:
    s = f.read().strip()

rna_s = s.replace('T', 'U')
print(rna_s)