def to_rna(dna_strand):
    rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna_strand = ""
    for nuc in dna_strand:
        rna_strand += rna[nuc]
    return rna_strand
