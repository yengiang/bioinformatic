# Given: A DNA string s of length at most 1000 nt. 
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# #count A
# lstA = []
# for c in dna:
#     if c == 'G':
#         continue
#     if c == 'T':
#         continue
#     if c == 'C':
#         continue
#     lstA.append(c)
# print(len(lstA))

# #count G
# lstG = []
# for c in dna:
#     if c == 'A':
#         continue
#     if c == 'T':
#         continue
#     if c == 'C':
#         continue
#     lstG.append(c)
# print(len(lstG))

# #count C
# lstC = []
# for c in dna:
#     if c == 'G':
#         continue
#     if c == 'T':
#         continue
#     if c == 'A':
#         continue
#     lstC.append(c)
# print(len(lstC))

# #count T
# lstT = []
# for c in dna:
#     if c == 'G':
#         continue
#     if c == 'A':
#         continue
#     if c == 'C':
#         continue
#     lstT.append(c)
# print(len(lstT))

count_a = 0
count_t = 0
count_g = 0
count_c = 0
for nuc in dna:
    if nuc == 'A':
        count_a += 1
    elif nuc == 'T':
        count_t += 1
    elif nuc == 'G':
        count_g += 1
    else:
        count_c += 1

print(count_a, count_c, count_g, count_t)