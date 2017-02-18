import math
import numpy

def calu_sigma(alist):
    sigma = 0
    meanvalue = numpy.mean(alist)
    num = len(alist)
    for i in range(0, num):
        sigma += (alist[i] - meanvalue) * (alist[i] - meanvalue)
    sigma = math.sqrt(sigma / num)
    return sigma

my_list = [5, 6, 8, 9]
print(calu_sigma(my_list))