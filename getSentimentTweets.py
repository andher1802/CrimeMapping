
import io
import re

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    Features

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='10f91228-88ff-4a29-a0ae-ddba6d0f48b0',
    password='KjourMQXKT5L')


filename = 'CleanedLocatedTweets.csv'
encoding = 'utf-8'

def main():

	with io.open('./Results/nlpTweets.csv','w',encoding = encoding) as outputFile:
		with io.open('./Results/'+filename,'r',encoding = encoding) as inputFile:
			inputBuffer = inputFile.readlines()
			outputFile.write(u'\t'.join(['crimeRelatedentity','TweetNumber', 'TweetID', 'Username', 'Date', 'Concept', 'Latitud', 'Longitud', 'Tweet', 'JoyScore', 'BadFeelingsScore',  '', 'Locations mentioned','\n']))
			for line in inputBuffer[3001:]:
				nlpBuffer = []
				lineList = line.strip().split('\t')
				cleanedTweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",lineList[-1]).split())
				cleanedTweet = cleanedTweet.lower()
				try:
					response = natural_language_understanding.analyze(text = cleanedTweet, features=[Features.Entities(), Features.Keywords(), Features.Emotion()])
				except: 
					print cleanedTweet.lower()
					continue
				emotionBuffer = {}
				for key in response:
					if 'emotion' in response.keys():
						emotionBuffer['anger'] = response['emotion']['document']['emotion']['anger']
						emotionBuffer['joy'] = response['emotion']['document']['emotion']['joy']
						emotionBuffer['sadness'] = response['emotion']['document']['emotion']['sadness']
						emotionBuffer['fear'] = response['emotion']['document']['emotion']['fear']
						emotionBuffer['disgust'] = response['emotion']['document']['emotion']['disgust']
						emotionBuffer['badFeelings'] = (emotionBuffer['anger']+emotionBuffer['sadness']+emotionBuffer['fear']+emotionBuffer['disgust'])/4
				if len(response['entities']) > 0:
					bufferEntityCondition = False
					bufferEntityEntities = [] 
					for elements in response['entities']:
						if elements['type'] == 'Crime':
							bufferEntityCondition = True
							bufferEntityEntities.append(unicode(elements['text'].lower()))
					if bufferEntityCondition:
						bufferEntityEntities.append(unicode(lineList[0]))
						bufferEntityEntities.append(unicode(lineList[1]))
						bufferEntityEntities.append(unicode(lineList[2]))
						bufferEntityEntities.append(unicode(lineList[3]))
						bufferEntityEntities.append(unicode(lineList[6]))
						bufferEntityEntities.append(unicode(lineList[11]))
						bufferEntityEntities.append(unicode(lineList[12]))
						bufferEntityEntities.append(unicode(cleanedTweet))
						bufferEntityEntities.append(unicode(emotionBuffer['joy']))
						bufferEntityEntities.append(unicode(emotionBuffer['badFeelings']))
						bufferEntityEntities.append(unicode(''))
						for elements in response['entities']:
							if elements['type'] == 'Location':
								bufferEntityEntities.append(unicode(elements['text'].lower()))
						bufferEntityEntities.append(u'\n')
						outputFile.write(u'\t'.join(bufferEntityEntities))


#u'usage': {u'text_characters': 48, u'features': 3, u'text_units': 1}, 
#u'keywords': [{u'relevance': 0.90568, u'text': u'mind committing'}, {u'relevance': 0.54225, u'text': u'crime'}], 
#u'emotion': {u'document': {u'emotion': {u'anger': 0.186358, u'joy': 0.029298, u'sadness': 0.270078, u'fear': 0.19758, u'disgust': 0.25353}}}, u'language': u'en', 
#u'entities': []

#{u'relevance': 0.33, u'text': u'robbery', u'type': u'Crime', u'count': 1}

#[
#{u'relevance': 0.33, u'text': u'ky', u'disambiguation': {u'subtype': [u'StateOrCounty']}, u'type': u'Location', u'count': 1}, 
#{u'relevance': 0.33, u'text': u'crescent springs', u'disambiguation': {u'subtype': [u'City'], u'name': u'Crescent Springs, Kentucky', u'dbpedia_resource': u'http://dbpedia.org/resource/Crescent_Springs,_Kentucky'}, u'type': u'Location', u'count': 1}, 
#{u'relevance': 0.33, u'text': u'robbery', u'type': u'Crime', u'count': 1}, {u'relevance': 0.33, u'text': u'one day', u'type': u'Quantity', u'count': 1}
#]

if __name__ == '__main__':
	main()