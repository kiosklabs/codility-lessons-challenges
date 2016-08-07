# get gcd
def gcd(n, d):
  if n % d == 0:
    return d
  else:
    return gcd(d, n % d)
 
def getSameFactors(p, q):
    if p == q == 0:
        return True
     
    denom = gcd(p, q)
     
    p = get_gcd(p, denom) == 1
    
    if (p != 1):
        return False

    q = get_gcd(q, denom) == 1
     
    return q

def get_gcd(n, d):
    while (n != 1):
        n_val = gcd(n, d)
        if n_val == 1:
            break
        n /= n_val
    return n
 
def solution(A, B):

    if len(A) != len(B):
        raise Exception("Invalid input")

    cnt = 0
    for ix in xrange(len(A)):
        if A[ix] < 0 or B[ix] < 0:
            raise Exception("Invalid value")
        if getSameFactors(A[ix], B[ix]):
            cnt += 1
     
    return cnt