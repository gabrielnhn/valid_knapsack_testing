def valid_knapsack(X: list, pairs: list, weights: list, knapsack_capacity: int) -> bool:
    """Return True iff X is a valid knapsack."""

    # check for right format
    if len(X) != len(weights):
        # print("len(X) != len(weights)")
        raise ValueError

    for pair in pairs:
        if type(pair) != tuple:
            # print(f"Pair {pair} is not a tuple")
            raise ValueError
        
        elif len(pair) != 2:
            # print(f"Length of pair {pair} != 2")
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

import os

if __name__ == "__main__":

    files = os.listdir()
    inputs = [file for file in files if file.endswith(".in")]
    inputs.sort()

    for file in inputs:
        with open(file) as f:

            X = eval(f.readline().split(":")[1])
            pairs = eval(f.readline().split(":")[1])
            weights = eval(f.readline().split(":")[1])
            knapsack_capacity = eval(f.readline().split(":")[1])

            try:
                expected_output = f.readline().split(":")[1]
            except:
                print("ERROR ", file)
                exit()


            print(f"File {file}.\n\t Returns '", end="")

            try:
                retval = valid_knapsack(X, pairs, weights, knapsack_capacity)
                print(retval, end="', ")
            
            except ValueError:
                print("ValueError", end=", ")

            print(f"expected '{expected_output[1:]}'.")
