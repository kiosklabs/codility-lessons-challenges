
def solution(S, P, Q):
     
    if len(P) != len(Q):
        raise Exception("Invalid input")
     
    last_seen_A = [-1] * len(S)
    last_seen_C = [-1] * len(S)
    last_seen_G = [-1] * len(S)
    last_seen_T = [-1] * len(S)
         
    for idx in xrange(len(S)):
        addChar(last_seen_A, S, 'A', idx)
        addChar(last_seen_C, S, 'C', idx)
        addChar(last_seen_G, S, 'G', idx)
        addChar(last_seen_T, S, 'T', idx)
     
     
    solution = [0] * len(Q)
     
    for idx in xrange(len(Q)):
        if last_seen_A[Q[idx]] >= P[idx]:
            solution[idx] = 1
        elif last_seen_C[Q[idx]] >= P[idx]:
            solution[idx] = 2
        elif last_seen_G[Q[idx]] >= P[idx]:
            solution[idx] = 3
        elif last_seen_T[Q[idx]] >= P[idx]:
            solution[idx] = 4
        else:    
            raise Exception("Should never happen")
         
    return solution

def addChar(previous_arr, sequence, identifier, pos):
    if sequence[pos] == identifier:
        previous_arr[pos] = pos
    elif pos > 0:
        previous_arr[pos] = previous_arr[pos -1]
 