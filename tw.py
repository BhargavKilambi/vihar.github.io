from twython import Twython
import genson
import json


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


print(timeline())
