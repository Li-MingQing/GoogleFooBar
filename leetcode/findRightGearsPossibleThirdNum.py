import findRightGears
def possibleThird():
    for i in range(7, 51):
        for j in range(i+1, 51):
            testCase = [1, 6, i, j]
            result = findRightGears.solution(testCase)
            if result != [-1, -1]:
                print([i,j])

if __name__ == "__main__":
    print(0 %2)
