def recite(start_verse, end_verse):
    dict_dias = {1 : "first",
                 2 : "second",
                 3 : "third",
                 4 : "fourth",
                 5 : "fifth",
                 6 : "sixth",
                 7 : "seventh",
                 8 : "eighth",
                 9 : "ninth",
                 10 : "tenth",
                 11 : "eleventh",
                 12 : "twelfth"}
    dict_numeros = {1 : "one",
                    2 : "two",
                    3 : "three",
                    4 : "four",
                    5 : "five",
                    6 : "six",
                    7 : "seven",
                    8 : "eight",
                    9 : "nine",
                    10 : "ten",
                    11 : "eleven",
                    12 : "twelve"}
    dict_frases = { "one" : "a Partridge in a Pear Tree.",
                    "two" : "two Turtle Doves, ",
                    "three" : "three French Hens, ",
                    "four" : "four Calling Birds, ",
                    "five" : "five Gold Rings, ",
                    "six" : "six Geese-a-Laying, ",
                    "seven" : "seven Swans-a-Swimming, ",
                    "eight" : "eight Maids-a-Milking, ",
                    "nine" : "nine Ladies Dancing, ",
                    "ten" : "ten Lords-a-Leaping, ",
                    "eleven" : "eleven Pipers Piping, ",
                    "twelve" : "twelve Drummers Drumming, "}
    lista_strings = []
    for i in range(start_verse, end_verse + 1):
        lista_verso_atual = []
        numero_inicio = dict_dias[i]
        verso_inicial_atual = f"On the {numero_inicio} day of Christmas my true love gave to me: "
        lista_verso_atual.append(verso_inicial_atual)
        contador = i
        while contador > 0:
            if contador == 1 and i != 1:
                nome_numero = dict_numeros[contador]
                frase_numero = dict_frases[nome_numero]
                frase_numero_1 = "and " + frase_numero
                lista_verso_atual.append(frase_numero_1)
                contador -= 1
            else:
                nome_numero = dict_numeros[contador]
                frase_numero = dict_frases[nome_numero]
                lista_verso_atual.append(frase_numero)
                contador -= 1
        string_final = ""
        for item in lista_verso_atual:
            string_final += item
        lista_strings.append(string_final)
    return lista_strings