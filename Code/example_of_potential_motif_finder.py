# Description: This script demonstrates how to find potential motifs in a given amino acid sequence.

# Import the re module to use regular expressions
import re

# Fictional Amino acid sequence to search for motifs
aa_seq = 'LAATLLTGCUAUUA'


# Preprocess the amino acid sequence to remove any non-alphabet characters
aa_seq = re.sub(r'[^A-Z]', '', aa_seq)
print(aa_seq)

# Find all matches of the pattern "AXX(X)A" or "LXX(X)L" in the amino acid sequence
matches = re.findall("(A.{2,3}A|L.{2,3}L)", aa_seq)

# Print out the motifs found
for match in matches:
    print("Motif found:", match)

# Print out the total number of motifs found and how many are A based and L based
print("Total number of motifs found:", str(len(matches)))
print("Total number of A based motifs found:", str(len([match for match in matches if match[0] == 'A'])))
print("Total number of L based motifs found:", str(len([match for match in matches if match[0] == 'L'])))