with open('count_n.txt', 'r') as f:
    s = f.read().strip()

A = s.count("A")
G = s.count("G")
T = s.count("T")
C = s.count("C")

print(A, C, G, T)