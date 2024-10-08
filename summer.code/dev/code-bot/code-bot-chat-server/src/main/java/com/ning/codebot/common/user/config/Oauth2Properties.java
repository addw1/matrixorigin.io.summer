package com.ning.codebot.common.user.config;


import lombok.Data;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Data
@Component
@ConfigurationProperties(prefix = "github")
public class Oauth2Properties {
    @Value("${github.client.id}")
    private String clientId;
    @Value("49a6e5f1b574455ce6e49b277ebc2bd8bcd2bc3a")
    private String clientSecret;
    @Value("${github.client.authorize-url}")
    private String authorizeUrl;
    @Value("${github.client.redirect-url}")
    private String redirectUrl;
    @Value("${github.client.access-token-url}")
    private String accessTokenUrl;
    @Value("${github.client.user-info-url}")
    private String userInfoUrl;
}
