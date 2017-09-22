import sys

def parseArgs(argv):
	error = 0
	if len(argv) % 2 != 0:
		return [error, False]

	else:
		argDict = {}
		for element in range(0,len(argv),2):
			argDict[argv[element]]= argv[element+1]

		if ('--originlon' and '--originlat' and '--oppositelon' 
			and '--oppositelat'  and '--numberRows' and '--numberCols') in argDict.keys():
			resultParse = [float(argDict['--originlon']),
			float(argDict['--originlat']),
			float(argDict['--oppositelon']),
			float(argDict['--oppositelat']),
			int(argDict['--numberRows']),
			int(argDict['--numberCols'])]
			return [resultParse, True]
		else:	
			return [error, False]

def main(argv):
	if len(argv) == 0:
		print 'You must pass some parameters. Use \"-h\" to help.'
		return

	if len(argv) == 1 and argv[0] == '-h':
		f = open('exporter_help_text.txt', 'r')
		print f.read()
		f.close()
		return
	
	try:
		args = parseArgs(argv)
		
		if args[1] != False:
#			originPoint = [-84.35, 39.05] # lon, lat
#			oppositePoint = [-84.65, 39.25] # lon, lat

			originlon = args[0][0]
			originlat = args[0][1]

			oppositePointLon = args[0][2]
			oppositePointLat = args[0][3]

			colNumber = args[0][5]
			rowNumber = args[0][4]

			stepVer = (oppositePointLat - originlat)/(rowNumber*1.00)
			stepHor = (oppositePointLon - originlon)/(colNumber*1.00)

			rowTemp = originlat
			finalGrid = []
			for row in range(rowNumber+1):
				colTemp = originlon
				for column in range(colNumber+1):
					finalGrid.append([round(colTemp,2), round(rowTemp,2)])
					colTemp += stepHor*1.00
				rowTemp += stepVer*1.00

			with open('./sources/GridFile.csv','w') as gridFile:
				for element in finalGrid:
					print >> gridFile, element
				print 'create grid file done!!!'
		else:
			print 'input is not well defined'
			raise Exception

	except:
		print 'Arguments parser error, try -h'
	
	finally:
		print 'Script closed ...'

if __name__ == '__main__':
	main(sys.argv[1:])