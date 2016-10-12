class rpnCalculator:
 
 def __init__(self):
         self.memory = []

 def pushValue(self,item):
	self.memory.append(item)
	
 def popValue(self, memory):
	self.memory.pop()

 def printStack(self):
	print "stack: ", self.memory

val1 = rpnCalculator()
val1.pushValue(5)
val1.pushValue(4)
val1.pushValue(3)
val1.pushValue(2)
val1.printStack()

	
