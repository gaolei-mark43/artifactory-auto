import os


# 计算目录下的json文件数量用
def count_json_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                count += 1
    return count


# 指定目录路径
directory_path = 'static3'

# 调用函数计算JSON文件数量
json_file_count = count_json_files(directory_path)

# 打印结果
print(f"目录 '{directory_path}' 下的JSON文件数量为: {json_file_count}")
