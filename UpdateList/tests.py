from list import access, move_to_front, transpose, counter, count

def mtf():
    sample = [1, 2, 3, 4, 5, 1]
    expected_l = [[1, 2, 3, 4, 5], [2, 1, 3, 4, 5], [3, 2, 1, 4, 5],
                  [4, 3, 2, 1, 5], [5, 4, 3, 2, 1], [1, 5, 4, 3, 2]]
    l = [1, 2, 3, 4, 5]
    for (index, elem) in enumerate(sample):
        _, l = access(elem, l, move_to_front)
        assert expected_l[index] == l


def tr():
    sample = [1, 2, 3, 4, 5, 1]
    expected_l = [[1, 2, 3, 4, 5], [2, 1, 3, 4, 5], [2, 3, 1, 4, 5],
                  [2, 3, 4, 1, 5], [2, 3, 4, 5, 1], [2, 3, 4, 1, 5]]
    l = [1, 2, 3, 4, 5]
    for (index, elem) in enumerate(sample):
        _, l = access(elem, l, transpose)
        assert expected_l[index] == l


def cnt():
    sample = [1, 2, 3, 4, 5,
              2, 2, 5, 4, 4, 4]
    expected_l = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5],
                  [2, 1, 3, 4, 5], [2, 1, 3, 4, 5], [2, 5, 1, 3, 4],
                  [2, 4, 5, 1, 3], [2, 4, 5, 1, 3], [4, 2, 5, 1, 3]]
    l = []
    for (index, elem) in enumerate(sample):
        _, l = access(elem, l, count)
        assert expected_l[index] == l


cnt()
mtf()
tr()
