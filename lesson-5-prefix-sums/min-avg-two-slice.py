def solution(A):
    earliest_index = 0
    minimum = 10001
 
    for idx in xrange(0, len(A)-1):
        if (A[idx] + A[idx+1])/2.0 < minimum:
            earliest_index = idx
            minimum = (A[idx] + A[idx+1])/2.0
        if idx < len(A)-2 and (A[idx] + A[idx+1] + A[idx+2])/3.0 < minimum:
            earliest_index = idx
            minimum = (A[idx] + A[idx+1] + A[idx+2])/3.0
 
    return earliest_index