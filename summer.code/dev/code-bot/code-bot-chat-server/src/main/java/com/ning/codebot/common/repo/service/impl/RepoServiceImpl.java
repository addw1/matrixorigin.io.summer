package com.ning.codebot.common.repo.service.impl;

import com.ning.codebot.common.repo.dao.RepoDao;
import com.ning.codebot.common.repo.domain.entity.UserRepo;
import com.ning.codebot.common.repo.service.RepoService;
import com.ning.codebot.common.repo.service.adapter.UserRepoAdapter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class RepoServiceImpl implements RepoService {

    @Autowired
    RepoDao repoDao;

    @Override
    public void storeRepo(String userName, String repoName) {
        if(repoDao.hasRepo(userName, repoName)) return ;
        repoDao.save(UserRepoAdapter.buildUserRepo(userName, repoName));
    }

    @Override
    public List<String> getRepos(String userName){
        List<UserRepo> repoEntities = repoDao.getRepos(userName);
        List<String> repos = new ArrayList<String>();
        for(UserRepo repo : repoEntities){
            repos.add(repo.getRepoName());
        }
        return repos;
    }
}
