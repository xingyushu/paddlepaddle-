#!/usr/bin/python3
#encoding:utf-8

import urllib
import urllib
import json
import base64

api_key = "SrhYKqzl3SE1URnAEuZ0FKdT" 
api_secert = "hGqeCkaMPb0ELMqtRGc2VjWdmjo7T89d"

class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
        # token认证的url
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        # 语音合成的resturl
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
        # 语音识别的resturl
        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        # 1.获取token
        token_url = self.token_url % (api_key,api_secert)

        r_str = urllib.urlopen(token_url).read()
        token_data = json.loads(r_str.decode('utf-8'))
        self.token_str = token_data['access_token']
        pass

    def getVoice(self, text, filename):
        # 2. 向Rest接口提交数据
        get_url = self.getvoice_url % (urllib.quote(text), self.cu_id, self.token_str)

        voice_data = urllib.urlopen(get_url).read()
        # 3.处理返回数据
        voice_fp = open(filename,'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        pass

    def getText(self, filename):
        # 2. 向Rest接口提交数据
        data = {}
        # 语音的一些参数
        data['format'] = 'wav'
        data['rate'] = 8000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str
        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        r_data = urllib.urlopen(self.upvoice_url,data=bytes(post_data,encoding="utf-8")).read()
        # 3.处理返回数据
        return json.loads(r_data)['result']



    

