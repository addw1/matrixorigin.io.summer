class Config():
    def __init__(self):
        self.subscribe_url = "http://localhost:8080/codebot/repo/upload/"
        self.send_code_url = "http://localhost:8080/codebot/login/valid?code="
        self.chat_url = "http://localhost:8080/codebot/chat/"
        self.auth_url = "http://localhost:8080/codebot/login/authorize"
        self.check_status = "http://localhost:8080/codebot/repo/check?repo_name="