from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Artifactory API endpoint
ARTIFACTORY_API = "http://47.96.180.139:8081/artifactory/api/storage/"
payload = {}
headers = {
    'Authorization': 'Basic XXXXXXXXXXXXXXXXXXXX=='
}


@app.route("/")
def index():
    # Retrieve query parameters from request
    repo_key = request.args.get("repo_key", "mvn-repo")
    start_date = request.args.get("start_date", "2023-03-01")
    end_date = request.args.get("end_date", "2023-03-22")

    # Call Artifactory API to retrieve repository stats
    url = ARTIFACTORY_API + repo_key + "?stats&statsStartDate=" + start_date + "&statsEndDate=" + end_date
    response = requests.get(url, headers=headers, data=payload)
    if response.status_code != 200:
        return "Error retrieving repository stats"

    # Parse response JSON to extract download stats
    download_stats = []
    stats = response.json().get("children", [])
    for stat in stats:
        download_count = stat.get("downloadCount", 0)
        download_date = stat.get("uri", "").replace("/", "")
        download_stats.append({"date": download_date, "count": download_count})

    # Render template with repository stats and query parameters
    return render_template("index.html", repo_key=repo_key, start_date=start_date, end_date=end_date, download_stats=download_stats)


if __name__ == '__main__':
    app.run()