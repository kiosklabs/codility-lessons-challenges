def solution(A):
    cars_pass = 0
    num_passes = 0
 
    for idx in xrange(len(A)-1, -1, -1):
        if A[idx] == 0:
            num_passes += cars_pass
            if num_passes > 1000000000:
                return -1
        else:
            cars_pass += 1
 
    return num_passes
