def zigzag(numbers):
    """actually one array would be enought to solve it"""
    if not numbers:
        return 0
    numbers = list(numbers)
    up = [numbers[0]]
    down = [numbers[0]]

    up_len = 1
    down_len = 1
    for i in range(1, len(numbers)):
        if up_len % 2:
            if numbers[i] > up[-1]:
                up.append(numbers[i])
                up_len += 1
            else:
                up[-1] = numbers[i]
        else:
            if numbers[i] < up[-1]:
                up.append(numbers[i])
                up_len += 1
            else:
                up[-1] = numbers[i]
        if down_len % 2 == 0:
            if numbers[i] > down[-1]:
                down.append(numbers[i])
                down_len += 1
            elif numbers[i] < down[-1]:
                down[-1] = numbers[i]
        else:
            if numbers[i] < down[-1]:
                down.append(numbers[i])
                down_len += 1
            else:
                down[-1] = numbers[i]
    print up
    print down
    print('up_len', up_len)
    print('down_len', down_len)
    return max(up_len, down_len)



def test_solution():
    assert zigzag([1, 7, 4, 9, 2, 5]) == 6
    assert zigzag([ 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 ]) == 7
    assert zigzag([ 44 ]) == 1
    assert zigzag([ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]) == 2
    assert zigzag([ 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32 ]) == 8
    assert zigzag([ 374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
        600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
        67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
        477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
        249, 22, 176, 279, 23, 22, 617, 462, 459, 244 ]) == 36


if __name__ == '__main__':
    test_solution()
