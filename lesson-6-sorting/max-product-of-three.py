def solution(A):
    if len(A) < 3:
        raise Exception("Invalid input")
         
    A.sort()
     
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
