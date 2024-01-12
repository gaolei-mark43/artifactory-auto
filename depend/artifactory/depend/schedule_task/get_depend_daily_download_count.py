# -*- coding: utf-8 -*-
import requests
import datetime
from tqdm import tqdm

# artifactory_base_url
aql_url = "https://depend.artifactory.com/artifactory/api/search/aql"
repo_base_url = "https://depend.artifactory.com/artifactory/api/repositories"
headers = {
        'Authorization': 'Basic XXXXXXXXXXXXXXXX'
    }


# 装饰器，统计函数执行时间
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print('函数{}运行时间为{}'.format(func.__name__, end_time - start_time))
    return wrapper


# 获取所有仓库名称
def get_all_repo_name():
    payload = {}
    response = requests.request("GET", repo_base_url, headers=headers, data=payload)
    repo_data = []
    for item in response.json():
        # item的值包含remote时，key的值拼接key+'-cache'
        if 'remote' in item['key']:
            repo_data.append(item['key'] + '-cache')
        else:
            repo_data.append(item['key'])
    return repo_data


# 获取一天下载量
def get_today_download_count(repo_name, day):
    repo_name = repo_name

    payload = "items.find({{\r\n    \"repo\":{{\"$eq\":\"{}\"}},\r\n\t\"$and\":[{{\"stat.downloaded\":{{\"$gt\" : \"{}T00:00:00.00+08:00\"}}}}],\r\n    \"$and\":[{{\"stat.downloaded\":{{\"$lte\": \"{}T23:59:59.00+08:00\"}}}}]\r\n}}).include(\"name\", \"repo\", \"stat.downloaded\")".format(repo_name, day, day)

    response = requests.request("POST", aql_url, headers=headers, data=payload)
    num = response.json()['range']['total']
    return repo_name, num, day


# 获取所有仓库下载量
@decorator
def get_data(day):
    for i in tqdm(get_all_repo_name()):
        list_data.append(get_today_download_count(i, day))


if __name__ == '__main__':
    list_data = []
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    print("昨日日期:{}".format(yesterday))
    log_dir = "/home/gaolei/schedule_task/get_depend_daily_download_count"
    get_data(yesterday)
    with open('{}/result-{}.txt'.format(log_dir, yesterday), 'w') as f:
        f.write(str(list_data))