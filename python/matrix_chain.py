BIG_NUMBER = 1000000

def memoized_matrix_chain(p):
    m = []
    N = len(p)
    for x in range(N):
        m.append([BIG_NUMBER] * N)

    return lookup_chain(m, p, 0, N - 1)

def lookup_chain(m, p, i, j):
    if m[i][j] < BIG_NUMBER:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = (lookup_chain(m, p, i, k)
                 + lookup_chain(m, p, k + 1, j)
                 + p[i-1] * p[k] * p[j])

            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]

if __name__ == "__main__":
    print(memoized_matrix_chain([4, 6, 10, 10, 2, 18]))
