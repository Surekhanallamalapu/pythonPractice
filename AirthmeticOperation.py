import math
def airthmeticOperations(*args, keyargs='sum'):
    if keyargs=='sum':
        return sum(args)
    if keyargs=='multiply':
        return math.prod(args)
    if keyargs=='reminder':
        return math.remainder(args)
airthmeticOperations(1,2,keyargs='multiply')
    