from kafka import KafkaConsumer
import io
consumer = KafkaConsumer(bootstrap_servers='localhost:9092',auto_offset_reset='earliest',
	value_deserializer=bytes.decode,
	key_deserializer=bytes.decode)
consumer.subscribe(['print'])

for message in consumer:
	print(message.value)
	print( type(message.value) )#.decode('utf8') )
	#print(message.value.decode('utf8') )
	print(message.value.encode('utf8') )
	value = bytearray(message.value.encode('utf8'))
	bytes_reader = io.BytesIO(value[5:])
	print(bytes)
	# bytes_reader = io.BytesIO(msg.value)
	#decoder = avro.io.BinaryDecoder(bytes_reader)
	#reader = avro.io.DatumReader(schema)
	#temp = reader.read(decoder)
	#print(temp)



