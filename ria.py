from twython import Twython
import genson
import json

# This connects to my twitter account and brings the tweets
def timeline():
    t = Twython('92UbSi1YbvPI5umlJVV6xwL62',
                'EMM846L8yfj3hP5T14mdxHKDII1rb9AV7whUUjwVy4X4ZTcx0c',
                '2257672447-BSkO8JVaFWzrPebefP3bCrY09AAh11Tq1yaX66c',
                'BrgI4HvNpqs1tg7u1q0JBYuBH5uePGHW5i1GjRrhZxo8U')

    tl = t.get_home_timeline()
    json.dumps(tl)
    s = genson.Schema()
    s.add_object(tl)
    tweets = []
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
    for tweet in tweets['tweets']:
        tw = tweet.split()
        print(tw)
        w = words()
        for i in tw:
            if i.lower() in w:
                print('match')
            else:
                print('no match')
                nm.append(i)
    print(nm)

# Finally Interpreting.
check()