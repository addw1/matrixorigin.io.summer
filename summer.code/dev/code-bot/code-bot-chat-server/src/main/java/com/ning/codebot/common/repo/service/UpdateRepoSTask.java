package com.ning.codebot.common.repo.service;
import com.ning.codebot.common.client.LLMClient;
import com.ning.codebot.common.repo.dao.RepoDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
/**
@Service
public class UpdateRepoSTask {
    @Autowired
    RepoDao repoDao;
    @Autowired
    LLMClient llmClient;
    @Scheduled(fixedDelay = 240000)
    public void performCronTask() {
        List<String> repos = repoDao.getUnsuccessRepo();
        List<String> successRepos = new ArrayList<String>();
        List<String> failRepos = new ArrayList<String>();
        for(String repo : repos) {
            if (llmClient.subscribeRepo(repo))
                successRepos.add(repo);
            else
                failRepos.add(repo);
        }
        // update success one
        for (String repo : successRepos) {
            repoDao.updateSuccessRepo(repo);
        }

        //add times for fail repo
        for (String repo : failRepos) {
            repoDao.updateTimesRepo(repo);
        }

        //change status
        repoDao.updateUnsuccessfulRepos();

    }
}
**/