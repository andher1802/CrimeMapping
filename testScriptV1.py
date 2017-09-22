from tweeterAPI.tweeterBrowser import tweeterBrowser

def main():

	params = {
#	'username':'@AndresMHC02',
	'query':'burglary',
	'geocode':'39.102066,-84.51655,30km',
	'since':'2012-01-01',
	'until':'2012-01-30',
	'maxTweets':30,
	}

	startingBrowser = tweeterBrowser(params)
	results = startingBrowser.getTweets()

	with open('./sources/testFile.csv', 'w') as outputFile:
		for element in results:
			print >> outputFile, element

if __name__ == '__main__':
	main()