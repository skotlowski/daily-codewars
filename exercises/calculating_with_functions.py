def zero(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 0 * result[1]
        elif result[0] == '//':
            return 0 // result[1]
        elif result[0] == '-':
            return 0 - result[1]
        elif result[0] == '+':
            return 0 + result[1]
    else:
        return 0


def one(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 1 * result[1]
        elif result[0] == '//':
            return 1 // result[1]
        elif result[0] == '-':
            return 1 - result[1]
        elif result[0] == '+':
            return 1 + result[1]
    else:
        return 1


def two(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 2 * result[1]
        elif result[0] == '//':
            return 2 // result[1]
        elif result[0] == '-':
            return 2 - result[1]
        elif result[0] == '+':
            return 2 + result[1]
    else:
        return 2


def three(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 3 * result[1]
        elif result[0] == '//':
            return 3 // result[1]
        elif result[0] == '-':
            return 3 - result[1]
        elif result[0] == '+':
            return 3 + result[1]
    else:
        return 3


def four(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 4 * result[1]
        elif result[0] == '//':
            return 4 // result[1]
        elif result[0] == '-':
            return 4 - result[1]
        elif result[0] == '+':
            return 4 + result[1]
    else:
        return 4


def five(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 5 * result[1]
        elif result[0] == '//':
            return 5 // result[1]
        elif result[0] == '-':
            return 5 - result[1]
        elif result[0] == '+':
            return 5 + result[1]
    else:
        return 5


def six(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 6 * result[1]
        elif result[0] == '//':
            return 6 // result[1]
        elif result[0] == '-':
            return 6 - result[1]
        elif result[0] == '+':
            return 6 + result[1]
    else:
        return 6


def seven(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 7 * result[1]
        elif result[0] == '//':
            return 7 // result[1]
        elif result[0] == '-':
            return 7 - result[1]
        elif result[0] == '+':
            return 7 + result[1]
    else:
        return 7


def eight(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 8 * result[1]
        elif result[0] == '//':
            return 8 // result[1]
        elif result[0] == '-':
            return 8 - result[1]
        elif result[0] == '+':
            return 8 + result[1]
    else:
        return 8


def nine(method: list = False):
    if method:
        result = method
        if result[0] == '*':
            return 9 * result[1]
        elif result[0] == '//':
            return 9 // result[1]
        elif result[0] == '-':
            return 9 - result[1]
        elif result[0] == '+':
            return 9 + result[1]
    else:
        return 9


def plus(number):
    return ['+', number]


def minus(number):
    return ['-', number]


def times(number):
    return ['*', number]


def divided_by(number):
    return ['//', number]
