""" Flask Web Application - CI/CD Demo v2.0 """
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

STUDENT_ID = "2440666125"
STUDENT_NAME = "Laishisheng"
APP_VERSION = "2.0"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Demo v2.0 - Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #ff6b6b 0%, #feca57 50%, #48dbfb 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
        }
        .card {
            background: #fff;
            border-radius: 20px;
            padding: 48px 40px;
            max-width: 560px;
            width: 90%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        .badge {
            display: inline-block;
            background: linear-gradient(135deg, #ff6b6b, #feca57);
            color: #fff;
            padding: 6px 20px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 16px;
        }
        h1 { color: #333; font-size: 28px; margin-bottom: 20px; }
        .student { color: #ff6b6b; font-size: 16px; font-weight: bold; margin-bottom: 16px; padding: 10px 20px; background: linear-gradient(135deg, #ffe6e6, #fff5e6); border-radius: 10px; display: inline-block; }
        .version { color: #48dbfb; font-size: 14px; font-weight: bold; margin-bottom: 24px; }
        .status { display: inline-block; background: #e8f5e9; color: #2e7d32; padding: 8px 20px; border-radius: 20px; font-size: 14px; margin-bottom: 24px; font-weight: bold; }
        .info { background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 12px; padding: 20px; text-align: left; font-size: 13px; color: #555; line-height: 2; }
        .info span { color: #333; font-weight: bold; }
        .features { margin-top: 20px; display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }
        .feature-tag { background: #48dbfb; color: #fff; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: bold; }
        .feature-tag.new { background: #ff6b6b; }
    </style>
</head>
<body>
    <div class="card">
        <p class="badge">CI/CD Auto Deploy Success!</p>
        <h1>CI/CD Experiment Demo</h1>
        <p class="student">Student ID: {{ student_id }} | Name: {{ student_name }}</p>
        <p class="version">Flask App v{{ version }} | Python {{ python_version }}</p>
        <div class="status">Service Running OK</div>
        <div class="info">
            <p><span>Hostname:</span> {{ hostname }}</p>
            <p><span>Deploy Time:</span> {{ deploy_time }}</p>
            <p><span>Environment:</span> {{ environment }}</p>
            <p><span>CI/CD:</span> GitHub Actions Auto Build + Test + Deploy</p>
        </div>
        <div class="features">
            <span class="feature-tag">Flask</span>
            <span class="feature-tag">Docker</span>
            <span class="feature-tag new">v2.0 New</span>
            <span class="feature-tag new">Colorful BG</span>
        </div>
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    import socket
    import platform
    import datetime
    return render_template_string(
        HTML_TEMPLATE,
        student_id=STUDENT_ID,
        student_name=STUDENT_NAME,
        version=APP_VERSION,
        python_version=platform.python_version(),
        hostname=socket.gethostname(),
        deploy_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment="Development"
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200


@app.route("/api/info")
def api_info():
    import socket
    import platform
    import datetime
    return jsonify({
        "app_name": "simple-web-cicd",
        "version": APP_VERSION,
        "student_id": STUDENT_ID,
        "student_name": STUDENT_NAME,
        "python_version": platform.python_version(),
        "hostname": socket.gethostname(),
        "deploy_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
