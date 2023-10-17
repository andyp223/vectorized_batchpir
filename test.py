import math

def nextPowerOf2(x):
    return 1 if x == 0 else 2**math.ceil(math.log2(x))


def FLUTE(inputSize,outputSize):
	return 4.236 * (2 ** inputSize - inputSize - 1)

def OT(N):
	return 0.118 * N

def calcOptCostCPIR(numLookups, numRecursion, inputSize, outputSize):

	# lookupCost = (float(numLookups)/batchSize)*numTables * (FLUTE(inputSize - numRecursion, outputSize) + 2*outputSize)
	lookupCost = (float(numLookups)/batchSize)*(3*8192*200 + 8192*30)

	print("LOOK UP COST WITH PIR IS " + str(round(lookupCost/ 8 /1024/1024,2)))

	answerCost = 0
	for i in range(numRecursion): 
		answerCost = 3 * AND() * outputSize 

	return queryCost + lookupCost + answerCost

b = 256
B = 2 * b 
inputSize = 16
outputSize = 16
primeSize = 16 # 16 32 or 64 

bandwidth = float(1) * 1024 / 8  # megabytes per second 
rtt = 0.04 # in seconds

NB = nextPowerOf2((2 ** inputSize) / float(B))


# server to client communication 
phase1 = 3 * b * primeSize 

# run OT or secondary batchPIR 

phase2OT = B * OT(NB)
phase2PIR = (3*8192*200) + 8192*30 

phase3 = 3*8192*200 + 8192*30 


totalOT = phase1 + phase2OT + phase3 
totalPIR = phase1 + phase2PIR + phase3 

totalFlute = b * (FLUTE(inputSize,outputSize) + 2 * outputSize)

commOT = totalOT / 8 / 1024 / 1024
commPIR = totalPIR / 8 / 1024 / 1024
commFlute = totalFlute / 8 / 1024 / 1024

print(round(totalOT / 8 / 1024 / 1024, 2))
print(round(totalPIR / 8 / 1024 / 1024, 2))
print(round(totalFlute / 8 / 1024 / 1024, 2))
print((commOT / bandwidth + rtt * 5))
print((commPIR / bandwidth + rtt * 5))
print((commFlute / bandwidth + rtt * 1))