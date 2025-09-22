def is_paired(input_string):
    lista_chars = [("(", ")"), ("[", "]"), ("{", "}")]
    qtd_abre_parenteses = input_string.count("(")
    qtd_fecha_parenteses = input_string.count(")")
    qtd_abre_bracket = input_string.count("[")
    qtd_fecha_bracket = input_string.count("]")
    qtd_abre_brace = input_string.count("{")
    qtd_fecha_brace = input_string.count("}")
    if qtd_abre_parenteses != qtd_fecha_parenteses or qtd_abre_bracket != qtd_fecha_bracket or qtd_abre_brace != qtd_fecha_brace:
        return False
    if qtd_abre_parenteses > 0 and qtd_fecha_parenteses > 0:
        if input_string.index(")") < input_string.index("("):
            return False
    if qtd_abre_brace > 0 and qtd_fecha_brace > 0:
        if input_string.index("}") < input_string.index("{"):
            return False
    if qtd_abre_bracket > 0 and qtd_fecha_bracket > 0:
        if input_string.index("]") < input_string.index("["):
            return False
    if qtd_abre_parenteses > 0 and qtd_fecha_parenteses > 0 and qtd_abre_brace > 0 and qtd_fecha_brace > 0:
        if input_string.index("(") < input_string.index("{") and input_string.index(")") < input_string.index("{"):
            return True
        if input_string.index("(") < input_string.index("{") and input_string.index(")") < input_string.index("}"):
            return False
        if input_string.index("{") < input_string.index("(") and input_string.index("}") < input_string.index(")"):
            return False
    if qtd_abre_parenteses > 0 and qtd_fecha_parenteses > 0 and qtd_abre_bracket > 0 and qtd_fecha_bracket > 0:
        if input_string.index("(") < input_string.index("[") and input_string.index(")") < input_string.index("["):
            return True
        if input_string.index("(") < input_string.index("[") and input_string.index(")") < input_string.index("]"):
            return False
        if input_string.index("[") < input_string.index("(") and input_string.index("]") < input_string.index(")"):
            return False
    if qtd_abre_brace > 0 and qtd_fecha_brace > 0 and qtd_abre_bracket > 0 and qtd_fecha_bracket > 0:
        if input_string.index("{") < input_string.index("[") and input_string.index("}") < input_string.index("["):
            return True
        if input_string.index("{") < input_string.index("[") and input_string.index("}") < input_string.index("]"):
            return False
        if input_string.index("[") < input_string.index("{") and input_string.index("]") < input_string.index("}"):
            return False
    return True