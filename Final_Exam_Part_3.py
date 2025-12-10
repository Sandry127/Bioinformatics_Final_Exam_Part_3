#Read the FASTA sequences
sequences = []
current = ""
with open("input.fasta") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current != "":
                sequences.append(current)
                current = ""
        else:
            current += line
    if current != "":
        sequences.append(current)

# The first sequence is the main DNA
dna = sequences[0]

# All the rest are introns
introns = sequences[1:]

#Remove introns from the DNA
for intron in introns:
    dna = dna.replace(intron, "")

#Transcribe DNA to RNA
rna = dna.replace("T", "U")

#Translation table for converting codons to amino acids
codon_table = {
    'UUU':'F','CUU':'L','AUU':'I','GUU':'V',
    'UUC':'F','CUC':'L','AUC':'I','GUC':'V',
    'UUA':'L','CUA':'L','AUA':'I','GUA':'V',
    'UUG':'L','CUG':'L','AUG':'M','GUG':'V',
    'UCU':'S','CCU':'P','ACU':'T','GCU':'A',
    'UCC':'S','CCC':'P','ACC':'T','GCC':'A',
    'UCA':'S','CCA':'P','ACA':'T','GCA':'A',
    'UCG':'S','CCG':'P','ACG':'T','GCG':'A',
    'UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
    'UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
    'UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E',
    'UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E',
    'UGU':'C','CGU':'R','AGU':'S','GGU':'G',
    'UGC':'C','CGC':'R','AGC':'S','GGC':'G',
    'UGA':'Stop','CGA':'R','AGA':'R','GGA':'G',
    'UGG':'W','CGG':'R','AGG':'R','GGG':'G'
}
#Translate RNA to protein
protein = ""
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    if len(codon) < 3:
        break
    amino = codon_table.get(codon)
    if amino == "Stop":
        break
    protein += amino

#For protein sequence output
print(protein)