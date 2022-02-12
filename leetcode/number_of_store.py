def my_function(K, A):
    res = 0
    house = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 1:
                house.append([i+1,j+1])
    L = len(house)-1

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != 1:
                for h in house:
                    if abs(h[0] - i-1) + abs(h[1] -j - 1) <= K:
                        if h == house[L]:
                            res += 1
                        else:
                            continue
                    elif abs(h[0] - i-1) + abs(h[1] -j - 1) > K:
                        break
            else:
                continue
    return res


if __name__ == "__main__":
    a = [[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0],[1, 0, 0, 0],[0, 0, 0, 0]]
    c =[[0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]]
    b = my_function(4,a)
    print(b)




