import requests
import json
import os
import traceback


# 获取所有JSON文件
def get_all_json_files():
    url = "https://depend.artifactory.com/artifactory/api/search/aql"
    payload = "items.find({\"repo\":{\"$eq\":\"cocoapods-luck-private\"}, \r\n\"name\":{\"$match\":\"*.json\"}, \"type\":\"file\"})"
    headers = {
        'Content-Type': 'text/plain',
        'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXXXXXXXX'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    return data['results']


# 下载JSON文件
def download_json_file(path):
    url = "https://depend.artifactory.com/artifactory/cocoapods-luck-private/"+path
    payload = {}
    headers = {
        'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXXXXXXXX'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    local_path = "static"+"/"+path
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"文件已成功下载到本地：{local_path}")
    else:
        print("下载文件时发生错误")


# 修改本地json文件内容
def update_json_files1(folder_path, old_string, new_string):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                    # 替换字符串
                    if old_string in content:
                        updated_content = content.replace(old_string, new_string)
                    else:
                        print("字符串不包括:"+old_string)
                        continue

                    with open(file_path, 'w') as updated_file:
                        updated_file.write(updated_content)

                    print(f"Updated file: {file_path}")
                except Exception as e:
                    print(f"Error: Failed to update file {file_path}")
                    print(str(e))


# 校验修改结果
def validate_json_files(folder_path, old_string):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r') as file:
                        json_data = file.read()
                    # 校验字符串
                    if old_string in json_data:
                        print("字符串包括:"+old_string+"，校验失败")
                        return False
                    else:
                        print("字符串不包括:"+old_string+"，校验成功")
                except (ValueError, json.JSONDecodeError) as e:
                    print(f"Error: Failed to update file {file_path}")
                    traceback.print_exc()
                    return False
    return True


# 获取修改后JSON文件
def get_json_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)
                print(file_path)
                upload_json_file(file_path)


# 上传JSON文件
def upload_json_file(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
    url = "https://depend.artifactory.com/artifactory/cocoapods-luck-private/"+file_path.replace("static3\\", "").replace("\\", "/")
    print(url)
    payload = file_content
    print(payload)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXXXXXXXX'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    if response.status_code == 201:
        # print(response.status_code, response.text)
        print(f"文件已成功上传到服务器：{file_path}")
    else:
        # print(response.status_code, response.text)
        print("上传文件时发生错误"+"\n"+response.text)


if __name__ == '__main__':
    # 执行迁移操作
    data = get_all_json_files()
    for item in data:
        print("开始下载"+item['path']+"/"+item['name'])
        download_json_file(item['path']+"/"+item['name'])
        print("下载完成")

    # 替换最常规的字符
    # update_json_files1("static3", "https://artifacts.artifactory.com/cocoapods-private/", "https://depend.artifactory.com/artifactory/cocoapods-luck-private/")

    # 替换剩余的非常规的字符
    # update_json_files1("static3", "https://artifacts.artifactory.com//cocoapods-private/", "https://depend.artifactory.com/artifactory/cocoapods-luck-private/")

    # if validate_json_files("static3", "https://artifacts.artifactory.com"):
    #     print("校验失败")
    # folder_path = "static3"
    # get_json_files(folder_path)

