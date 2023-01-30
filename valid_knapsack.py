def valid_knapsack(X, pairs, weights, knapsack_capacity):
    """
    Return True iff X is a feasible solution.
    """

    # check for right format
    if len(X) != len(weights):
        print("len(X) != len(weights)")
        raise ValueError

    for pair in pairs:
        if type(pair) != tuple:
            print(f"Pair {pair} is not a tuple")
            raise ValueError
        
        elif len(pair) != 2:
            print(f"Length of pair {pair} != 2")
            raise ValueError

    # actual algorithm:

    # no invalid pairs:
    for i, j in pairs:
        if (X[i] == 1) and (X[j] == 1):
            return False

    # total weight less/equal than maximum capacity:
    w = [weights[i] for i in range(len(X)) if (X[i] == 1)]
    total_weight = sum(w)
    if total_weight > knapsack_capacity:
        return False

    return True

if __name__ == "__main__":
    X = eval(input().split(":")[1])
    pairs = eval(input().split(":")[1])
    weights = eval(input().split(":")[1])
    knapsack_capacity = eval(input().split(":")[1])

    retval = valid_knapsack(X, pairs, weights, knapsack_capacity)
    print(retval)