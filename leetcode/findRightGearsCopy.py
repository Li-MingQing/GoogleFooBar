from fractions import Fraction
import random
def solution(pegs):
    numerator = 0
    denominator = 0
    sign = 1

    for i in range(len(pegs) - 1):
        numerator += sign * (pegs[i + 1] - pegs[i])
        denominator = 2 + sign
        sign *= -1
    print(denominator)
    FirstGearRadius = Fraction(2 * numerator/denominator).limit_denominator()

    # validating the result
    if numerator >= denominator:
        radius = 2 * numerator / denominator
        for i in range(len(pegs) - 1):
            radius = pegs[i + 1] - pegs[i] - radius
            if radius < 1:
                return [-1, -1]
            else:
                continue
    else:
        return [-1, -1]
    return [FirstGearRadius.numerator, FirstGearRadius.denominator]
    """
def test():
    testCase = []
    gaps = []
    sign = 1
    numerator = 0
    denominator = 0
    a = random.randint(2, 20)

    for i in range(a):
        testCase.append(random.randint(1,10000))
    testCase.sort()
    for i in range(len(testCase) - 1):
        gaps.append(testCase[i + 1] - testCase[i])
    #print(testCase)
    #print(gaps)
    result = solution(testCase)
    #validating result:

    for i in range(len(testCase) - 1):
        numerator += sign * (testCase[i + 1] - testCase[i])
        denominator = 2 + sign
        sign *= -1

    if result != [-1, -1]:
        if 2*numerator == result[0] and denominator == result[1]:
            print("test passed")
    elif result == [-1, -1]:
        pass
    else:
        print("test failed_____________________________________________________________________")
    """
pegs = [4, 300, 501, 600, 800, 1000]
a = solution(pegs)
print(a)




