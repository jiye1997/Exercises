#!/usr/bin/python

file=open('plain_genomic_seq.txt')
sequence=file.read()
exon_1=sequence[:62]
intron=senquence[63:89]
exon_2=sequence[90:]
print(exon_1,exon_2)

with open('AJ223353.fasta') as my_file:
    whole_sequence=my_file.read()
    whole_sequence=whole_sequence.replace('\n','')
    whole_sequence.upper()
    print(whole_sequence)
