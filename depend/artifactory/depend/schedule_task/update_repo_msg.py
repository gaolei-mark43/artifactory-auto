import time
import requests
import json

# artifactory名称
artifactory_name = "depend.artifactory.com"
# artifactory-base_url
base_url = "https://depend.artifactory.com/artifactory/api/repositories"


# 装饰器-计算函数运行时间
def get_run_time(func_name):
    def wrapper(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            run_time = end_time - start_time
            print("方法:{} 运行时间为：{}".format(func_name, run_time))
            return result
        return inner
    return wrapper


# 封装http请求
class http_handler:
    # 定义http请求头
    def __init__(self):
        self.headers = {
            'Authorization': 'Basic XXXXXXXXXXXXX'}

    # 定义http-GET请求
    def http_get_handler(self, url):
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data=payload)
        return response

    # 定义http-POST请求
    def http_post_handler(self, url, headers, payload):

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

        return response.status_code


# 获取mvn-repo库代理maven本地仓库
@get_run_time("获取mvn-repo本地仓库的名称")
def get_mvn_repo():
    url = base_url + "/mvn-repo"
    response = http_handler.http_get_handler(url)
    json_data = response.json()
    data = []
    for project_name in json_data['repositories']:
        data.append(project_name)
    new_list = [item for item in data if "remote" not in item and "mvn-3rd-private" not in item and "3rdParty" not in item and "thirdparty" not in item and "temp" not in item]
    print("获取到{}本地仓库数量:{}".format(artifactory_name, len(new_list)))
    print("获取到{}本地仓库名称:".format(artifactory_name), *new_list, sep='\n')
    return new_list


# 备份txt
@get_run_time("备份函数")
def json2txt(json_data):
    print("备份开始-START")
    file_name = "artifactory-" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".txt"
    with open("{}".format(file_name), "w", encoding="utf-8") as f:
        f.write(str(json_data))
    print("备份完成-END")
    print("备份文件:{}".format(file_name))


# 更新配置
def update_Pattern(repo_name):
    url = base_url + "/" + repo_name
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic XXXXXXXXXXXXX'
    }
    payload = json.dumps(
        {
            "key": "{}".format(repo_name),
            "excludesPattern": "com/fasterxml/**,com/alibaba/**,com/amazonaws/**,com/couchbase/**,com/google/**,com/h2database/**,com/hazelcast/**,com/netflix/**,com/oracle/**,com/redislabs/**,com/twitter/**,com/zaxxer/**,com/atlassian/**,com/cloudera/**,com/dropbox/**,com/elastic/**,com/etsy/**,com/facebookresearch/**,com/goldmansachs/**,com/linkedin/**,com/mozilla/**,com/pivotal/**,com/redhat/**,com/salesforce/**,com/symantec/**,com/yahoo/**,com/yelp/**,com/android/**,com/squareup/**,com/sun/**,io/**,jakarta/**,junit/**,net/**,org/**,androidx/**,app/**,commons-beanutils/**,commons-io/**,commons-logging/**"
        }
    )
    # 加入睡眠3s
    time.sleep(3)
    response = http_handler.http_post_handler(url, headers, payload)
    # response = 200
    if response == 200:
        print("修改{}配置成功".format(repo_name))
    else:
        print("修改{}配置失败".format(repo_name))


# 获取单个仓库的信息
def get_repo_msg(repo_name):
    url = base_url + "/" + repo_name
    response = http_handler.http_get_handler(url)
    json_data = response.json()
    return json_data


# 主函数
if __name__ == '__main__':
    http_handler = http_handler()
    new_list = get_mvn_repo()
    list_data = []
    for i in new_list:
        list_data.append(get_repo_msg(i))
    json2txt(list_data)

    for i in new_list:
        update_Pattern(i)

