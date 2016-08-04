def solution(A, B):
    survivors = 0
    fishes_upstream = []
     
    for idx in xrange(len(A)):
        if B[idx] == 0:
            # check if it encounters any fish
            while len(fishes_upstream) != 0:
                if fishes_upstream[-1] > A[idx]:
                    break
                else:
                    fishes_upstream.pop()
            # add as survivor if no fish
            else:
                survivors += 1
        else:
            # add fish to survivors
            fishes_upstream.append(A[idx])
             
    survivors += len(fishes_upstream)
     
    return survivors