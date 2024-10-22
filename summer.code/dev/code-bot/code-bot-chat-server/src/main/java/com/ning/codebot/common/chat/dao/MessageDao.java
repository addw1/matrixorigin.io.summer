package com.ning.codebot.common.chat.dao;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.ning.codebot.common.chat.domain.entity.Message;
import com.ning.codebot.common.chat.mapper.MessageMapper;
import com.ning.codebot.common.repo.domain.entity.UserRepo;
import org.springframework.stereotype.Service;

import java.util.List;

/*
 * store chat message
 */
@Service
public class MessageDao extends ServiceImpl<MessageMapper, Message> {
    public List<Message> getMessages(String botName, String repoName, Long msgId) {
        return lambdaQuery()
                .eq(Message::getSenderName, botName)
                .eq(Message::getRoomName, repoName)
                .gt(Message::getId, msgId)
                .list();
    }
}
