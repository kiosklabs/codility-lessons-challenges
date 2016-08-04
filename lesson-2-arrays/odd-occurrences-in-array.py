def solution(A):
    missing_int = 0
    for value in A:
        # use xor operation as to determine the unpaired value
        missing_int ^= value
    return missing_int