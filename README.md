# Bioinformatics_Final_Exam_Part_3
A) After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
a.	Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
b.	Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Example Data:
Given: 
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG

>Rosalind_12
ATCGGTCGAA

>Rosalind_15
ATCGGTCGAGCGTGT

Output:
MVYIADKQHVASREAYGHMFKVCA
