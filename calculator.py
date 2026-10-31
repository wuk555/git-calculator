def add(a, b):
    result = a + b
    return result


print(add(10, 5))


def subtract(a, b):
    result = a - b
    return result


print(subtract(20, 8))


def multiply(a, b):
    return a * b


print(multiply(6, 7))


def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b


print(divide(20, 4))