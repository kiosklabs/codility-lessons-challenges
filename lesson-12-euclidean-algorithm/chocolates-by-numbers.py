def gcd(ntotal, divisor):
  if divisor == 0:
    return ntotal
  #recurse while ntotal > 0
  return gcd(divisor, ntotal % divisor)

# returns the no. of times we can eat given n chocolates and m skips
def get_eat_rounds(p, q):
    actual_skips = q / gcd(p,q)
    return (p * actual_skips) / q
 
def solution(N, M):
    return get_eat_rounds(N, M)
