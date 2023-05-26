
def inanna_utu(n: int) -> str:
    """
    A function that checks if a given number n is divisible by 3, 5, or both.
    If n is divisible by 3, return "Inanna!"
    If n is divisible by 5, return "Utu!"
    If n is divisible by both 3 and 5, return "Inanna Utu!"
    If n is not divisible by 3 or 5, return an empty string.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "Inanna Utu!"
    elif n % 3 == 0:
        return "Inanna!"
    elif n % 5 == 0:
        return "Utu!"
    else:
        return ""
