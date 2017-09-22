
def main():
	fileName = 'TweetCrimeComplete.csv'
	removeTerms = []

	with open('./Results/'+fileName, 'r') as inputFile:
		inputBuffer = inputFile.readlines()
		idCheck = []
		newBuffer = []
		removeTerms = [
		'Accessory', 
		'Alert', 
		'Examination', 
		'Fundamental', 
		'International', 
		'Information', 
		'Government', 
		'Extreme', 
		'Expert', 
		'Unexpected',
		'Neighborhood',
		'Power',
		'Principle',
		'Reported',
		]

		for line in inputBuffer:
			lineList = line.rstrip().split(';')
			if not (lineList[-7] in idCheck): 
				if not (lineList[-4] in removeTerms):
					idCheck.append(lineList[-7])
					lineList.pop(-5)
					newBuffer.append(lineList)

	with open('./Results/Cleaned'+fileName, 'w') as outPutFile:
		for line in newBuffer:
			print >> outPutFile, ';'.join(line)

	print 'completed',len(newBuffer), 'of',len(inputBuffer) 

if __name__ == '__main__':
	main()