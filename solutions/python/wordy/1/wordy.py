def answer(question):
    dict_ops = {"plus" : "+",
                "minus" : "-",
                "multiplied by" : "*",
                "divided by" : "/"}
    question = question.replace("What is ", "")
    question = question.replace("?", "")
    for op in dict_ops:
        if op in question:
            question = question.replace(op, dict_ops[op])
    lista_string = question.split()
    try:
        resultado = int(lista_string[0])
    except:
        raise ValueError("syntax error")
    i = 1
    while i < len(lista_string):
        try:
            operacao = lista_string[i]
            num = int(lista_string[i+1])
            
            if operacao == '+':
                resultado += num
            elif operacao == '-':
                resultado -= num
            elif operacao == '*':
                resultado *= num
            elif operacao == '/':
                resultado /= num
            i += 2
        except:
            if "cubed" in question:
                raise ValueError("unknown operation")
            else:
                raise ValueError("syntax error")
    return resultado
        
        