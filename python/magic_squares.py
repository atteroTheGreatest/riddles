# Magic square problem

from __future__ import division
from collections import defaultdict
import random
import itertools
import copy


SQUARE_SIZE = 5


def compute_magic_value(size):
    min = 1
    max = size ** 2
    return (min + max) / 2 * size


def transpose(matrix):
    num_of_rows = len(matrix[0])
    transposed = [[] for x in xrange(num_of_rows)]
    for row in matrix:
        for j, x in enumerate(row):
            transposed[j].append(x)
    return transposed


def compute_violations(square, magic_value):
    violation = 0
    row_violations = defaultdict(int)
    column_violations = defaultdict(int)
    for i, row in enumerate(square):
        current_violation = abs(sum(row) - magic_value)
        violation += current_violation
        row_violations[i] = current_violation

    for i, column in enumerate(transpose(square)):
        current_violation = abs(sum(column) - magic_value)
        violation += current_violation
        column_violations[i] = current_violation

    square_size = len(square[0])
    left_diagonal = 0
    right_diagonal = 0
    for x in range(square_size):
        left_diagonal += square[x][x]
        right_diagonal += square[square_size - 1 - x][x]
    violation += abs(left_diagonal - magic_value)
    violation += abs(right_diagonal - magic_value)
    return (violation, column_violations, row_violations)


def generate_square(size):
    valid_numbers = [x for x in xrange(1, size ** 2 + 1)]
    random.shuffle(valid_numbers)
    square = [[valid_numbers.pop() for x in xrange(size)] for x
              in xrange(size)]
    return square


def print_square(square):
    for row in square:
        print row


def swap_elements(square, x1, y1, x2, y2):
    square[x1][y1], square[x2][y2] = square[x2][y2], square[x1][y1]


def get_most_violating(columns_violations, row_violations):
    ys = sorted(columns_violations.iteritems(), key=lambda x: x[1])
    xs = sorted(row_violations.iteritems(), key=lambda x: x[1])
    points = []
    for y in ys:
        for x in xs:
            points.append((x[0], y[0]))
    return points


def main():
    print "Magic square solving!"

    found = False
    while not found:
        square = generate_square(SQUARE_SIZE)
        magic_value = compute_magic_value(SQUARE_SIZE)
        violation, columns, rows = compute_violations(square, magic_value)

        while violation > 0:
            violation, columns, rows = compute_violations(square, magic_value)
            most_violatating = get_most_violating(columns, rows)
            best_pair = most_violatating[:2]
            best_result = violation

            for pair in itertools.combinations(most_violatating, 2):
                square_copy = copy.deepcopy(square)
                first = pair[0]
                second = pair[1]
                swap_elements(square_copy, first[0], first[1], second[0],
                              second[1])
                cur_violation, c, r = compute_violations(square_copy,
                                                         magic_value)
                if cur_violation < best_result:
                    best_result = cur_violation
                    best_pair = [first, second]

            if best_result < violation:
                first = best_pair[0]
                second = best_pair[1]
                swap_elements(square, first[0], first[1], second[0], second[1])
                violation, columns, rows = compute_violations(square,
                                                              magic_value)
            else:
                # Stuck in local minimum :<
                break
        else:
            found = True
            print "We have a winner:"
            print_square(square)
if __name__ == '__main__':
    main()
