#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi
import os, random, json

config = {
    'Region': 'gz',
    'secretId': 'AKIDLakvxosWaUDl9MOj5jJ1zqV3PkxydQ2j',
    'secretKey': 'mQuLdjebWSODuPnCcxo5FQl6LPPNMI6j',
    'method': 'post'
}
def emotion():
    module = 'wenzhi'
    service = QcloudApi(module, config)

    action = 'TextSentiment'
    params = {
        'content': '', #utf8 only
        'type': 1 #（可选参数，默认为4） 1：电商；2：APP；3：美食；4：酒店和其他。
    }
    samples = 'samples/pos'
    entries = os.listdir(samples)
    res = []
    for e in entries:
        with open(os.path.join(samples, e)) as f:
            params['content'] = f.read()
#            print params
            res.append(json.loads(service.call(action, params)))

    return res


def fetch(symbol='SH601985', page=1):
    module = 'wenzhi'
    service = QcloudApi(module, config)

    action = 'ContentGrab' # 竟然不支持https，要自己加个代理
    tpl = 'https://xueqiu.com/statuses/search.json?count=20&comment=0&symbol=%s&hl=0&source=user&page=%d&sort=time&_=%d'
    url = tpl % (symbol, page, random.randint(0, 10e6))
    params = {'url': url}
    content = service.call(action, params)
    with open('samples/xueqiu', 'w+') as f:
        f.write(content)
    res = json.loads(content)
    return res

#print emotion()
print fetch()

#action = 'ContentGrab'
#params = {'url':'http://kit.logger.im/static/ashare.html'}
'''
try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
    #service.setRequestMethod('get')
    #print service.call('DescribeCdnEntities', {})
except Exception, e:
    print 'exception:', e
'''
