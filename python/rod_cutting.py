
def cut_rod(p, n):
    if n == 0:
        print('n == 0')
        return 0
    q = -1000
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    print('N', n)
    print('q', q)
    return q


def bottom_up_cut_rod(p, n):
    r = [0]

    for j in range(1, n + 1):
        q = - 1000
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r.append(q)
    print(r[n])
    return r[n]

if __name__ == "__main__":
    p = [1, 2, 3, 5, 7, 9, 14]
    n = 6

    print("regular cut rod")
    cut_rod(p, n)
    print("bottom up cut rod")
    bottom_up_cut_rod(p, n)
