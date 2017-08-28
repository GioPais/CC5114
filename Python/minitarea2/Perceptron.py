import random

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


	def train_perceptron(self,cases):
		c = 0.01
		for i in range(cases):
			x = random.randint(-50,50)
			y = random.randint(-100,100)

			output=self.get_output(x,y)

			#Condicion del if es la recta con la que se entrenara

			if(3*x+10>y):
				answer = 0
			else:
				answer = 1

			if(output == 0 and answer == 1):
				self._w1 = self._w1 + c*x
				self._w2 = self._w2 + c*y
			else:
				if(output == 1 and answer == 0):
					self._w1 = self._w1 - c*x
					self._w2 = self._w2 - c*y

	def test_trainnig(self,cases):
		match=0
		for i in range(cases):
			x = random.randint(-50,50)
			y = random.randint(-100,100)

			output=self.get_output(x,y)

			#Condicion del if es la recta con la que se entrenara

			if(3*x+10>y):
				answer = 0
			else:
				answer = 1

			if(output == 0 and answer == 0):
				match=match+1
			else:
				if(output == 1 and answer == 1):
					match=match+1
		return match


if __name__ == "__main__":
	p=Perceptron()

	b_trainning=p.test_trainnig(1000)
	p.train_perceptron(10000)
	a_trainning=p.test_trainnig(1000)

	print "Cantida de match sin entrenamiento:"
	print b_trainning
	print "Cantida de match con entrenamiento:"
	print a_trainning



