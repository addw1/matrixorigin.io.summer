package com.ning.codebot.common.chat.service.strategy.msg;

import com.ning.codebot.common.chat.dao.MessageDao;
import com.ning.codebot.common.chat.domain.entity.Message;
import com.ning.codebot.common.chat.domain.enums.MessageTypeEnum;
import com.ning.codebot.common.chat.domain.vo.request.TextMsgReq;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class TextMsgHandler extends AbstractMsgHandler<TextMsgReq> {
    @Autowired
    private MessageDao messageDao;

    @Override
    MessageTypeEnum getMsgTypeEnum() {
        return MessageTypeEnum.TEXT;
    }

    protected String convertToRowData(String content){
        return content;
    }

}
