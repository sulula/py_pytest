import os
from allure_pytest import plugin as allure_plugin
import pytest
from page.searchpage import Search


class TestSearch:
    def test_string_1(self, driver):
        ele = Search().search_str(driver, "test")
        print('test_string', ele.text)
        assert ele.text == "test"

    def test_number_2(self, driver):
        ele = Search().search_number(driver, "1")
        label = ele.get_attribute('aria-label')
        print('test_number', ele.get_attribute('aria-label'))
        assert label.find("1") >= 0


    def test_number_3(self):
        assert 1 == 3


if __name__ == '__main__':
    pytest.main(['-s', 'test_search_page.py', '--html=./report/result.html', '-—alluredir=./report/xml'])
    # pytest.main(['-s', './testcase/test_search2.py', '--alluredir', './report/xml'])
    os.system('allure gengerate ./report/xml -o ./allreport --clean')
