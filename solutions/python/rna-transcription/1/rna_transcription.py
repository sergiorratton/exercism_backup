def to_rna(dna_strand):
    dict_dna_rna = {"G" : "C",
                    "C" : "G",
                    "T" : "A",
                    "A" : "U"}
    string_retorno = ""
    for letra in dna_strand:
        if letra in dict_dna_rna:
            retorno = dict_dna_rna[letra]
            string_retorno += retorno
    return string_retorno