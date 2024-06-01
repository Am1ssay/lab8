from l7 import L7_T1, L7_T2, L7_T3, L7_T4


def test_tt1():
    n = 6
    assert L7_T1.step_num(n) == 13


def test_tt2():
    a, b = L7_T2.find_mx_bfstr("кокошнель")
    assert a == 'ко' and b == 2


def test_tt3():
    map = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    assert L7_T3.paths(map) == 15


def test_tt4():
    str1 = "intention"
    str2 = "execution"
    assert L7_T4.str_hint(str1, str2) == 5
