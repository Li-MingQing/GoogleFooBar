#output the next 5 digits at i position in the prime number string"2357111317......"
import math
class solution:
    def isPrime(self, n):
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

    def solution(self, i):
        primeString = "2"
        Prime = 3
        while len(primeString) <= i+5:
            if self.isPrime(Prime):
                primeString += str(Prime)
                Prime += 2
            else:
                Prime += 2
                continue
        return primeString[i:i+5]

if __name__ == "__main__":
    a = solution()
    print(a.solution(4))
