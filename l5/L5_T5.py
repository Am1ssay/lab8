from math import sqrt as s


def fib_num(n):
    return int(((1 / s(5)) * (((1 + s(5)) / 2)**n - ((1 - s(5)) / 2)**n)))


if __name__ == "__main__":
    n = int(input())
    print(fib_num(n))
