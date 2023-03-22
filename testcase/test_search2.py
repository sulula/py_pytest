import os
import requests
import pytest


class TestCase:
    # def setup(self):
    #     # global home
    #     self.home = Home()
    source = [
        {
            "name": "gemey",
            "age": "33"
        }, {
            "name": "fred",
            "age": "22"
        }, {
            "name": "xxx",
            "age": "11"
        }
    ]

    def test_api(self):
        # url="http://httpbin.org/get"

        res = requests.get("http://httpbin.org/get?name=gemey&age=22")
        res_dict = res.json()
        print('res:', res_dict)

        assert res_dict.get("args").get("age") == "22"

    def test_api_1(self):
        # url="http://httpbin.org/get"
        params = {
            "name": "gemey",
            "age": 22
        }
        res = requests.get("http://httpbin.org/get", params=params)
        res_dict = res.json()
        print('res:', res_dict)

        assert res_dict.get("args").get("age") == "22"

    @pytest.mark.parametrize("data", source)
    def test_api_2(self, data):
        # url="http://httpbin.org/get"
        name = data.get("name")
        age = data.get("age")
        params = {
            "name": name,
            "age": age
        }
        res = requests.get("http://httpbin.org/get", params=params)
        res_dict = res.json()
        print('res:', res_dict)

        assert res_dict.get("args").get("age") == age

# def test_number(self):
#     module = self.home.search(1)
#     ele = module.search_number()
#     print('test_number')
#     assert ele.get_attribute('aria-label').find("1") >= 0
#
# def test_number2(self):
#     assert False

# if __name__ == '__main__':
# pytest.main(['-s', '--html=./report/result.html', '-—alluredir=./report'])
