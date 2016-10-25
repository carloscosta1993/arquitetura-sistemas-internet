class rpnCalculator:
 
 def __init__(self):
         self.memory = [1,2,3,4,5]

 def pushValue(self,item):
	self.memory.append(item)
	
 def popValue(self):
	self.memory.pop(0)
	print "item: ", self.memory[0]
	
 def printStack(self):
	print "stack: ", self.memory

val1 = rpnCalculator()
val1.popValue()
val1.pushValue(33333)
val1.printStack()

	
