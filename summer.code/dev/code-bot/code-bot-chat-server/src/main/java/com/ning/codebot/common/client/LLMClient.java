package com.ning.codebot.common.client;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.beans.factory.annotation.Autowired;

@Service
public class LLMClient {
    private final RestTemplate restTemplate;

    @Value("${llm.backend.subscribe.url}")
    private String subscribeUrl;

    public LLMClient() {
        this.restTemplate = new RestTemplate();
    }

    public String sendMsg(String repoName, Long userID, String question) {
        // Construct the URL dynamically
        String url = String.format("http://localhost:8080/talks/%s/%d/%s", repoName, userID, question);
        // Make a GET request and return the response
        return restTemplate.getForObject(url, String.class);
    }

    public boolean subscribeRepo(String repoName){
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        String requestBody = String.format("{\"repo_name\": \"%s\"}", repoName);
        HttpEntity<String> request = new HttpEntity<>(requestBody, headers);
        try {
            ResponseEntity<String> response = restTemplate.postForEntity(subscribeUrl, request, String.class);
            return response.getStatusCode().is2xxSuccessful();
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}