#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi
import os, random, json, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

config = {
    'Region': 'gz',
    'secretId': 'AKIDLakvxosWaUDl9MOj5jJ1zqV3PkxydQ2j',
    'secretKey': 'mQuLdjebWSODuPnCcxo5FQl6LPPNMI6j',
    'method': 'post'
}
def emotion(content=''):
    module = 'wenzhi'
    service = QcloudApi(module, config)

    action = 'TextSentiment'
    params = {
        'content': content, #utf8 only
        'type': 1 #（可选参数，默认为4） 1：电商；2：APP；3：美食；4：酒店和其他。
    }
    '''
    samples = 'samples/pos'
    entries = os.listdir(samples)
    res = []
    for e in entries:
        with open(os.path.join(samples, e)) as f:
            params['content'] = f.read()
#            print params
            res.append(json.loads(service.call(action, params)))
    return res
    '''
    return json.loads(service.call(action, params))


def fetch(symbol='SH601985', page=1, count=20, source='user', sort='time'):
    '''module = 'wenzhi'
    service = QcloudApi(module, config)
    action = 'ContentGrab' # 竟然不支持https，要自己加个代理
    tpl = 'http://qcloud.logger.im:8081/statuses/search.json?count=20&comment=0&symbol=%s&hl=0&source=user&page=%d&sort=time&_=%d'
    url = tpl % (symbol, page, random.randint(0, 10e6))
    params = {'url': url}
    res = json.loads(service.call(action, params))
    content = res['content']
    with open('samples/xueqiu', 'w+') as f:
        f.write(content)
    res = json.loads(res)
'''
    tpl = 'http://qcloud.logger.im:8081/statuses/search.json?count=%d&comment=0&symbol=%s&hl=0&source=%s&page=%d&sort=%s&_=%d'
    url = tpl % (count, symbol, source, page, sort, random.randint(0, 10e6))
    res = urllib2.urlopen(url).read()
    return json.loads(res)

#print emotion()
# fetch 100 message and get the score
def calc():
    res = fetch(count=10, page=2, source='user', sort='time')
    score = 0
    for item in res['list']:
        s = emotion(item['text'])
        print s, item['title']
        score += s['positive'] - 0.5 # 还可以进行调整

    return score
#SH601668
# test symbol, source[all|user] sort[time|alpha]
print 'current score', calc()
