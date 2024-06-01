from l5 import L5_T1, L5_T2, L5_T3, L5_T4, L5_T5


def test_t1():
    words = ["flow", "fly", "flick"]
    s = L5_T1.prefix(words)
    assert s == "fl"


def test_t2():
    nums = [1, 2, 3, 4, 5, 6, 8]

    assert L5_T2.find_number(nums) == 7


def test_t3():
    assert L5_T3.translate_nums("XIV") == 14


def test_t4():
    assert L5_T4.are_anagrams("listen", "silent", "enlist") == True


def test_t5():
    assert L5_T5.fib_num(10) == 55
