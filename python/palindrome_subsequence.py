from functools import wraps


def memoize(func):
    cache = {}
    @wraps(func)
    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return inner

@memoize
def longest_palindrome_subsequence(text):
    return longest(0, len(text) - 1, text)

def longest(i, j, p):
    if i == j:
        return 1
    elif p[i] == p[j]:
        return 2 + longest(i + 1, j - 1, p)
    else:
        return max(longest(i + 1, j, p), longest(i, j - 1, p))

if __name__ == '__main__':
    print(longest_palindrome_subsequence('character'))
    assert longest_palindrome_subsequence('character') == 5
