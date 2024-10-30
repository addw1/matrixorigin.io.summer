<img src="https://img.shields.io/badge/platform-MacOS-white.svg" alt="macos"/> <img src="https://img.shields.io/badge/platform-Linux-9cf.svg" alt="linux"/><img src="https://img.shields.io/badge/License-Apache%202.0-red.svg" alt="license"/> <img src="https://img.shields.io/badge/Language-Java-blue.svg" alt="language"/> <img src="https://img.shields.io/badge/Language-Python-green.svg" alt="language"/>
<br>

# MatrixAI 

本项目希望开发一个github仓库对话机器人。用户通过输入仓库对应URL后，机器人能够回答关于仓库的相关信息，帮助用户学习使用相应仓库。在系统设计上采用了**springboot** + **Flask**的混合框架。同时基于**matrix one**完成了向量存储 && 检索以构建本地知识库。

<img src="./img/2.png" alt="8bit-gamepad" style="zoom: 67%;" />

### Why matrix one?

MatrixOne的HSTAP数据库技术与Dell ObjectScale的可扩展对象存储相结合，为AI生成内容（AIGC）提供了强大的平台。该解决方案的高性能和可扩展性使组织能够快速高效地训练和部署人工智能模型，从而加速有价值的见解和内容的生成。![dellmatrix](./img/dellmatrix.png)



### Why springboot ?

:one: 开发人员生产力的大幅提升

:two: 简化的高级抽象

:three: 微服务和云原生友好



## 💪  功能介绍

### 💬 对话

多轮对话支持： 帮助您在持续交流中不断学习和优化对话内容。<br>
仓库选择功能： 允许您选择不同的知识仓库来获取最相关的回答。<br>
**<font color = red>开发中 </font>**:briefcase: :通过引入 Graph RAG 技术，提升 bot 对仓库内容的理解能力，从而提供更准确的回答。

### :card_file_box: 仓库管理
**一键上传**： 轻松上传您的仓库，快速启动 GPT 的量子速读功能，让智能助手迅速为您处理和分析数据。:fire:<br>
**超细颗粒度更新** 支持根据不同版本的commit进行更新，帮助您从头开始了解项目。

### 📜 对话历史

**历史消息**：对话历史自动保存，一键查看。<br>
**bot记忆模块**：基于滑动窗口🪟,在多轮对话中让AI保持长期记忆。

## 客户端
采用pyqt5编写。





## 后端
💥 技术栈 **springboot**, **mybatis plus**, **matrix one**, **spring security**, **redis**, **mysql**, **flask** <br>
  <code><img width="10%" src="https://www.vectorlogo.zone/logos/java/java-ar21.svg"></code><img width="10%" src="https://www.vectorlogo.zone/logos/springio/springio-ar21.svg"><code><img width="10%" src="https://www.vectorlogo.zone/logos/mysql/mysql-ar21.svg"></code>  <code><img width="10%" src="https://www.vectorlogo.zone/logos/redis/redis-ar21.svg"></code><img width="10%" src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.svg">

## 贡献规则
参考contributing.md

