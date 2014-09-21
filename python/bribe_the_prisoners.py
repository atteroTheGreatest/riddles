# https://code.google.com/codejam/contest/189252/dashboard#s=p2&a=2
# bribe the prisoners
# dynamic programming solution

def bribe_dp(prisoners, total):
    cache = {}
    def solve(a, b):
        if (a, b) in cache:
            return cache[(a, b)]
        r = 0
        for p in prisoners:
            if p >= a and p <= b:
                temp = (b - a) + solve(a, p - 1) + solve(p + 1, b)
                if temp < r or r == 0:
                    r = temp

        cache[(a, b)] = r
        return r
    return solve(1, total)


if __name__ == '__main__':
    print(bribe_dp([3], 8))
    print(bribe_dp([3, 6, 14], 20))
    lines = []
    with open('python/C-large-practice.in') as f:
        for line in f:
            lines.append(line.strip())
    with open('python/C-large-practice.out', 'w+') as f:
        total = 0
        for i, line in enumerate(lines[1:]):
            if i % 2 == 0:
                total = int(line.split()[0])
            else:
                to_release = [int(n) for n in line.split()]
                total_bribe = bribe_dp(to_release, total)

                f.write("Case #%s: %s\n" % (i / 2 + 1, total_bribe))
