#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import web
import reply
import receive
import time


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "DENGBENYE_CHIKE"   # 自己定义的tokent

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(''.join(list).encode('utf-8'))  # 将py3中的字符串编码为bytes类型
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature:", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            print(e)

    def POST(self):
        try:
            webData = web.data()
            print("web post datails: ", webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == "text":
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"
        except Exception as e:
            print(e) 
            


if __name__ == '__main__':
    h = Handle()
    
