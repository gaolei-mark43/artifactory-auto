# 获取私服每日下载量
## 1. 程序介绍
### 1.1 修改点
```
1.headers公共参数中Authorization值修改为你的认证apikey，可由postman生成
```
### 1.2 使用方法
```
1.登录主机172.31.65.60
2.crontab -l查看定时任务 1 0 * * * python /home/gaolei/schedule_task/get_depend_daily_download_count/get_depend_daily_download_count.py >> /home/gaolei/schedule_task/get_depend_daily_download_count/log/get_data.log
3./home/gaolei/schedule_task/get_depend_daily_download_count每日凌晨0点1分输出result+日期文件保存昨天下载量数据
4.log文件夹下保存日志
```