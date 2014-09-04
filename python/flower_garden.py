# !/bin/env python

# http://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
from operator import add

def best_garden(flower_heights, flower_blooms, flower_wilts):
    flowers = zip(flower_heights, flower_blooms, flower_wilts)

    flowers.sort(key=lambda x: x[1])  # sort by bloom times

    best_garden_all = []
    best_garden = [[flowers[0][0]]]
    group_offset = 0

    group_ending_time = flowers[0][2]
    for i in range(1, len(flowers)):
        if flowers[i][0] < best_garden[i - 1 - group_offset][-1] and flowers[i][1] <= group_ending_time:
            best_garden.append([flowers[i][0]] + best_garden[i - 1 - group_offset])
            group_ending_time = max(group_ending_time, flowers[i][2])
        elif flowers[i][0] > best_garden[i - 1 - group_offset][-1] and flowers[i][1] <= group_ending_time:
            best_garden.append(best_garden[i - 1 - group_offset] + [flowers[i][0]])
        else:
            group_offset += len(best_garden)
            best_garden_all.append(best_garden[-1])
            best_garden = [[flowers[i][0]]]
            group_ending_time = flowers[i][2]

    best_garden_all.append(best_garden[-1])
    best_garden_all.sort(key=lambda x: - x[0])

    best_garden_joined = reduce(add, best_garden_all)
    return best_garden_joined

if __name__ == '__main__':
    print best_garden([5,4,3,2,1],
                      [1,1,1,1,1],
                      [365,365,365,365,365])
    print best_garden([5,4,3,2,1],
                      [1,5,10,15,20],
                      [4,9,14,19,24])
    print best_garden([5,4,3,2,1],
                      [1,5,10,15,20],
                      [5,10,15,20,25])
    print best_garden([5,4,3,2,1],
                      [1,5,10,15,20],
                      [5,10,14,20,25])
    print best_garden([1,2,3,4,5,6],
                      [1,3,1,3,1,3],
                      [2,4,2,4,2,4])
    print best_garden([3,2,5,4],
                      [1,2,11,10],
                      [4,3,12,13])
