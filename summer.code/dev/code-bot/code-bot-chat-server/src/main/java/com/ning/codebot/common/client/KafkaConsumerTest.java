package com.ning.codebot.common.client;


import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class KafkaConsumerTest {
    public static void main(String[] args) {
        //System.out.println("test");
        Map<String, Object> consummerConfig = new HashMap<String, Object>();
        consummerConfig.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        consummerConfig.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        consummerConfig.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        consummerConfig.put(ConsumerConfig.GROUP_ID_CONFIG, "group1");
        // create consumer instant
        KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(consummerConfig);
        consumer.subscribe(Collections.singletonList("test"));
        // get the data from kafka
         final ConsumerRecords<String, String> records = consumer.poll(100);
         for (ConsumerRecord<String, String> record : records) {
             System.out.println(record.key() + ":" + record.value());
         }
        // kafka close the pipe
        consumer.close();


    }
}
