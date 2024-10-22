package com.ning.codebot.common.chat.service;

import com.ning.codebot.common.chat.domain.MessageDto;
import com.ning.codebot.common.chat.domain.vo.request.ChatMessageReq;
import com.ning.codebot.common.chat.domain.vo.response.ChatMessageResp;

import java.util.List;

/**
 *  handle chat messages
 */

public interface ChatService {
    /**
     * Send message
     * @param request
     */
    Long storeMsg(ChatMessageReq request);

    /**
     * get messages
     */
    List<MessageDto> getMessages(String userName, String groupName, Long chatId);
}
