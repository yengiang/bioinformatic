# Given: A DNA string s of length at most 1000 nt. 
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# Sao lại không and được ở khúc if mà phải tách ra làm 3 if riêng

dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

#count A
lstA = []
for c in dna:
    if c == 'G' or c == 'T' or c == 'C':
        continue
    lstA.append(c)
print(len(lstA))

#count G
lstG = []
for c in dna:
    if c == 'A' or c == 'T' or c == 'C':
        continue
    lstG.append(c)
print(len(lstG))

#count C
lstC = []
for c in dna:
    if c == 'G' or c == 'T' or c == 'A':
        continue
    lstC.append(c)
print(len(lstC))

#count T
lstT = []
for c in dna:
    if c == 'G' or c == 'A' or c == 'C':
        continue
    lstT.append(c)
print(len(lstT))
