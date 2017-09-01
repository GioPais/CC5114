import random
from math import exp


class Sigmoid(object):
    def __init__(self, bias=0, w1=1, w2=1, thres=0.5):
        self._bias = bias
        self._w1 = w1
        self._w2 = w2
        self._thres = thres

    def get_bias(self):
        return self._bias

    def get_w1(self):
        return self._w1

    def get_output(self, x1, x2):

        output = (1.0 / (1 + exp(x1 * self._w1 + x2 * self._w2 + self._bias)))
        if output >= self._thres:
            return 0
        else:
            return 1

    def NAND(self, x1, x2):
        self._w1 = -2
        self._w2 = -2
        self._bias = 3
        self._thres = 0.5
        return self.get_output(x1, x2)

    def AND(self, x1, x2):
        self._w1 = 1
        self._w2 = 1
        self._bias = -1.5
        self._thres = 0.5
        return self.get_output(x1, x2)

    def OR(self, x1, x2):
        self._w1 = 1
        self._w2 = 1
        self._bias = -0.5
        self._thres = 0.5
        return self.get_output(x1, x2)

    def train(self, cases):
        c = 0.01
        for i in range(cases):
            x = random.randint(-50, 50)
            y = random.randint(-100, 100)

            output = self.get_output(x, y)

            # Condicion del if es la recta con la que se entrenara

            if (3 * x + 10 > y):
                answer = 0
            else:
                answer = 1

            if (output == 0 and answer == 1):
                self._w1 = self._w1 + c * x
                self._w2 = self._w2 + c * y
            else:
                if (output == 1 and answer == 0):
                    self._w1 = self._w1 - c * x
                    self._w2 = self._w2 - c * y

    def test_trainnig(self, cases):
        match = 0
        for i in range(cases):
            x = random.randint(-50, 50)
            y = random.randint(-100, 100)

            output = self.get_output(x, y)

            # Condicion del if es la recta con la que se entrenara

            if (3 * x + 10 > y):
                answer = 0
            else:
                answer = 1

            if (output == 0 and answer == 0):
                match = match + 1
            else:
                if (output == 1 and answer == 1):
                    match = match + 1
        return match


if __name__ == "__main__":
    p = Sigmoid()

    # TEST para comportamientos logicos

    # NAND
    assert p.NAND(0, 0) == 1
    assert p.NAND(0, 1) == 1
    assert p.NAND(1, 0) == 1
    assert p.NAND(1, 1) == 0

    # AND
    assert p.AND(0, 0) == 0
    assert p.AND(0, 1) == 0
    assert p.AND(1, 0) == 0
    assert p.AND(1, 1) == 1

    # OR
    assert p.OR(0, 0) == 0
    assert p.OR(0, 1) == 1
    assert p.OR(1, 0) == 1
    assert p.OR(1, 1) == 1

    b_trainning = p.test_trainnig(1000)
    p.train(10000)
    a_trainning = p.test_trainnig(1000)

    print "Cantidad de match sin entrenamiento:"
    print b_trainning
    print "Cantidad de match con entrenamiento:"
    print a_trainning
