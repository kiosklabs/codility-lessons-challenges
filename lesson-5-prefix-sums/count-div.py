def solution(A, B, K):
    if B < A or K <= 0:
        raise Exception("Invalid Input")
 
    # // to get whole number part only
    minimum =  ((A + K -1) // K) * K
 
    if minimum > B:
      return 0
 
    return ((B - minimum) // K) + 1