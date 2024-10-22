package com.ning.codebot.common.client.entity;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ChatMessage {

    private Long id;
    private String senderName;
    private String groupName;
    private String content;
    public ChatMessage(Long id, String senderName, String groupName, String content) {
        this.id = id;
        this.senderName = senderName;
        this.groupName = groupName;
        this.content = content;
    }
}