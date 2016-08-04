def solution(X, Y, D):
    # check if input exceed tresholds
    # X = initial position, Y - target position
    # D = distance the frog can jump
    if Y < X or D <= 0:
        raise Exception("Invalid arguments")
         
    if (Y - X) % D == 0:
        # double slash to get only whole number
        return (Y - X) // D
    else:
        return ((Y - X) // D) + 1