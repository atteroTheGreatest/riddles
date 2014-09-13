# Longest common subsequence
import pprint
pp = pprint.PrettyPrinter(indent=4)


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    b = []
    c = []
    for i in range(m):
        c.append([0] * n)
        b.append(['.'] * n)

    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '\\'
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = '^'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = '<-'
    return c, b

pp.pprint(lcs_length('ABCDDAB', 'VACDDB'))
