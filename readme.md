# 拉取
ql repo https://github.com/zijiahong/bilibili.git "BILIBILI|bilibili"


# 配置文件参数

## biliVerify
Key(字段)	Value(值)	说明
biliCookies	str	bilibili 的 cookie，获取方式请查看使用说明
## taskConfig

Key(字段)	Value(值)	说明
matchGame	[false,true]	是否开启赛事预测。
showHandModel	[false,true]	true ：压赔率高的，false：压赔率低的。
predictNumberOfCoins	[1,10]	单次预测的硬币数量,默认为1。
minimumNumberOfCoins	[1,无穷大]	预留的硬币数，低于此数量不执行赛事预测。
taskIntervalTime	[1,无穷大]	任务之间的执行间隔,默认10秒,云函数用户不建议调整的太长，注意免费时长。
numberOfCoins	[0,5]	每日投币数量,默认 5 ,为 0 时则不投币。
reserveCoins	[0,4000]	预留的硬币数，当硬币余额小于这个值时，不会进行投币任务，默认值为 50。
selectLike	[0,1]	投币时是否点赞，默认 0, 0：否 1：是。
monthEndAutoCharge	[false,true]	年度大会员月底是否用 B 币券自动充电，默认 true。
chargeDay	[1，28]	充电日期，默认为每月28号。
chargeForLove	[充电对象的 uid]	给指定 up 主充电，可填写充电对象的 UID ,默认给作者充电。
giveGift	[false,true]	直播送出即将过期的礼物，默认开启，如需关闭请改为 false。
upLive	[0,送礼 up 主的 uid]	直播送出即将过期的礼物，可填写指定 up 主的 UID ，为 0 时则随随机选取一个 up 主。
silver2Coin	[false,true]	银瓜子兑换硬币，默认开启，如需关闭请改为 false。
devicePlatform	[ios,android]	手机端漫画签到时的平台，建议选择你设备的平台 ，默认 ios。
coinAddPriority	[0,1]	0：优先给热榜视频投币，1：优先给关注的 up 投币。
userAgent	浏览器 UA	你的浏览器的 UA。
skipDailyTask	[false,true]	是否跳过每日任务，默认true,如果关闭跳过每日任务，请改为false。


* tips:从 1.0.0 版本开始，随机视频投币有一定的概率会将硬币投给本项目的开发者。

* 默认配置文件是给开发者充电，给自己充电或者给其他 up 充电，请改为对应的 uid

* userAgent 建议使用你自己真实常用浏览器 UA，如果不知道自己的 UA 请到配置生成页面查看你的 UA

## pushConfig

字段类型	Key(字段)	Value(值)	说明
server 酱	SC_KEY	str	Server 酱老版本 key，SCU 开头的
server 酱 turbo	SCT_KEY	str	Server 酱 Turbo 版本 key，SCT 开头的
Telegram	TG_USE_CUSTOM_URL	[false,true]	是否开启 TGbotAPI 反代
Telegram	TG_BOT_TOKEN	str	TG 推送 bot_token,若开启反代，需填写完整反代 url https://***/bot?token=xxx
Telegram	TG_USER_ID	str	TG 推送的用户/群组/频道 ID
PUSH PLUS	PUSH_PLUS_TOKEN	str	push plus++推送的token
钉钉	DING_TALK_URL	str	钉钉推送的完整 URL,e.g.https://oapi.dingtalk.com/robot/send?access_token=xxx
钉钉	DING_TALK_SECRET	str	钉钉推送的密钥
推送代理	PROXY_HTTP_HOST	str	推送使用 HTTP 代理,e.g.127.0.0.1
推送代理	PROXY_SOCKET_HOST	str	推送使用 SOCKS(V4/V5)代理,e.g.127.0.0.1
推送代理	PROXY_PORT	int	推送代理的端口，默认 0 不代理
企业微信群消息	WE_COM_TOKEN	str	企业微信，群消息非应用消息
企业微信应用	WE_COM_APP_CORPID	str	企业 id 获取方式参考 :获取
企业微信应用	WE_COM_APP_CORP_SECRET	str	应用的凭证密钥
企业微信应用	WE_COM_APP_AGENT_ID	int	企业应用的 id，整型
企业微信应用	WE_COM_APP_TO_USER	str	指定接收消息的成员，成员 ID 列表 默认为@all

* tips:PROXY_HTTP_HOST和PROXY_SOCKET_HOST仅需填写一个。
* tips:钉钉推送密钥可不填，不填仅用关键词验证。