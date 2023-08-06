# pydingbot
[![Build Status](https://travis-ci.org/seniverse/pydingbot.svg?branch=main)](https://travis-ci.org/Clarmy/pydingbot)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Clarmy/pydingbot/issues)

pydingbot 是一个让钉钉机器人更好用的包。

## 安装
你可以用 `pip` 来安装pydingbot
```shell
$ pip install pydingbot
```

## 使用

在使用pydingbot之前，首先你需要在钉钉群里添加你的机器人，安全设置选择**加签**，然后点开“机器人设置”找到 **webhook** 和 **secret**（秘钥），这些是使用机器人所必须的信息，webhook和secret的来源如图所示：   

![config](docs/static/config.png)   

使用示例：

```python
>>> from pydingbot import inform

>>> webhook = 'https://oapi.dingtalk.com/robot/send?access_token=170d919d864e90502b48603ecbcd7646701bd66cc590f495bac1b7c5049e171e'

>>> secret = 'SEC474937571de1506cdd724af0d5866f4fa2788968032a2d6d982da988bea4e5de'

>>> inform(webhook=webhook, secret=secret, title='My Title', text='My Text')

>>> inform(webhook=webhook, secret=secret, title='My Title', text='My Text', at_mobiles['158xxxx2009'], at_all=True)
```
如果你的配置正确，那么消息应该就已经发送到你的钉钉群里了。 