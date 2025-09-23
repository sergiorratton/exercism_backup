def roman(number):
    numero_romano = ""
    while number > 0:
        if number >= 1000:
            number -= 1000
            numero_romano += "M"
            continue
        if number < 1000 and number >= 900:
            number -= 900
            numero_romano += "CM"
            continue
        if number < 900 and number >= 500:
            number -= 500
            numero_romano += "D"
            continue
        if number < 500 and number >= 400:
            number -= 400
            numero_romano += "CD"
            continue
        if number < 400 and number >= 100:
            number -= 100
            numero_romano += "C"
            continue
        if number < 100 and number >= 90:
            number -= 90
            numero_romano += "XC"
            continue
        if number < 90 and number >= 50:
            number -= 50
            numero_romano += "L"
            continue
        if number < 50 and number > 40:
            number -= 40
            numero_romano += "XL"
            continue
        if number < 40 and number >= 10:
            number -= 10
            numero_romano += "X"
            continue
        if number < 10 and number >= 9:
            number -= 9
            numero_romano += "IX"
            continue
        if number < 9 and number >= 5:
            number -= 5
            numero_romano += "V"
            continue
        if number < 5 and number >= 4:
            number -= 4
            numero_romano += "IV"
            continue
        if number < 4:
            number -= 1
            numero_romano += "I"
            continue
    return numero_romano