def solution(H):
    boxes = 0
     
    stack = []
     
    for height in H:
        # limit scope of block sizes to within height
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()
         
        if len(stack) != 0 and stack[-1] == height:
            # ignore same height stack 
            pass
        else:
            # add block to the stack
            boxes += 1
            stack.append(height)
             
    return boxes