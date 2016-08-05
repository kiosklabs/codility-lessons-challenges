def sieve(N):
    semi = set()
    sieve = [True]* (N+1)
    sieve[0] = sieve[1] = False
 
    i = 2
    while (i*i <= N):
        if sieve[i] == True:
            for j in xrange(i*i, N+1, i):
                sieve[j] = False
        i += 1
 
    i = 2
    while (i*i <= N):
        if sieve[i] == True:
            for j in xrange(i*i, N+1, i):
                if (j % i == 0 and sieve[j/i] == True):
                    semi.add(j)
        i += 1
 
    return semi
 
def solution(N, P, Q):
 
    semi_set = sieve(N)
 
    prefix = []
 
    prefix.append(0) # 0
    prefix.append(0) # 1
    prefix.append(0) # 2
    prefix.append(0) # 3
    prefix.append(1) # 4
 
    for idx in xrange(5, max(Q)+1):
        if idx in semi_set:
            prefix.append(prefix[-1]+1)
        else:
            prefix.append(prefix[-1])
 
    solution = []
 
    for idx in xrange(len(Q)):
        solution.append(prefix[Q[idx]] - prefix[P[idx]-1])
 
    return solution
