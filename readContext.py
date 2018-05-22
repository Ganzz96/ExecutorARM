import re
import sys

#-------------------------------------------------------------------------------------------------------

def getRegContext(fileName):
	with open(fileName) as f:
		context = f.read()

	f.close()

	return re.findall(r'\-?\d+', context)

#-------------------------------------------------------------------------------------------------------

def generateAsmTest(regContext, prologue, instruction, epilogue):

	f = open("test.s", "w")

	f.write(prologue)

	for i in range(len(regContext)):
		f.write("ldr r" + str(i) + ", =r" + str(i) + " \n")
		f.write("ldr r" + str(i) + ", [r" + str(i) + "]\n")

	f.write(instruction)

	f.write(epilogue)

	for i in range(len(regContext)):
		f.write("r" + str(i) + ": .word " + regContext[i] + " \n")

	f.close()

#-------------------------------------------------------------------------------------------------------

instructionFile = sys.argv[1]
contextFile 	= sys.argv[2]

regContext = getRegContext(contextFile)

with open("requierd_files/prologue.s") as f:
	prologue = f.read()

f.close()

with open("requierd_files/epilogue.s") as f:
	epilogue = f.read()

f.close()

with open(instructionFile) as f:
	instruction = f.read()
f.close()

generateAsmTest(regContext, prologue, instruction, epilogue)

#-------------------------------------------------------------------------------------------------------

