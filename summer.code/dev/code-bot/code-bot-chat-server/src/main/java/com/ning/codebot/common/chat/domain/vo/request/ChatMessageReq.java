package com.ning.codebot.common.chat.domain.vo.request;

import io.swagger.annotations.ApiModelProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.validation.constraints.NotNull;

/**
 * holder for chat message
 */
@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class ChatMessageReq {

    @ApiModelProperty("Room Name")
    @NotNull
    private String roomName;

    // Now only support text type
    //TODO: support more types in the feature
    @ApiModelProperty("Message Type")
    @NotNull
    // 1: text type
    private Integer msgType;

    @ApiModelProperty("Message Body")
    @NotNull
    private String content;

    @ApiModelProperty("senderName")
    @NotNull
    private String senderName;

}