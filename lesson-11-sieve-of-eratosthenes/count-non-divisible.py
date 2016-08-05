def solution(A):
    from math import sqrt

    maxVal = max(A)
    array_size = len(A)

    # get frequency for each el
    count = {}
    for el in A:
        count[el] = count.get(el,0)+1

    # assign first divisor
    divisors = {}
    for el in A:
        divisors[el] = [1]

    # get divisor by determining multiples less than sqrt(maxVal)
    for divisor in xrange(2, int(sqrt(maxVal))+1):
        multiple = divisor
        while multiple  <= maxVal:
            if multiple in divisors and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor

    # clean up results, leave distinct val only
    for el in divisors:
        temp = [el / div for div in divisors[el]]
        temp = [item for item in temp if item not in divisors[el]]
        divisors[el].extend(temp)

    result = []
    for el in A:
        result.append(array_size - sum([count.get(div,0) for div in divisors[el]]))

    return result