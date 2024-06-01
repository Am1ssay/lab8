def translate_nums(str):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_num = 0
    sum = 0
    for symb in reversed(str):
        num = roman[symb]
        if num < prev_num:
            sum -= num
        else:
            sum += num
        prev_num = roman[symb]
    return sum


if __name__ == "__main__":
    str = input()
    print(translate_nums(str))
