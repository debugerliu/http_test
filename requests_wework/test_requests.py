import random
import time

import pytest
import requests


@pytest.fixture(scope='session')
def test_get_token():
    corpid = "ww35a24a92f146f3ab"
    corpsecret = 'sGqyxfeoc288ZoEjn3TpJH8s8-iZF7ERTPph2o6yMZc'
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    # print(r.json()['access_token'])
    return r.json()['access_token']


def test_get_member(test_get_token, userid='ChengBai'):
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token}&userid={userid}')
    print(r.json()['errcode'])
    return r.json()


def test_creat_member(userid, name, mobile, test_get_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": "1",
    }
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token}', json=data)
    # print(r.text)
    return r.json()


def test_delete_member(userid, test_get_token):
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_token}&userid={userid}')
    # print(r.text)
    return r.json()


def test_create_data():
    data = [(str(random.randint(0, 9999)), 'zhangsan24', str(random.randint(13800000000, 13900000000))) for x in
            range(10)]
    print(data)
    return data


w = [('5597', 'zhangsan24', '13886050962'), ('8038', 'zhangsan24', '13811328335'), ('4735', 'zhangsan24', '13855000357'), ('5457', 'zhangsan24', '13893647030'), ('4572', 'zhangsan24', '13825376644'), ('5402', 'zhangsan24', '13814658271'), ('8586', 'zhangsan24', '13805064973'), ('8090', 'zhangsan24', '13866207247'), ('2130', 'zhangsan24', '13819620355'), ('4143', 'zhangsan24', '13873527511')]


@pytest.mark.parametrize('userid, name, mobile', w)
def test_all(userid, name, mobile, test_get_token):
    # print(test_creat_member(userid, name, mobile, test_get_token)['errmsg'])
    # print(test_delete_member(userid, test_get_token)['errmsg'])
    assert 'created' == test_creat_member(userid, name, mobile, test_get_token)['errmsg']
    # assert 'deleted' == test_delete_member(userid, test_get_token)['errmsg']
    # assert 'created' == test_creat_member(userid, name, mobile)['errmsg']
    # assert name == test_get_member(userid)['name']
