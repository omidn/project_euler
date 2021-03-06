# https://www.hackerrank.com/contests/projecteuler/challenges/euler002

def fibo(n):
    if (n == 2):
        return 2
    elif (n == 5):
        return 8
    return 4 * fibo(n - 3) + fibo(n - 6)

# cache all values
dict = {}
MAX = 4*10**16

for i in range(2, 100, 3):
    dict[i] = fibo(i)
    if (dict[i] > MAX):
        break

t = int(input().strip())

for i in range(t):
    upper_limit = int(input().strip())
    # sum only terms which do not exceed the upper_limit
    sum = 0
    counter = 2
    while (dict[counter] < upper_limit):
        sum += dict[counter]
        counter += 3
        print (sum)

