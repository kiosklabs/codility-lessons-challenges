import sys
 
def solution(A):

    # initial cycle, determine parts bound
    parts = [0] * len(A)
    parts[0] = A[0]
  
    for idx in xrange(1, len(A)):
        parts[idx] = A[idx] + parts[idx-1]
  
    # following cycle, getting the minimum bounded parts
    solution = sys.maxint
    for idx in xrange(0, len(parts)-1):
        solution = min(solution,abs(parts[-1] - 2 * parts[idx]));  
  
    return solution
