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
	temp = "/1.1/statuses/show/455461039371350016.json"
#	timeline_endpoint = "https://api.twitter.com/1.1/statuses/show/455461039371350016.json"
	client = setAuth()
	fileName = 'CleanedTweetCrimeComplete.csv'

	with open ('./Results/'+fileName, 'r') as inputFile:
		linesResults = inputFile.readlines()
		counterCoordinates = 0
		for line in linesResults[1:20]:
			lineList = line.split(';')
			if not (len(lineList) != 11):
				idString = lineList[-6]
				timeline_endpoint = "https://api.twitter.com/1.1/statuses/show/"+idString+".json"
				response, data = client.request(timeline_endpoint)
				tweets = json.loads(data)
				if 'coordinates' in tweets.keys():
					counterCoordinates += 1
					print tweets['coordinates']
				if 'place' in tweets.keys():
					print tweets['place']
				if 'user' in tweets.keys():
					print tweets['user']['location']
				if 'text' in tweets.keys():
					print tweets['text']
				if 'created_at' in tweets.keys():
					print tweets['created_at']

		print counterCoordinates

			
if __name__ == '__main__':
	main()