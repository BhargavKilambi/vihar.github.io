from twython import Twython
import genson
import json
import requests
from bs4 import BeautifulSoup


def define(word):
    response = requests.get(
        'http://dictionary.reference.com/browse/{}?s=t'.format(word))
    html = response.content
    soup = BeautifulSoup(html, 'html5lib')
    definitions = soup.find_all('div', {'class': 'def-content'})
    # for meaning in definitions:
    #    print(meaning.text.strip())
    if definitions:
        print('The Definition - {}'.format(definitions[0].text.strip()))
    else:
        print('Definition not found on web:(\n')


# This connects to my twitter account and brings the tweets

t = Twython('92UbSi1YbvPI5umlJVV6xwL62',
            'EMM846L8yfj3hP5T14mdxHKDII1rb9AV7whUUjwVy4X4ZTcx0c',
            '2257672447-BSkO8JVaFWzrPebefP3bCrY09AAh11Tq1yaX66c',
            'BrgI4HvNpqs1tg7u1q0JBYuBH5uePGHW5i1GjRrhZxo8U')

tl = t.get_home_timeline()
json.dumps(tl)
s = genson.Schema()
s.add_object(tl)
tweets = []


def timeline():
    for i in range(0, len(tl)):
        # pprint(tl[i]['text'])
        tweets.append(tl[i]['text'])
    tweets_dict = {'tweets': tweets}
    return tweets_dict


# This function is to load all the dictionary word and
# this function will return all the words.

def words():
    file = open('3esl.txt', 'r')
    lines = file.readlines()
    array = []
    for line in lines:
        array.append(line.strip())
    return array

# THis fucnction is to compare tweets with the dict


def check():
    tweets = timeline()
    nm = []
    tweet_count = 1
    for tweet in tweets['tweets']:
        print('{}\n'.format(tweet_count))
        print('{}\n'.format(tweet))
        print('Spliting the tweet :)')
        tw = tweet.split()
        print('{}\n'.format(tw))
        w = words()
        for i in tw:
            if i.lower() in w:
                print('{} Is Found in Dictionary - Match\n'.format(i))
            else:
                print('{} - Not found in Dictionary\n'.format(i))
                print('Searching Web')
                nm.append(i)
                define(i)
        print('######################################\n\n\n')
        tweet_count += 1
    # print(nm)


# Finally Interpreting.
check()
