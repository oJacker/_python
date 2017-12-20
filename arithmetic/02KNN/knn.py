import math

def ComputerEuclideanDistance(x1, y1, x2, y2):
    # Euclidean distance
    d = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))
    return d
d_ag = ComputerEuclideanDistance(3, 104, 18, 90)
d_bg = ComputerEuclideanDistance(2, 100, 18, 90)
d_cg = ComputerEuclideanDistance(1, 81, 18, 90)
d_dg = ComputerEuclideanDistance(101, 10, 18, 90)
d_eg = ComputerEuclideanDistance(99, 5, 18, 90)
d_fg = ComputerEuclideanDistance(98, 2, 18, 90)



print(d_ag)
print(d_bg)
print(d_cg)
print(d_dg)
print(d_eg)
print(d_fg)
