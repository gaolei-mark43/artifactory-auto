list = ["mvn-remote-maven.google.com",
        "mvn-remote-epository.apache.org",
        "mvn-remote-epository.jboss.org",
        "mvn-remote-maven.geo-solutions.it",
        "mvn-remote-repo.jenkins-ci.org",
        "mvn-remote-repository.apache.org.snapshots",
        "mvn-remote-repo.maven.apache.org",
        "mvn-remote-repo1.maven.org",
        "mvn-remote-dl.bintray.com",
        "mvn-remote-oss_jfrog_org",
        "mvn-remote-nexus.pentaho.org",
        "mvn-remote-repo.osgeo.org",
        "mvn-remote-mvn.mob.com",
        "mvn-remote-maven.aliyun.com",
        "mvn-remote-jcenter.bintray.com",
        "mvn-remote-qxb-proxy",
        "mvn-remote-EBD-interanl-nexus",
        "mvn-remote-mvn.gt.igexin.com",
        "mvn-remote-plugins.gradle.org",
        "mvn-remote-developer.huawei.com.repo",
        "mvn-remote-weimob",
        "mvn-remote-mirrors.huaweicloud.com",
        "mvn-remote-nexus.public",
        "mvn-remote-maven.bytedance.com",
        "mvn-remote-mvn.topobyte.de",
        "mvn-remote-mvn.slimjars.com",
        "mvn-remote-maven.aliyun.com-gradle-plugin",
        "mvn-remote-nexus-app.bokecc.com",
        "mvn-remote-repo.e-iceblue.cn",
        "mvn-remote-jitpack.io", ]

import requests

url = "https://depend.artifactory.com/artifactory/api/repositories/"

payload = {}
headers = {
    'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXXXXXX'
}


def getUrl():
    for i in list:
        response = requests.request("GET", url + i, headers=headers, data=payload)
        re = response.json()
        print(i)
        print(re["url"])


if __name__ == '__main__':
    getUrl()
