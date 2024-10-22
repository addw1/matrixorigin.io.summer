package com.ning.codebot.common.repo.controller;

import com.ning.codebot.common.chat.domain.vo.response.ChatMessageResp;
import com.ning.codebot.common.client.LLMClient;
import com.ning.codebot.common.client.service.MyKafkaProducerService;
import com.ning.codebot.common.common.utils.RequestHolder;
import com.ning.codebot.common.domain.vo.response.ApiResult;
import com.ning.codebot.common.repo.domain.GetRepoReq;
import com.ning.codebot.common.repo.domain.RepoUploadReq;
import com.ning.codebot.common.repo.service.RepoService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("codebot/repo")
@Api(tags = "The interface for chat service")
@Slf4j
public class RepoController {

    @Autowired
    RepoService repoService;
    @Autowired
    private MyKafkaProducerService producer;
    @Value("${kafka.topic.my-topic2}")
    String myTopic;

    @PostMapping("/upload")
    @ApiOperation("subscribe the repository")
    public ApiResult<Object> sendMsg(@Valid @RequestBody RepoUploadReq request) {
        // store in DB
        repoService.storeRepo(request.getUserName(), request.getRepoName());
        // send to the kafka
        producer.sendMessage(myTopic, request.getRepoName());
        return ApiResult.success();
    }

    @GetMapping("/groups")
    @ApiOperation("get users' subscribe")
    public ApiResult<List<String>> getGroups(@Valid @RequestParam("userName") String userName){
        List<String> repos = repoService.getRepos(userName);
        return ApiResult.success(repos);
    }

}