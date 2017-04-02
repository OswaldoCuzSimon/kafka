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

### 5 Ejecutar el Streaming y [Consumer](https://github.com/OswaldoCuzSimon/kafka/blob/master/stream/Consumer.java)
```
javac -cp "kafka-path/libs/*"  	stream/ApplicationResetExample.java
java -cp "kafka-path/libs/*":.  	stream/ApplicationResetExample
javac -cp "kafka-path/libs/*"  	stream/Consumer.java
java -cp "kafka-path/libs/*":.  	stream/Consumer
```

### 6 Ejecuar el producer
```python streaming.py```
