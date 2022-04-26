# Given: A DNA string s of length at most 1000 nt. 
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

#count A
lstA = []
for c in dna:
    if c != 'A':
        continue
    lstA.append(c)
print(len(lstA))

#count G
lstG = []
for c in dna:
    if c != 'G':
        continue
    lstG.append(c)
print(len(lstG))

#count C
lstC = []
for c in dna:
    if c != 'C':
        continue
    lstC.append(c)
print(len(lstC))

#count T
lstT = []
for c in dna:
    if c != 'T':
        continue
    lstT.append(c)
print(len(lstT))
