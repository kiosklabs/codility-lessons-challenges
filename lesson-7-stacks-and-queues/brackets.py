def isValidPair(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True 
    if left == '{' and right == '}':
        return True   
    return False
 
def solution(S):
    unpaired = []
     
    for char in S:
        if char == '[' or char == '{' or char == '(':
            unpaired.append(char)
        else:
            if len(unpaired) == 0:
                return 0
            last = unpaired.pop()
            if not isValidPair(last, char):
                return 0
     
    if len(unpaired) != 0:
        return 0
             
    return 1
