from datetime import datetime, timedelta
from threading import Timer
from collections import defaultdict
import tweepy
import random

#x = datetime.today()
#y = x.replace(day = x.day, hour = 14, minute = 34, second = 0, microsecond = 0) + timedelta(days = 1)
#delta_t = y - x
#secs = delta_t.total_seconds()

def KanyeBot():

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

#t = Timer(secs, KanyeBot)
#t.start()

KanyeBot()
