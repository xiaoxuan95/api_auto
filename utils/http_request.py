import requests

common_url = 'http://api.apishop.net'


def send_http_request(single_case_info: dict) -> tuple:
    """

    :param single_case_info: 参数数据
    :return:
    """
    http_method = single_case_info.get('method')
    if http_method == 'POST':
        url = common_url + single_case_info.get('path')
        data = single_case_info.get('data')
        res = requests.post(url=url, data=data)
        res_dict = res.json()
        return res_dict['statusCode'], res_dict['desc'], res_dict['result']
    elif http_method == 'GET':
        pass
    else:
        raise Exception("错误的http请求，目前只支持GET、POST，错误的请求方法为:{}".format(http_method))
