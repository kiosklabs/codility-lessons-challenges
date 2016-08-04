def solution(X, A):
    # presume that frog cant pass at initial state
    canpass = [False] * X
    uncovered = X
 
    for idx in xrange(len(A)):
        if A[idx] <= 0 or A[idx] > X:
            raise Exception("Invalid value", A[idx])
        
        if canpass[A[idx]-1] == False:
            canpass[A[idx]-1] = True
            uncovered -= 1
            if uncovered == 0:
                return idx
 
    return -1