def to_rna(string):
    dna = {'G':'C','C':'G','T':'A','A':'U'};
    rna = '';
    try:
        for c in string:
            rna = rna + dna[c];
        return rna
    except KeyError:
        return '';
