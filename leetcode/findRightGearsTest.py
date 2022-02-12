import findRightGears
import random
def test():
    test = []
    num = random.randint(2,20)
    gaps = []
    for i in range(num):
        test.append(random.randint(1,10000))
    test.sort()
    #print(test)
    for i in range(len(test)-1):
        gaps.append(test[i+1]-test[i])
    #print(gaps)
    result = findRightGears.solution(test)

    radius = 0
    #validating result
    if len(gaps) %2 == 0 and result != [-1, -1]:
        radius = result[0]
    elif len(gaps) %2 == 1 and result != [-1, -1]:
        radius = result[0]

    i = 0
    j = 0
    if len(gaps) %2 == 0 and radius != 0:
        while i < len(test):
            if gaps[i] > radius >= 1:
                radius = gaps[i] - radius
                if radius >= 1:
                    continue
                elif radius < 1:
                    print("test not passed" + str(test))
            elif gaps[i] <= radius or radius < 1:
                print("test not passed" + str(test))
            i += 1
        print("test passed")
    elif len(gaps) %2 ==1 and radius != 0:
        while j < len(test):
            if 3*gaps[j] > radius >= 3:
                radius = 3*gaps[j] - radius
                if radius >= 3:
                    continue
                elif radius < 3:
                    print("test not passed" + str(test))
            elif 3*gaps[j] <= radius or radius < 3:
                print("test not passed" + str(test))
            j += 1
        print("test passed")

    """  
    for i in range(len(gaps)):
        if gaps[i] > radius >= 1:
            radius = gaps[i] - radius
            if radius >= 1:
                continue
            elif radius < 1:
                return [-1, -1]
        elif gaps[i] <= radius or radius < 1:
            return [-1, -1]
    return [result, 1]
    """
if __name__ == "__main__":
    while True:
        test()