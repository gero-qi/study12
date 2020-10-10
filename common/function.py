import os
import configparser


def project_path():
    return os.path.realpath(__file__).split("common")[0]


def config_url():
    config = configparser.ConfigParser()
    print(project_path() + "config")
    config.read(project_path() + "config")
    return config.get('testUrl', 'url')


if __name__ == '__main__':
    print("项目名称：" + project_path())
    print("测试地址:" + config_url())
