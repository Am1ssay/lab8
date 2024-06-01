from l6 import L6


def test_list():
    listt = L6.LinkedList()
    listt.append(5)
    listt.append(2)
    listt.append(3)
    listt.append(4)
    listt.append(1)
    assert listt.__str__() == "5 2 3 4 1 "
    listt.sort_list()
    assert listt.__str__() == "1 2 3 4 5 "
