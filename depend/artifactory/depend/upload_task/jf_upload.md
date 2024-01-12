# depedn-artifactory迁移NPM库
## 1. 程序介绍
### 1.1 修改点
```
1.dir_list中的dir_list变量修改为你需要迁移的文件目录列表
```
### 1.2 使用方法
```
1.查看wiki:http://wiki.artifactory.com/pages/viewpage.action?pageId=506073788 去用户机器上安装python以及artifactory-cli工具
2.执行此py即可
3.过程日志会输出，查看日志即可查看本次迁移结果，绕过发生报错，会打印出报错日志文件，去查看报错日志文件定位迁移失败原因
```