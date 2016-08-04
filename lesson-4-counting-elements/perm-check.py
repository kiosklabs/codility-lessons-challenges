def solution(A):
    found = [False] * len(A)
 
    for num in A:
        if 0 <= num > len(A):
            return 0
        if found[num-1] == True:
            return 0
        found[num-1] = True
 
    return 1
