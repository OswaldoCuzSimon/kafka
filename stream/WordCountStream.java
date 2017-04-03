import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.KStreamBuilder;
import org.apache.kafka.streams.kstream.KTable;
import org.apache.kafka.streams.KeyValue; 

import java.util.Properties;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.function.Function;
import java.util.stream.Collectors;

//https://github.com/confluentinc/examples/blob/3.2.x/kafka-streams/src/main/java/io/confluent/examples/streams/ApplicationResetExample.java
public class WordCountStream {
	private static int count = 0;
	public static void main(final String[] args) throws Exception {

		final Properties streamsConfiguration = new Properties();
		streamsConfiguration.put(StreamsConfig.APPLICATION_ID_CONFIG, "application-reset-demo");
		streamsConfiguration.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
		//streamsConfiguration.put(StreamsConfig.KEY_SERDE_CLASS_CONFIG, "org.apache.kafka.common.serialization.ByteArraySerializer");
		//streamsConfiguration.put(StreamsConfig.VALUE_SERDE_CLASS_CONFIG,"org.apache.kafka.common.serialization.ByteArraySerializer");


		streamsConfiguration.put(StreamsConfig.KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
		streamsConfiguration.put(StreamsConfig.VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());
		streamsConfiguration.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

		final KafkaStreams streams = run(args, streamsConfiguration);
	}

	public static KafkaStreams run(final String[] args, final Properties streamsConfiguration) {
		// Define the processing topology
		final KStreamBuilder builder = new KStreamBuilder();
		final KStream < String, String > input = builder.stream("tweet");

		KStream < String, String > inputFilter = input.mapValues(value ->
			Arrays.asList(value.toLowerCase().split("\\W+")).stream().collect(
					Collectors.groupingBy(Function.identity(), Collectors.counting())
				).entrySet()
                .parallelStream()
                .filter(map -> map.getValue() >= 3)
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue)).toString()
		).filterNot( (key,value) ->
			value.length()<=2
		);//.map( (key,value) -> new KeyValue<>(Integer.toString(++count), value) );
		inputFilter.to(Serdes.String(), Serdes.String(),"print");
		inputFilter.foreach( (key,value) -> {
			System.out.println(key+" -> ["+value+"]");
		});
		final KafkaStreams streams = new KafkaStreams(builder, streamsConfiguration);

		// Delete the application's local state on reset
		if (args.length > 0 && args[0].equals("--reset")) {
			streams.cleanUp();
		}

		streams.start();

		return streams;
	}

}
