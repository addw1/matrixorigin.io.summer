package com.ning.codebot.common.chat.controller;
import com.ning.codebot.common.chat.domain.MessageDto;
import com.ning.codebot.common.chat.domain.vo.request.ChatMessageReq;
import com.ning.codebot.common.chat.domain.vo.response.ChatMessageResp;
import com.ning.codebot.common.chat.service.ChatService;
import com.ning.codebot.common.client.entity.ChatMessage;
import com.ning.codebot.common.client.service.MyKafkaProducerService;
import com.ning.codebot.common.common.utils.RequestHolder;
import com.ning.codebot.common.domain.vo.response.ApiResult;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

/**
 * <p>
 * chat interface
 * </p>
 */
@RestController
@RequestMapping("codebot/chat")
@Api(tags = "The interface for chat service")
@Slf4j
public class ChatController {
    @Autowired
    private ChatService chatService;
    @Autowired
    private MyKafkaProducerService producer;
    @Value("${kafka.topic.my-topic1}")
    String myTopic;

    @PostMapping("/msg")
    @ApiOperation("Send meesage")
    public ApiResult<ChatMessageResp> sendMsg(@Valid @RequestBody ChatMessageReq request) {
        // store in the db
        Long msgId = chatService.storeMsg(request);
        // send to the kafka
        producer.sendMessage(myTopic,
                new ChatMessage(
                        msgId,
                        request.getSenderName(),
                        request.getRoomName(),
                        request.getContent()
                ));
        return ApiResult.success(ChatMessageResp.builder().id(msgId).build());
    }

    // get new data
    @GetMapping("/getMes")
    @ApiOperation("get new messages")
    public ApiResult<List<MessageDto>> getNewMessages(@Valid @RequestParam("userName") String userName,
                                                      @Valid @RequestParam("roomName") String roomName,
                                                      @Valid @RequestParam("id") Long id) {
        return ApiResult.success(chatService.getMessages(userName, roomName, id));
    }


}
