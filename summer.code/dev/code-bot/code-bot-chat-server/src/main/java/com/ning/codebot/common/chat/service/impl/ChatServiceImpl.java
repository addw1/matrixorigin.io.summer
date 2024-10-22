package com.ning.codebot.common.chat.service.impl;

import com.ning.codebot.common.chat.dao.MessageDao;
import com.ning.codebot.common.chat.domain.MessageDto;
import com.ning.codebot.common.chat.domain.entity.Message;
import com.ning.codebot.common.chat.domain.vo.request.ChatMessageReq;
import com.ning.codebot.common.chat.domain.vo.response.ChatMessageResp;
import com.ning.codebot.common.chat.service.ChatService;
import com.ning.codebot.common.chat.service.strategy.msg.AbstractMsgHandler;
import com.ning.codebot.common.chat.service.strategy.msg.MsgHandlerFactory;
import com.ning.codebot.common.client.LLMClient;
import com.ning.codebot.common.repo.domain.entity.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;

@Service
public class ChatServiceImpl implements ChatService {
    @Autowired
    MessageDao messageDao;

    @Autowired
    LLMClient llmClient;

    @Override
    @Transactional
    public Long storeMsg(ChatMessageReq request){
        AbstractMsgHandler<?> msgHandler = MsgHandlerFactory.getStrategyNoNull(request.getMsgType());
        Long msgId = msgHandler.checkAndSaveMsg(request);
        return msgId;
    }

    @Override
    public List<MessageDto> getMessages(String userName, String groupName, Long chatId){
        List<Message> messages = messageDao.getMessages(
                "bot-" +userName,
                groupName,
                chatId
        );
        List<MessageDto> dtos = new ArrayList<MessageDto>();
        for (Message message : messages) {
            MessageDto dto  = MessageDto
                                .builder()
                                .content(message.getContent())
                                .sender(message.getSenderName())
                                .build();
            dtos.add(dto);
        }
        return dtos;
    }



}
