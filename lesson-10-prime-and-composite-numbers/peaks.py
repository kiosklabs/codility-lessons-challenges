def solution(A):
    peaks = []
 
    for idx in xrange(1, len(A)-1):
        if A[idx-1] < A[idx] > A[idx+1]:
            peaks.append(idx)
 
    if len(peaks) == 0:
        return 0
 
    for size in xrange(len(peaks), 0, -1):
        if len(A) % size == 0:
            block_size = len(A) // size
            found = [False] * size
            found_cnt = 0
            for peak in peaks:
                block_nr = peak//block_size
                if found[block_nr] == False:
                    found[block_nr] = True
                    found_cnt += 1
 
            if found_cnt == size:
                return size
 
    return 0
