package com.ning.codebot.common.repo.service;

import java.util.List;

public interface RepoService {
    void storeRepo(String userName, String repoName);
    List<String> getRepos(String userName);
}
