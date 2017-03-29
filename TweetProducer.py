from kafka import KafkaProducer
import time

class TweetProducer:
	def __init__(self,url):
		self.url = url
		self.producer = KafkaProducer(bootstrap_servers=url)

	def sendTweet(self,topic,tweet):
		self.producer.send(topic, str.encode(tweet) )
