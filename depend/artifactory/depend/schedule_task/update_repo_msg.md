# 批量更新maven仓库的排除目录
## 1. 程序介绍
### 1.1 修改点
```
1.update_Patter方法中excludesPattern值修改为你需要配置的目录
2.http_handler中的__init__初始化方法中Authorization值修改为你的认证apikey，可由postman生成
```
### 1.2 使用方法
```
1.执行artifactory\depend\schedule_task\update_repo_msg.py
2.查看执行过程打印的日志
3.备份文件会备份artifactory-日期.txt文件保存上次仓库配置
```