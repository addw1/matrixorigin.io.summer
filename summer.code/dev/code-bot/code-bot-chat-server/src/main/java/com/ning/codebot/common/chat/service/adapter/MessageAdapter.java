package com.ning.codebot.common.chat.service.adapter;

import com.ning.codebot.common.chat.domain.entity.Message;
import com.ning.codebot.common.chat.domain.vo.request.ChatMessageReq;

import java.util.Date;

public class MessageAdapter {

    public static Message buildMsgSave(ChatMessageReq request, String content) {

        return Message.builder()
                .senderName(request.getSenderName())
                .roomName(request.getRoomName())
                .content(content)
                .createTime(new Date())
                .build();
    }
}
