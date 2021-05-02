import os
import yaml

yaml_dir_path = os.path.dirname(os.path.dirname(__file__)) + '/data/'


def get_yaml_data(*, func_no, test_no) -> tuple:
    """
    读取yaml文件，获取用例数据
    :param func_no: 功能号
    :param test_no: 用例号
    :return:
    """
    case = []
    http = []
    expected = []
    yaml_data_path = yaml_dir_path + '{}.yml'.format(func_no)
    with open(yaml_data_path, encoding='utf-8') as file:
        dat = yaml.load(file.read(), Loader=yaml.SafeLoader, )
        test = dat[test_no]
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    return case, parameters
