from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
	producer.send('test', b"test")
	producer.send('test', b"\xc2Hola, mundo!")
	time.sleep(1)
