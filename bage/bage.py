def knapsack(W, weight, cost, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(cost[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K

