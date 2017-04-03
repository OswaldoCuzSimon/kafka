# kafka

## Synopsis
Aplicacion que captura tweets con python y envia a un topic de Kafka
que usa la API de striming para filtrar las palabras que se repiten
3 veces o mas en un tweet y se envian al a otro topic
Este ultimo tiene un consumer en java que solo imprime el mensaje

## Instalacion

### 1 Crear un entorno virtual
```virtualenv -p /usr/bin/python3.4 env ```

### 2 Activar el entorno
```source env/bin/activate```

### 3 Instalar las librerias
```pip install -r requirements.txt```

### 4 Correr el contenedor [spotify/kafka](https://hub.docker.com/r/spotify/kafka/)
```docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 spotify/kafka```

### 5 Ejecutar el [Stream](https://github.com/OswaldoCuzSimon/kafka/blob/master/stream/WordCountStream.java) y [Consumer](https://github.com/OswaldoCuzSimon/kafka/blob/master/stream/Consumer.java)
```shell
cd stream
javac -cp "kafka-path/libs/*" WordCountStream.java
java -cp "kafka-path/libs/*":. WordCountStream
javac -cp "kafka-path/libs/*" Consumer.java
java -cp "kafka-path/libs/*":. Consumer
```
### 6 Crear tokens.py
```python
import os

os.environ['CONSUMER_KEY']      = "YOUR_CONSUMER_KEY"
os.environ['CONSUMER_SECRET']   = "YOUR_CONSUMER_SECRET"
os.environ['ACCESS_TOKEN']      = "YOUR_ACCESS_TOKEN"
os.environ['ACCESS_TOKEN_SECRET'] = "YOUR_ACCESS_TOKEN_SECRET"
```
### 7 Ejecutar el [producer](https://github.com/OswaldoCuzSimon/kafka/blob/master/TweetStream.py)
```python TweetStream.py```

### Good Luck
