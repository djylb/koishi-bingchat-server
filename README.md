# koishi-bingchat-server

2023.2.14 更新 修复返回未知错误。

2023.2.16 更新 优化输出，优化体积，修复损坏的重置功能。

2023.2.16 更新 支持bing聊天。

## 前提准备

- 搭建一个可以运行的koshi服务器
- 拥有一个微软账号，获取bing网页cookie。[cookie-editor](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm/)
- 拥有一台服务器并拥有python环境（如果不需要在服务器在搭建可以不需要）

# **docker 搭建 server （推荐）By D-Jy**

```shell
# 下载项目源码
git clone https://github.com/D-Jy-lab/koishi-bingchat-server.git

# 进入项目
cd koishi-bingchat-server

# 修改cookie.json文件，填入bing网页cookie。
nano cookie.json

# 编译容器
docker build -t duan2001/bingchat .

# 运行容器
docker run -d --name=bingchat --restart=always -p 8007:8007 duan2001/bingchat

```

# 手动搭建
## 待续


## Links

koishi-openchat-server
[https://github.com/houko/koishi-openchat-server](https://github.com/houko/koishi-openchat-server),

OpenChat
[https://github.com/MirrorCY/openchat](https://github.com/MirrorCY/openchat),

EdgeGPT
[https://github.com/acheong08/EdgeGPT](https://github.com/acheong08/EdgeGPT),
