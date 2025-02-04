def to_rna(dna_strand):
    rna = "GCTA"
    new_rna = "CGAU"

    swap = str.maketrans(rna,new_rna)

    return dna_strand.translate(swap)
