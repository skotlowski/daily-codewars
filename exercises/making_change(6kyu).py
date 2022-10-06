def make_change(amount):
    result = {}
    if amount >= 50:
        result['H'] = amount // 50
        amount -= 50 * (amount // 50)
    if amount >= 25:
        result['Q'] = amount // 25
        amount -= 25 * (amount // 25)
    if amount >= 10:
        result['D'] = amount // 10
        amount -= 10 * (amount // 10)
    if amount >= 5:
        result['N'] = amount // 5
        amount -= 5 * (amount // 5)
    if amount >= 1:
        result['P'] = amount // 1
        amount -= 1 * (amount // 1)
    return result
