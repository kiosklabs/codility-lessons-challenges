PLANK_START = 0
PLANK_END = 1
 
NAIL_ARR_IDX = 0
NAIL_HIT_LOCATION = 1
 
class NoNailFoundException(Exception):
    def __init__(self):
        pass
 
def findPosOfNail(nails, plank, previous_max):
    nail_idx = -1
    result = -1
 
    # logarithmic scan O(log(M))
    lower_idx = 0
    upper_idx = len(nails) - 1
 
    while lower_idx <= upper_idx:
        mid_idx = (lower_idx + upper_idx) // 2
        if nails[mid_idx][NAIL_HIT_LOCATION] < plank[PLANK_START]:
            lower_idx = mid_idx + 1
        elif nails[mid_idx][NAIL_HIT_LOCATION] > plank[PLANK_END]:
            upper_idx = mid_idx - 1
        else:
            upper_idx = mid_idx - 1
            result = nails[mid_idx][PLANK_START]
            nail_idx = mid_idx
 
    if result == -1:
        raise NoNailFoundException
 
    # linear scan O(M)
    nail_idx += 1
    while nail_idx < len(nails):
        if nails[nail_idx][NAIL_HIT_LOCATION] > plank[PLANK_END]:
            break
        result = min(result, nails[nail_idx][NAIL_ARR_IDX])
        if result <= previous_max:
            return result
        nail_idx += 1
 
    if result == -1:
        raise NoNailFoundException
 
    return result
 
def getNrNailsRequired(planks, nails):
    result = 0
    for plank in planks:
        result = max(result, findPosOfNail(nails, plank, result))
 
    return result+1
 
def solution(A, B ,C):
    planks = zip(A,B)
 
    nails = sorted(enumerate(C), key=lambda var: var[1])
 
    try:
        return getNrNailsRequired(planks, nails)
    except NoNailFoundException:
        return -1