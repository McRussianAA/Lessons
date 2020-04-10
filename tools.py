funct = {
    'sum': lambda x, y: x + y,
    'pow': lambda x, y: x ** y,
    'mult': lambda x, y: x * y
}


def Graphik(a, b, funct):
    args = []
    step = (b - a) / 1000
    x = a
    while x <= b:
        args.append(x)
        x += step
    map(funct, args)


def FamilySqaure(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


Graphik(1, 10, lambda x: x ** 2 + 2 * x - 10)
f = FamilySqaure(10, -2, 11)


def CheckValidMail(mail: str) -> bool:
    '''

    :param mail:
    :return:
    '''
    if type(mail) != str:
        raise TypeError()

    import re
    pattern = "(^[a-zA-Z0-9_+-]+(\.[a-zA-Z0-9_+-]+)*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    return re.match(pattern=pattern, string=mail.strip().lower()) != None
