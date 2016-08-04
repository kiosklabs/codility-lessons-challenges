
import math
def solution(N):
    if N <= 0:
      return 0
   
    for i in xrange(int(math.sqrt(N)), 0, -1):
        if N % i == 0:
            return 2*(i+N/i)
             
    raise Exception("should never reach here!")  

