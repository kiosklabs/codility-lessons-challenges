def solution(N):

    has_one = False
    binary = N
    zero_count = 0
    max_count = 0
    
    # while we have a value
    while binary:
        # binary comparison (if binary contains a 1)
        if binary & 1 == 1:
            if (has_one == False):
                has_one = True
            else:
                # compare zero count
                max_count = max(max_count,zero_count)
            # reset count for new gap
            zero_count = 0
        else:
            # increase zero count until one is found
            zero_count += 1

        # bitwise step to the right (right shift)
        binary >>= 1
            
    return max_count