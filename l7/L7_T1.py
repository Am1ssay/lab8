from math import sqrt as s


def step_num(n):
    n = n + 1
    return int(((1 / s(5)) * (((1 + s(5)) / 2)**n - ((1 - s(5)) / 2)**n)))


if __name__ == "__main__":
    n = int(input("Введите номер ступеньки: "))
    print(step_num(n))
