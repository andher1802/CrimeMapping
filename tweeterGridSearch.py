from tweeterAPI.tweeterBrowser import tweeterBrowser

def main():
	gridFilename = 'GridFile.csv'
	sinceDate = '2012-01-01'
	untilDate = '2012-12-31'
	dictionaryFilename = 'CrimeDictionary'

	limit = 5

	#Reading grid file
	with open('./sources/'+gridFilename, 'r') as GridFile:
		gridFileBuffer = GridFile.readlines()
		coordinatesBuffer = []

		for element in gridFileBuffer[:]:
			stringCoordinates = element[1:-2] # lon, lat
			coordinatesBuffer.append(stringCoordinates.split(','))

	#Open dict file here

	relatedTermCrime = {}

	with open ('./sources/'+dictionaryFilename, 'r') as dictFile:
		dictBuffer = dictFile.readlines()
		for conceptLine in dictBuffer:
			tempLine = conceptLine.split(',')[:]
			crimeConcept = tempLine[0]
			crimeLine = tempLine
			relatedTermCrime[crimeConcept] = crimeLine

	#Set params
	maxtweets = 50
	radius = '5km'

	enable = True

	if enable: 
		#Open output File
		outputFileName = 'TweeterGridSearchResults_'+sinceDate+'-'+untilDate+'_grid'+gridFilename.split('.')[0]+'_Dict'+dictionaryFilename+'.csv'

		with open('./Results/'+outputFileName, 'w') as outputFile:			
			checkDuplicates = []
			appendedResults = []
			print >> outputFile, "Username;DateTime;Retweets;Text;Hashtag;ID;Permanentlink;Concept;Latitud;Longitud;Radius"

			for crime, relatedConcepts in relatedTermCrime.iteritems():
				for concept in relatedConcepts:
					for geolocation in coordinatesBuffer:
							print concept, geolocation, sinceDate, untilDate
							params = {
							'query':concept,
							'geocode': geolocation[1][1:]+','+geolocation[0]+','+radius,
							'since':sinceDate,
							'until':untilDate,
							'maxTweets':maxtweets,
							}
							startingBrowser = tweeterBrowser(params)
							results = startingBrowser.getTweets()
							for result in results:
								printResults = result+';'+crime+';'+concept+';'+geolocation[1][1:]+';'+geolocation[0]+';'+radius
								appendedResults.append(printResults)
								tweetId = printResults.split(';')[-7]
								if not(tweetId in checkDuplicates):
									checkDuplicates.append(tweetId)
									print >> outputFile, printResults

if __name__ == '__main__':
	main()