def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a % b


if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(20, 8))
    print(multiply(6, 7))
    print(divide(20, 4))
    print(power(2, 3))
    print(modulo(10, 3))
