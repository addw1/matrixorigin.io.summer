package com.ning.codebot.common.client;
//如果是SSL接入点实例或者SASL接入点实例，请注释以下第一行代码。

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

public class KafkaProducerTest {
    public static void main(String[] args) {
        // create producer
        // create configuration
        Map<String, Object> configMap = new HashMap<>();
        configMap.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        configMap.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        configMap.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        // producer should set the type k - v
        KafkaProducer<String, String> producer = new KafkaProducer<String, String>(configMap);
        // create data
        // 构建数据要传递3个参数： 主题名称
        //                     key
        //                     value

        ProducerRecord<String, String> record = new ProducerRecord<String, String>(
                "test","key","value"
        );
        // send to the kafka
        producer.send(record);
        //close
        producer.close();
    }
}
