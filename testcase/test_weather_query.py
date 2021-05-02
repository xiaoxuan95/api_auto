from utils.http_request import send_http_request
from utils.load_yaml import get_yaml_data
import pytest

cases, list_params = get_yaml_data(func_no='weather_query', test_no='tests_001')


class TestWeatherQuery:

    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def tests_001(self, case, http, expected):
        code, desc, result = send_http_request(http)
        assert code == expected['response']['statusCode']
        assert desc == expected['response']['desc']
        assert str(len(result['hourList'])) == expected['response']['result']['count']

