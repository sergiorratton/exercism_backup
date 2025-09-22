def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    exp1 = a + b >= c
    exp2 = b + c >= a
    exp3 = a + c >= b
    exp4 = a > 0 and b > 0 and c > 0
    set_conditions = {exp1,
                      exp2,
                      exp3,
                      exp4}
    if False in set_conditions:
        return False
    elif a == b == c:
        return True
    else:
        return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    exp1 = a + b >= c
    exp2 = b + c >= a
    exp3 = a + c >= b
    exp4 = a > 0 and b > 0 and c > 0
    set_conditions = {exp1,
                      exp2,
                      exp3,
                      exp4}
    if False in set_conditions:
        return False
    elif a == b or a == c or b == c:
        return True
    else:
        return False

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    exp1 = a + b >= c
    exp2 = b + c >= a
    exp3 = a + c >= b
    exp4 = a > 0 and b > 0 and c > 0
    set_conditions = {exp1,
                      exp2,
                      exp3,
                      exp4}
    if False in set_conditions:
        return False
    elif a != b and a != c and b != c:
        return True
    else:
        return False
