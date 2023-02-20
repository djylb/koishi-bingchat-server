# koishi-bingchat-server

2023.2.14 更新 修复返回未知错误。

2023.2.16 更新 优化输出，优化体积，修复损坏的重置功能。

2023.2.16 更新 支持bing聊天。

2023.2.20 更新 修复小bug，更新说明文档。

## 前提准备

- 搭建一个可以运行的koshi服务器
- 拥有一个微软账号，获取bing网页cookie。[cookie-editor](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm/)
- 拥有一台服务器并拥有python环境（如果不需要在服务器在搭建可以不需要）


 要求
- Microsoft Edge (Required)
- 一个能够访问 http://bing.com/chat 的微软账户 (Required)


<details>
  <summary>

  ### 检查账户访问权限 (Required)

  </summary>

- 安装最新版本的 Microsoft Edge
- 打开 http://bing.com/chat
- 如果看到聊天界面说明账户可用

</details>


<details>
  <summary>

  ### 获得Cookie (Required)

  </summary>

- 安装浏览器插件 [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
- 打开该网址 `bing.com`
- 打开安装的浏览器扩展插件
- 点击 "Export" 按钮导出Cookie信息 (This saves your cookies to clipboard)
- 将剪贴板内容粘贴到 `cookies.json`

</details>


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
docker run -d --name=bingchat --restart=always -p <你想要开放的端口>:8007 duan2001/bingchat

#在插件页面填入后端地址：http://127.0.0.1:<上面开放的端口>/chat

# 更新方法
#进入下载项目源码的文件夹
cd koishi-bingchat-server

# 获取更新
git pull origin

# 重新编译容器
docker build -t duan2001/bingchat .

# 删除现有容器
docker stop bingchat
docker rm bingchat

# 运行更新后的容器
docker run -d --name=openchat --restart=always -p <你想要开放的端口>:8006 duan2001/bingchat

```


# 手动搭建
## 待续
参考Dockerfile文件，并按需要修改chat.py文件。


## Links

koishi-openchat-server
[https://github.com/houko/koishi-openchat-server](https://github.com/houko/koishi-openchat-server),

OpenChat
[https://github.com/MirrorCY/openchat](https://github.com/MirrorCY/openchat),

EdgeGPT
[https://github.com/acheong08/EdgeGPT](https://github.com/acheong08/EdgeGPT),
