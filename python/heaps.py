

def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def format_heap(A):
    i = 1
    heap = []
    level = 1
    while i < len(A) - 1:
        heap.append(str(A[i:i + 2**(level - 1)]))
        i += 2 ** (level - 1)
        level += 1
    return "\n".join(heap)


def build_max_heap(A):
    for i in range((len(A) - 2)/ 2, 0, -1):
        max_heapify(A, i)
    return A


def heap_maximum(A):
    return A[1]


def heap_extract_max(A):
    if len(A) == 2:
        return A[1], None
    else:
        curr_max = A[1]
        A[1] = A[len(A) - 1]
        A = A[:-1]
        max_heapify(A, 1)
    return curr_max, A

if __name__ == '__main__':
    A = [1, 1, 2, 3, 33, 12, 11, 5, 2, 5, 43, 12, 4]

    build_max_heap(A)
    while A:
        max_val, A = heap_extract_max(A)
        print(max_val)
