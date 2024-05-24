def test_func(sum_num):
    result = sum_num(range(1, 101))
    print(result)
dy = lambda x: sum(x)
test_func(dy)

