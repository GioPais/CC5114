

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




if __name__ == "__main__":
    print 'hello world'
    #sm.execute()



    