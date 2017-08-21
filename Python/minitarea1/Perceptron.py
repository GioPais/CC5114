

class Perceptron(object):
    def __init__(self, bias=0, w1=1, w2=1):
        self._bias=bias
        self._w1 = w1
        self._w2 = w2

    def get_bias(self):
        return self._bias

    def get_w1(self):
        return self._w1

    def get_output(self,x1,x2):

    	if self._w1*x1+self._w2*x2+self._bias <=0:
    		return 0
    	else:
    		return 1

    def NAND(self,x1,x2):
    	self._w1=-2
    	self._w2=-2
    	self._bias=3
    	return self.get_output(x1,x2)

    def AND(self,x1,x2):
    	self._w1=1
    	self._w2=1
    	self._bias=-1.5
    	return self.get_output(x1,x2)

    def OR(self,x1,x2):
    	self._w1=1
    	self._w2=1
    	self._bias=-0.5
    	return self.get_output(x1,x2)

    def XOR(self,x1,x2):
    	aux=self.NAND(x1,x2)
    	out1=self.NAND(x1,aux)
    	out2=self.NAND(aux,x2)
    	return self.NAND(out1,out2)

    def bit_adder(self,x1,x2):
    	out=self.XOR(x1,x2)
    	carryOut=self.AND(x1,x2)
    	return [carryOut,out]




if __name__ == "__main__":
    
    p=Perceptron()

    #TEST para comportamientos logicos

    #NAND
    assert p.NAND(0, 0) == 1
    assert p.NAND(0, 1) == 1
    assert p.NAND(1, 0) == 1
    assert p.NAND(1, 1) == 0

    #AND
    assert p.AND(0, 0) == 0
    assert p.AND(0, 1) == 0
    assert p.AND(1, 0) == 0
    assert p.AND(1, 1) == 1

    #OR
    assert p.OR(0, 0) == 0
    assert p.OR(0, 1) == 1
    assert p.OR(1, 0) == 1
    assert p.OR(1, 1) == 1

    #XOR
    assert p.XOR(0, 0) == 0
    assert p.XOR(0, 1) == 1
    assert p.XOR(1, 0) == 1
    assert p.XOR(1, 1) == 0

    #TEST para sumador de un bit

    assert p.bit_adder(0, 0) == [0,0]
    assert p.bit_adder(0, 1) == [0,1]
    assert p.bit_adder(1, 0) == [0,1]
    assert p.bit_adder(1, 1) == [1,0]






    