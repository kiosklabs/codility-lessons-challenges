def reverse(A, i, j):
    for idx in xrange((j - i + 1) / 2):
        A[i+idx], A[j-idx] = A[j-idx], A[i+idx]
 
def solution(A, K):
    l = len(A)
    if l == 0:
        return []
    
    # module to determine actual position     
    K = K%l
     
    reverse(A, l - K, l -1)
    reverse(A, 0, l - K -1)
    reverse(A, 0, l - 1)
 
    return A