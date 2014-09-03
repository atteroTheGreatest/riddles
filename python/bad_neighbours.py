# !/bin/env python

# http://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009

def collect_founds(neighbours):

    if neighbours[-1] > neighbours[0]:
        neighbours = neighbours[1:]
    else:
        neighbours = neighbours[:-1]

    if len(neighbours) == 1:
        return neighbours[0]

    best_so_far = [neighbours[0], max(neighbours[0], neighbours[1])]

    if len(neighbours) > 2:
        for i in range(2, len(neighbours)):
            best_now = max(best_so_far[i - 2] + neighbours[i], best_so_far[i - 1])
            best_so_far.append(best_now)

    return max(best_so_far)


if __name__ == '__main__':
    print(collect_founds([10, 3, 2, 5, 7, 8]))
    print(collect_founds([11, 15]))
    print(collect_founds([ 7, 7, 7, 7, 7, 7, 7]))
    print(collect_founds([ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
    print(collect_founds([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
                          6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
                          52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]))
