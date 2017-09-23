#{
#  "url": "https://gateway.watsonplatform.net/natural-language-understanding/api",
#  "username": "10f91228-88ff-4a29-a0ae-ddba6d0f48b0",
#  "password": "KjourMQXKT5L"
#}

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    Features

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='10f91228-88ff-4a29-a0ae-ddba6d0f48b0',
    password='KjourMQXKT5L')

response = natural_language_understanding.analyze(
    text='Arson on 49XX RAPID RUN RD, Cincinnati, OH (via http://t.co/oCHXeNDI): Calls For Service-CARSON COVEDALE PK http://t.co/kBliJIMm',
    features=[Features.Entities(), Features.Keywords(), Features.Emotion() ])

print(json.dumps(response, indent=2))