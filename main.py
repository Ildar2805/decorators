from decorators import logger1, logger2

#1
@logger1
def _sum1(a, b):
    return a + b

result1 = _sum1(5, 7)

#2
@logger2(path = 'info2.log')
def _sum2(a, b):
    return a + b

result2 = _sum2(8, 10)



