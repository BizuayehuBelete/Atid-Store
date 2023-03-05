import allure
import pytest
import requests
from server.API.constants.constant_for_search import search


class test_search():
    @allure.description("search correct in the website")
    def test_search_correctly(self):
        url = search.url
        body = search.data
        res = requests.post(url, json=body)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description("search null in the website")
    def test_search_null(self):
        url = search.url
        body = search.data1
        res = requests.post(url, json=body)
        res_data = res.json()
        assert res.status_code == 404
        assert res.elapsed.total_seconds() < 10


if __name__ == '__main__':
    test_search()
