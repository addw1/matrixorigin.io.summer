package com.ning.codebot.common;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;


@SpringBootApplication(scanBasePackages = {"com.ning.codebot"})
@MapperScan({"com.ning.codebot.common.**.mapper"})
@EnableScheduling
public class CodeBotApplication {

    public static void main(String[] args) {
        SpringApplication.run(CodeBotApplication.class,args);
    }

}