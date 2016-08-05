def solution(A):
    member = ''
    elements = 0
 
    for value in A:
        if member == '':
            member = value
            elements = 1
        else:
            if value != member:
                elements -= 1
                if elements == 0:
                    member = ''
            else:
                elements += 1
 
    if elements == 0:
        return 0
 
    cnt = 0
    last_idx = 0
 
    for idx, value in enumerate(A):
        if value == member:
            cnt += 1
            last_idx = idx
 
    if cnt < len(A)//2:
        return 0
 
    equi_leaders = 0
    cnt_to_the_left = 0
    for idx, value in enumerate(A):
        if value == member:
            cnt_to_the_left +=1
        if cnt_to_the_left > (idx + 1)//2 and \
            cnt - cnt_to_the_left > (len(A) - idx - 1) //2:
            equi_leaders += 1
 
    return equi_leaders