def solution(A):

    start_pt, end_pt = [0] * len(A), [0] * len(A)
    max_double_slice = 0
     
    # confirm end pts first
    for idx in xrange(1, len(A)):
        end_pt[idx] = max(0, end_pt[idx-1] + A[idx])
    
    # determine start_pts
    for idx in reversed(xrange(len(A)-1)):
        start_pt[idx] = max(0, start_pt[idx+1] + A[idx])

    # compare slices
    for idx in xrange(1, len(A)-1):
        max_double_slice = max(max_double_slice, start_pt[idx+1] + end_pt[idx-1])
         
         
    return max_double_slice
