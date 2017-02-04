# Perceptrons!

class TwoStepFun(object):
    """A step function with configurable threshold.
    >>> 3+3
    6
    >>> f1 = TwoStepFun()
    >>> f1.threshold
    0.5
    >>> f1(0.4)
    0
    >>> f1(0.6)
    1
    >>> f2 = TwoStepFun(1)
    >>> f2(0.99)
    0
    >>> f2(-1.2)
    0
    >>> f2(1.001)
    1
    """
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def __call__(self, value):
        if value < self.threshold:
            return 0
        else:
            return 1

class Perceptron(object):
    """Represent a perceptron with 2 inputs, bias.
    >>> p1 = Perceptron(TwoStepFun(1))
    >>> p1.weights = [0.6, 0.6, 0.0]
    >>> bits = [0,1]
    >>> [p1(a,b) for a in bits for b in bits]
    [0, 0, 0, 1]
    >>> p2 = Perceptron(TwoStepFun(0.5))
    >>> p2.weights = [0.6, 0.6, 0.0]
    >>> bits = [0,1]
    >>> [p2(a,b) for a in bits for b in bits]
    [0, 1, 1, 1]
    """
    def __init__(self, transfer):
        from random import random
        self.transfer = transfer
        self.weights = [random()*4-2,
                        random()*4-2,
                        random()*4-2]

    def __call__(self, x0, x1):
        avg = (x0 * self.weights[0] +
               x1 * self.weights[1] +
               1  * self.weights[2])
        return self.transfer(avg)
    """
    #delta W = a(t - y) x
    #alpha = learning rate
    #t = target
    #y = output
    #x = input
    #y = ((x*w) + (x*))
    """
    def learn(self, x0, x1, target):
        output = self(x0, x1)
        err = (target - output)
        DeltaW0 = (0.2)*(err)*(x0)
        DeltaW1 = (0.2)*(err)*(x1)

        self.weights[0] += DeltaW0
        self.weights[1] += DeltaW1
        
          

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print doctest.testmod()
    p = Perceptron(TwoStepFun(0.5))
    attempts = 0
    bits = [0,1] # bits 0 & 1 reflects true and falls in a truth table
    for a in bits:
        for b in bits:
            attempts += 1
            p.learn(a, b, (a*b))
            print p.weights
            print "attempts made: ", + attempts
