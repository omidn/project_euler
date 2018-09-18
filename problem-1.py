def sum(n):
    return (n * (n + 1)) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    m3 = (n - 1) // 3
    m5 = (n - 1) // 5
    m15 = (n - 1) // 15
    
    print (3 * sum(m3) + 5 * sum(m5) - 15 * sum(m15))
