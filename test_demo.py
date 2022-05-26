import requests


class Test_Demo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.text)
        print(r.json())

    def test_query(self):
        payload = {'name': 'll'}
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_form(self):
        payload = {'name': 'll'}
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_file(self):
        file = {'file': open("test.xls", 'rb')}
        r = requests.post('https://httpbin.testing-studio.com/post', file=file)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {'name': 'll'}
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200


    def test_post_cookie(self):
        payload = {'Cookie': 'hogw=school'}
        r = requests.post('https://httpbin.testing-studio.com/cookoes', headers=payload)
        print(r.request.headers)
        # assert r.status_code == 200
