from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/depend')
def show_remote_repositories():
    payload = {}
    headers = {
      'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    }
    response = requests.get('https://depend.artifactory.com/artifactory/api/repositories?type=remote', headers=headers, data=payload)

    repositories = response.json()
    headers = []
    rows = []
    for repository in repositories:
        headers.append(repository['key'])
        rows.append(repository)
    return render_template('repositories.html', headers=headers, rows=rows)


@app.route('/aliyun')
def show_remote_repositories1():
    payload = {}
    headers = {
        'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=='
    }
    response = requests.get('http://47.96.180.139:8081/artifactory/api/repositories?type=remote', headers=headers, data=payload)

    repositories = response.json()
    headers = []
    rows = []
    for repository in repositories:
        headers.append(repository['key'])
        rows.append(repository)
    return render_template('repositories.html', headers=headers, rows=rows)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

