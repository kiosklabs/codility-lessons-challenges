def solution(A):
    A_len = len(A)
    element = -1
    element_count = 0
    element_index = -1
 
    for index in xrange(A_len):
        if element_count == 0:
            element = A[index]
            element_index = index
            element_count += 1
        else:
            if A[index] == element:
                element_count += 1
            else:
                element_count -= 1
 
    if len([number for number in A if number == element]) <= A_len//2:
        return -1
    else:
        return element_index