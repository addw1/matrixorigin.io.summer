package com.ning.codebot.common.chat.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@AllArgsConstructor
@Data
public class MessageDto {
    String sender;
    String content;
}
