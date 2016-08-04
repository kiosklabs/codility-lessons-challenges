def solution(A):
    missing_element = len(A)+1
     
    for idx,value in enumerate(A):
        # same as before using xor to find missing value in a given equation
        missing_element = missing_element ^ value ^ (idx+1)
         
    return missing_element