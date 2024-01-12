# 使用artifatory-aql接口查询两个库的所有zip，对比结果

import requests

depend_url = "https://depend.artifactory.com/artifactory/api/search/aql"
artifacts_url = "https://artifacts.artifactory.com/artifactory/api/search/aql"
payload = "items.find({\"repo\":{\"$eq\":\"cocoapods-private\"}, \r\n\"name\":{\"$match\":\"*.json\"}, \"type\":\"file\"}).include(\"name\",\"path\",\"actual_md5\")"


# 获取老私服的josn文件信息
def get_artifacts_zip_file():
    headers = {
        'Content-Type': 'text/plain',
        'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXXXXXXXX'
    }
    response = requests.request("POST", artifacts_url, headers=headers, data=payload)
    result = response.json()
    # print(response.text)
    return result


# 获取新私服的json文件信息
def get_depend_zip_file():
    headers = {
        'Content-Type': 'text/plain',
        'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXXXXXXXX'
    }
    response = requests.request("POST", depend_url, headers=headers, data=payload)
    result = response.json()
    return result


# 对比两个库的zip文件
def compare_zip_file(list_data1, list_data2):
    diff1 = [x for x in list_data1 if x not in list_data2]
    diff2 = [x for x in list_data2 if x not in list_data1]
    return diff1, diff2


if __name__ == '__main__':
    count = 0
    depend_zip_data = []
    for i in get_depend_zip_file()['results']:
        count += 1
        depend_zip_data.append(i['path'] + "/" + i['name'] + " " + i['actual_md5'])
    print("depends总数为：" + str(count))

    artifacts_zip_data = []
    for i in get_artifacts_zip_file()['results']:
        artifacts_zip_data.append(i['path'] + "/" + i['name'] + " " + i['actual_md5'])
    print("artifacts总数为：" + str(len(artifacts_zip_data)))

    diff1, diff2 = compare_zip_file(depend_zip_data, artifacts_zip_data)
    print("-"*100)
    dist = []
    # 输出两个库的差异，list转为str切割保留文件名
    for i in diff1:
        print(i.split(" ")[0])
        dist.append(i.split(" ")[0])
    print("-"*100)

