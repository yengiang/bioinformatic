# Given: A DNA string s of length at most 1000 nt. 
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

#count A
count_A = 0
for c in dna:
    if c == 'A':
        count_A += 1
print(count_A)

#count G
count_G = 0
for c in dna:
    if c == 'G':
        count_G += 1
print(count_G)

#count C
count_C = 0
for c in dna:
    if c == 'C':
        count_C += 1
print(count_C)

#count T
count_T = 0
for c in dna:
    if c == 'T':
        count_T += 1
print(count_T)
