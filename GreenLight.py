######################################################################
# Green lights.
#
#
######################################################################
import numpy


def greenlight(p, k):
    """
    Calculate the probability of k lights be green.
    :param p: 1-d array, every item in array represents the probability of corresponding light to be green
    :param k: number of green light, should be non-negative integer
    :return: the probability of k lights be green
    """

    # number of lights
    n = len(p)

    if k > n:
        raise Exception("Number of green lights should not larger than number of all lights.")

    # no lights
    if n == 0:
        return 1

    # get array of probabilities for all green
    agps = all_true_pro(p)
    # print('All green probabilities:')
    # print(agps)

    np = [1-item for item in p]
    # get array of probabilities for all green
    arps = all_true_pro(np)
    # print('All red probabilities:')
    # print(agps)

    return rec_func(p, k, agps, arps)


def rec_func(p, k, agps, arps):
    """
    Calculate the probability of k lights be green, with all green probabilities array 'agps'
    and all red probabilities array 'arps'.
    :param p: 1-d array, every item in array represents the probability of corresponding light to be green
    :param k: number of green light, should be non-negative integer
    :param agps: 1-d array, i-th item is the probability of all pre (i+1) lights all be green
    :param arps: 1-d array, i-th item is the probability of all pre (i+1) lights all be red
    :return: the probability of k lights be green
    """
    n = len(p)
    if k == n:
        return agps[n - 1]
    if k == 0:
        return arps[n - 1]

    return rec_func(p[:-1], k, agps, arps) * (1 - p[n-1]) + rec_func(p[:-1], k - 1, agps, arps) * p[n-1]


def all_true_pro(p):
    """
    Get all true probabilities array.
    :param p: 1-d array, every item in array represents the probability of corresponding light to be green or red
    :return: 1-d array, size same with input array, ith item is the probability of all pre (i+1) lights all be green
    or all be red
    """
    if len(p) == 0:
        raise Exception("Empty Array.")

    ans = []
    tmp = 1
    for item in p:
        tmp *= item
        ans.append(tmp)

    return ans


def dynamic_planning(p, k):
    """
    Calculate the probability of k lights be green.
    :param p: 1-d array, every item in array represents the probability of corresponding light to be green
    :param k: number of green light, should be non-negative integer
    :return: the probability of k lights be green
    """
    # number of lights
    n = len(p)
    if k > n:
        raise Exception("Number of green lights should not larger than number of all lights.")
    # no lights
    if n == 0:
        return 1
    # get array of probabilities for all green
    agps = all_true_pro(p)
    np = [1 - item for item in p]
    # get array of probabilities for all green
    arps = all_true_pro(np)
    if k == n:
        return agps[n-1]
    if k == 0:
        return arps[n-1]
    p_arr = numpy.zeros((n+1, n+1))
    p_arr[0][0] = 1
    for i in range(1, n):
        p_arr[i][i] = agps[i-1]
        p_arr[0][i] = arps[i-1]
    # populating
    for j in range(1, n+1):
        for i in range(1, j):
            if i > k:
                break
            else:
                p_arr[i][j] = p_arr[i][j-1]*(1-p[j-1]) + p_arr[i-1][j-1]*p[j-1]

    return p_arr[k][n]


if __name__ == '__main__':
    p = [0.2, 0.3, 0.1, 0.5, 0.6]
    k = 4
    print(greenlight(p, k))
    print(dynamic_planning(p, k))
