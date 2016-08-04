def solution(A):
    if len(A) == 0:
        return 0
 
    # for easy comparison
    A.sort()
 
    distinct_vals = 1
    last_val = A[0]
 
    for idx in xrange(1, len(A)):
        if A[idx] != last_val:
            distinct_vals += 1
            last_val = A[idx]
 
    return distinct_vals
