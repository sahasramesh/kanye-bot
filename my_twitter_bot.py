from datetime import datetime
from collections import defaultdict
import tweepy
import random

def KanyeBot():
    CONSUMER_KEY = '7metadWxD4c1yIoCJrCTyYA77'
    CONSUMER_SECRET = 'DvK2CNXIh5oJj2nbn6xH1JK64j3z031O5z4CpEVAM3KGqbeYNZ'
    ACCESS_KEY = '1154847777383276544-0KL98MpXkLL3SlSozevDhXS8m7Knhz'
    ACCESS_SECRET = 'U02lsTKH49LdesNRvXR0F7JC6WLJrjIIqnh7q0dNJVysz'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    senLen = 0
    finalSen = ''
    with open("kanyewords.rtf") as f:
        words = f.read().split()

        word_dict = defaultdict(list)
        for word, next_word in zip(words, words[1:]):
            word_dict[word].append(next_word)

            word = random.choice(words)
    print(word, ' ')
    finalSen+= word +' '

    while not word.endswith("."):
        senLen+= len(word)
        word = random.choice(word_dict[word])
        print(word, ' ')
        finalSen+= word +' '
        senLen+= len(word)

    api.update_status(finalSen)

with open(datetime.now().strftime("%d-%m-%Y"),"w") as file:
    file.write(str(KanyeBot()))
