def solution(A):
    found = [False] * len(A)
    for num in A:
        if 0 < num <= len(A):
            found[num-1] = True
 
    for idx in xrange(len(found)):
        if found[idx] == False:
            return idx + 1
 
    return len(A) + 1