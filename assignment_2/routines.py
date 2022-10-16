

def intersection(l1: tuple, l2: tuple):

    # define our 4 points that make up the 2 lines 
    p1 = l1[0]
    p2 = l1[1]
    p3 = l2[0]
    p4 = l2[1]

    # define all 8 values that make up the 2 lines
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    x4 = p4[0]
    y4 = p4[1]

    # according to en.wikipedia.org/wiki/Line%E2%80%93line_intersection, we can use the following expression
    if (((x1-x2)*(y3-y4)) -  ((y1-y2)*(x3-x4))) != 0:
        x_intercept = ((((x1*y2) - (y1*x2))*(x3-x4)) - ((x1-x2)*((x3*y4) - (y3*x4))))/(((x1-x2)*(y3-y4)) -  ((y1-y2)*(x3-x4)))

        y_intercept = ((((x1*y2) - (y1*x2))*(y3-y4)) - ((y1-y2)*((x3*y4) - (y3*x4))))/(((x1-x2)*(y3-y4)) -  ((y1-y2)*(x3-x4)))

        return [x_intercept, y_intercept]
    else:
        return ['parallel']
