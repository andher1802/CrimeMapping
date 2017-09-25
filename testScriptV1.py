from tweeterAPI.tweeterBrowser import tweeterBrowser
import io
import oauth2 as oauth
import json

def setAuth():
	ACCESS_TOKEN = '570259739-4u7BUZr6jEkwOPNnh46b3yOupCditBI6fVaT34aR'
	ACCESS_SECRET = 'YFpqCtdEVglZs4W7PbeL10Mq8zHYPdExvVZ8u7I3GPp65'
	CONSUMER_KEY = 'GsaV4E0nUX8ns4nNMmZihEXUD'
	CONSUMER_SECRET = 'zED1r57gysR7aL9dguhWHZxgSknf60juzGCRzFSzFaebsczR3O'
	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	access_token = oauth.Token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)
	client = oauth.Client(consumer, access_token)
	return client

def main():
	params = {
	'username':'@AndresMHC02',
#	'query':'burglary',
#	'geocode':'39.102066,-84.51655,30km',
#	'since':'2012-01-01',
#	'until':'2017-01-30',
	'maxTweets':50,
	}

	encoding = 'utf-8'

	startingBrowser = tweeterBrowser(params)
	results = startingBrowser.getTweets()
	client = setAuth()

	with io.open('./Results/testFile.csv', 'w', encoding=encoding) as outputFile:
		for result in results:
			timeline_endpoint = "https://api.twitter.com/1.1/statuses/show/"+result.split(';')[-2]+".json"
			try:
				response, data = client.request(timeline_endpoint)
				tweets = json.loads(data)
			except:
				print "Twitter weird response. Try to see on browser: %s" % tweets
				sys.exit()
				return

			outputLine = []
			if 'coordinates' in tweets.keys():
				if tweets['coordinates']:
					outputLine.append(unicode(tweets['coordinates']['type']))
					outputLine.append(unicode(tweets['coordinates']['coordinates'][1]))
					outputLine.append(unicode(tweets['coordinates']['coordinates'][0]))
				else:
					outputLine.append(u'NA')
					outputLine.append(u'NA')
					outputLine.append(u'NA')
			else:
				outputLine.append(u'NA')
				outputLine.append(u'NA')
				outputLine.append(u'NA')
			if 'place' in tweets.keys():
				outputLine.append(unicode(tweets['place']))
			else:
				outputLine.append(u'NA')
			if 'user' in tweets.keys():
				outputLine.append(unicode(tweets['user']['location']))
			else:
				outputLine.append(u'NA')
			if 'created_at' in tweets.keys():
				outputLine.append(unicode(tweets['created_at']))
			else:
				outputLine.append(u'NA')
			if 'text' in tweets.keys():
				tempText = tweets['text'].replace('\t', ' ')
				tempText = tempText.replace('\n', ' ')
				tempText = tempText.replace('"', '')
				outputLine.append(tempText)

			outputLine.append('\n')
			outputFile.write(unichr(9).join(outputLine))


if __name__ == '__main__':
	main()