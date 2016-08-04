def solution(N):
    cnt = 0
    i = 1
    while ( i * i <= N):
        if (N % i == 0):
            if i * i == N:
               cnt += 1
            else:
                cnt += 2
        i += 1
    return cnt
