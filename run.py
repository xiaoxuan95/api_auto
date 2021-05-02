import os
import time
import pytest

report_dir = os.path.dirname(__file__)+'/report'
case_dir = os.path.dirname(__file__)+'/testcase'


def gen_report_url():  # 报告端口9004
    report_port = '9004'
    command = r'allure serve {}\xml -p {}'.format(report_dir, report_port)
    try:
        taskinfo = os.popen('netstat -ano | findstr {}'.format(report_port))
        line = taskinfo.readline()
        aList = line.split()
        taskinfo.close()
        pid = aList[4]
        os.popen('taskkill /pid %s /f' % pid)
    except Exception:
        pass
    finally:
        os.popen(command)


def run():
    try:
        pytest.main([str(case_dir), '-vv', '--reruns=1', '--reruns-delay=2', '-n=auto',
                     '--alluredir={}/xml'.format(str(report_dir))])
        os.system(r'allure generate {}/xml -o {}/html --clean'.format(str(report_dir), str(report_dir)))
        time.sleep(5)
        gen_report_url()
    except Exception as e:
        print(e)
        print(str(report_dir))
        raise


def run_p0():
    try:
        pytest.main([str(case_dir), '-vv', '-m=p0', '--reruns=1', '--reruns-delay=2',
                     '--alluredir={}/xml'.format(str(report_dir))])
        os.system(r'allure generate {}/xml -o {}/html --clean'.format(str(report_dir), str(report_dir)))
        time.sleep(5)
        gen_report_url()
    except Exception as e:
        print(e)
        print(str(report_dir))
        raise


if __name__ == '__main__':
    run()