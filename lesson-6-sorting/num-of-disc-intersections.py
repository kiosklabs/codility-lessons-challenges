def solution(A):

    overlaps = 0
    overlapping_circle = 0
    vertices = []

    for index, area in enumerate(A):
        left_point = index - area
        right_point = index + area
        vertices += [(left_point, True), (right_point, False)]
 
    vertices.sort(key=lambda x: (x[0], not x[1]))
 
    for _, left_vertex in vertices:
        if left_vertex:
            overlaps += overlapping_circle
            overlapping_circle += 1
        else:
            overlapping_circle -= 1
            
        # sanity check
        if overlaps > 10E6:
            return -1
 
    return overlaps
