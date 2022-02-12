import math


def isPrime(n):
    a = int(math.sqrt(n)) + 1
    i = 2
    while i < a:
        if n % i == 0:
            return False
            break
        elif n % i != 0:
            i += 1
            continue
    else:
        return True
#output the next 5 digits at i position in the prime number string"2357111317......"
def solution(i):
    primeString = "2"
    result = ""
    Prime = 3
    while len(primeString) <= i+5:
        if isPrime(Prime):
            primeString += str(Prime)
            Prime += 2
        else:
            Prime += 2
            continue

    for n in range(5):
        result += primeString[i + n]
    return result


if __name__ == "__main__":

    a = solution(3)
