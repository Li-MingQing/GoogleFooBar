def solution(pegs):
    gaps = []
    result = 0
    for i in range(len(pegs) - 1):
        gaps.append(pegs[i + 1] - pegs[i])
    #print(gaps)
    for i in range(len(gaps)):
        result += -gaps[i] if (i + 1) % 2 == 0 else gaps[i]
    result = 2 * result
    #print(result)

    #judge first number greater than 2
    """
    if len(gaps) %2 == 1:
        b = result
        if b < 6:
            return [-1, -1]
    elif len(gaps) %2 == 0:
        b = result
        if b < 2:
            return [-1, -1]
    """
    """
        if len(gaps) %2 == 1:
            result = [result,3]
        elif len(gaps) %2 == 0:
            result = [result,1]
        if len(gaps) % 2 == 0 and result >= 1:
            radius = result
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
    # validating the result
    if len(gaps) % 2 == 0 and result >= 2:
        radius = result
        for i in range(len(gaps)):
            if gaps[i] > radius >= 1:
                radius = gaps[i] - radius
                continue
            elif gaps[i] <= radius or radius < 1:
                return [-1, -1]
        return [result, 1]
    elif len(gaps) % 2 == 1 and result >= 6:
        radius = result
        for i in range(len(gaps)):
            if gaps[i]*3 > radius >= 3:
                radius = 3*gaps[i] - radius
                continue
            elif 3*gaps[i] <= radius or radius < 3:
                return [-1, -1]
        return [result, 3] #4,5,9,10
    else:
        return [-1, -1]

    #validating result with iteration

def isValid(radius, gap):
    if len(gap) != 0:
        gapList = iter(gap)
        nextRadius = next(gapList) - radius if next(gapList) else -1
        nextGap = next(gapList)
        if gap > radius >= 1:
            nextRadius = gap[i+1] - radius
            nextGap = gap[i+1]
        else:
            return False
        isValid(nextRadius, nextGap)
    elif len(gap) == 0:
        return False


if __name__ == "__main__":
    pegs = [[4, 17, 50],
            [4, 300, 501, 600],
            [4, 300, 501, 600, 800, 1000],
            [68, 1515, 2022, 2315, 2772, 2987, 3621, 3863, 5304, 6921, 8042, 8594, 8668, 8674, 9536, 9833],
           ]
    answer = [[-1, -1],
              [388, 3],
              [388, 3]
             ]
    j = 0
    for i in pegs:
        print(i)
        a = solution(i)
        print(a)
        if a == answer[j]:
            print("test"+str(j)+"passed")
            j +=1
        else:
            print("test"+str(j)+"not passed_______________________________________________________________________")
            j +=1

