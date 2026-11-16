pairs = {
    'A': 'T',
    'G': 'C',
    'T': 'A',
    'C': 'G'
}

reverse_complement = ''
with open('revc.txt', 'r') as f:
    s = f.read().strip()
    r = s[::-1]

for base in r:
    reverse_complement += pairs[base]

# Version 2: Using str.translate() and str.maketrans()
# table = str.maketrans('ATGC', 'TACG')
# reverse_complement = s.translate(table)[::-1]

# Version 3: Using Biopython
# from Bio.Seq import Seq
# reverse_complement = Seq(s).reverse_complement()