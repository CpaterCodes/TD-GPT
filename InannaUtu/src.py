
def inanna_utu(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "Inanna Utu!"
    elif n % 3 == 0:
        return "Inanna!"
    elif n % 5 == 0:
        return "Utu!"
    else:
        return str(n)
