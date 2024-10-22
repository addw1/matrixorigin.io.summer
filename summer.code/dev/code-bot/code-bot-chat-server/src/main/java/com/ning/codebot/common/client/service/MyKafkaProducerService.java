package com.ning.codebot.common.client.service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.stereotype.Service;
import org.springframework.util.concurrent.ListenableFuture;
import org.springframework.util.concurrent.ListenableFutureCallback;


@Service
public class MyKafkaProducerService {

    private static final Logger logger = LoggerFactory.getLogger(MyKafkaProducerService.class);

    private final KafkaTemplate<String, Object> kafkaTemplate;

    public MyKafkaProducerService(KafkaTemplate<String, Object> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void sendMessage(String topic, Object o) {
        ListenableFuture<SendResult<String, Object>> future = kafkaTemplate.send(topic, o);
        future.addCallback(new ListenableFutureCallback<SendResult<String, Object>>() {
            @Override
            public void onSuccess(SendResult<String, Object> sendResult) {
                logger.info("Sucess: " + topic + "-> " + sendResult.getProducerRecord().value().toString());
            }
            @Override
            public void onFailure(Throwable throwable) {
                logger.error("Producer send：{} fail，reason：{}", o.toString(), throwable.getMessage());
            }
        });
    }
}