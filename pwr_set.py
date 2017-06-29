import math

import timeit


# def power_set(lst):

#     N = len(lst)

#     set_list = [[]]
#     count = 0

#     for i in range(2 ** len(lst)):
#         sub_list = []

#         for j in xrange(int(math.sqrt(i))):
#             count += 1
#             if (i >> j) % 2 == 1:
#                 sub_list.append(lst[j])
#                 # print sub_list
#         set_list.append(sub_list)

#     print set_list
#     print count

def power_set(lst):

    # N = len(lst)

    set_list = [[]]
    # count = 0

    for i in xrange(2 ** len(lst)):
        sub_list = []

        for j in xrange(len(lst)):
            # count += 1
            if 2**j & i != 0:
                sub_list.append(lst[j])
                # print sub_list
        set_list.append(sub_list)

    return set_list
    # print count


# start1 = timeit.default_timer()

def power_set_2(lst):
    """For every element in the list we have seen so far, add new element to 
    all combinations of elements prior to num_iters
    """
    subsets = [[]]
    # num_iters = 0

    for i in range(len(lst)):
        for j in range(len(subsets)):
            # print "i: %s, j: %s" % (i, j)
            # print "subsets before: %s" % subsets
            subsets.append(subsets[j] + [lst[i]])
            # print "subsets after: %s" % subsets
            # num_iters += 1

    return subsets
    # print num_iters

# stop1 = timeit.default_timer()


def time_solution(name, func, iterations):
    start = timeit.default_timer()
    i = 0
    while i < iterations:
        func(range(6))
        i += 1
    stop = timeit.default_timer()
    print "%s's function time: %s" % (name, stop - start)

time_solution("blerina", power_set, 10000)
time_solution("alain", power_set_2, 10000)
