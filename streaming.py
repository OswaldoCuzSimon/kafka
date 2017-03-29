# librerias utilizadas durante el proceso
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import sys,re,os
import tokens
from TweetProducer import TweetProducer

consumer_key    = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token    = os.environ['ACCESS_TOKEN']
access_secret   = os.environ['ACCESS_TOKEN_SECRET']
# importa la llaves y tokes de twitter


#funcion que realiza la limpieza del texto en los tweets 
def limpia(tweet):
        tweet = tweet.lower()
        tweet = tweet.encode('utf-8').decode('utf8')
        tweet = tweet.replace('\n', '\t')
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
        tweet = re.sub('[\s]+', ' ', tweet)
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        tweet = tweet.strip('\'"')

        return tweet

class TweetStream(StreamListener):
    def __init__(self):
        StreamListener.__init__(self)
        self.tweetProducer = TweetProducer('localhost:9092')
    def on_data(self, data):

        try:

            dict_data = json.loads(data)
            
            # se eliminan los ceros y se ordena el formato de la fecha, pasandola formato iso
            timestamp = datetime.strptime(dict_data["created_at"].replace("+0000 ",""), "%a %b %d %H:%M:%S %Y").isoformat()
            limpieza = limpia(dict_data["text"])
            print(limpieza)
            self.tweetProducer.sendTweet('tweet',limpieza)
        except:

            # Manda un mensaje de error, si existe alguna exepcion e imprime el tweet que genera error
            print("processing exception")
            print ( sys.exc_info()[0] )

        return True

    # en caso de error imprime el estatus
    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    listener = TweetStream()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    
    stream = Stream(auth, listener)

    stream.filter(track=['bbva', 'bancomer', 'hsbc', 'banamex','banorte'])
