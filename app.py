""" Flask Web Application - CI/CD Demo v1.0 """
from flask import Flask, render_template_string

app = Flask(__name__)

STUDENT_ID = "2440666125"
STUDENT_NAME = "赖石生"
APP_VERSION = "1.0"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Demo - Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
        }
        .card {
            background: #fff;
            border-radius: 16px;
            padding: 40px;
            max-width: 500px;
            width: 90%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        h1 { color: #333; font-size: 28px; margin-bottom: 20px; }
        .student { color: #667eea; font-size: 16px; font-weight: bold; margin-bottom: 16px; padding: 10px; background: #eef0ff; border-radius: 8px; }
        .version { color: #764ba2; font-size: 14px; font-weight: bold; margin-bottom: 20px; }
        .status { display: inline-block; background: #e8f5e9; color: #2e7d32; padding: 6px 16px; border-radius: 20px; font-size: 14px; margin-bottom: 20px; }
        .info { background: #f5f5f5; border-radius: 8px; padding: 16px; text-align: left; font-size: 13px; color: #666; line-height: 1.8; }
        .info span { color: #333; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h1>CI/CD Deployment Success!</h1>
        <p class="student">Student ID: {{ student_id }} | Name: {{ student_name }}</p>
        <p class="version">Flask App v{{ version }} | Python {{ python_version }}</p>
        <div class="status">Service Running OK</div>
        <div class="info">
            <p><span>Hostname:</span> {{ hostname }}</p>
            <p><span>Deploy Time:</span> {{ deploy_time }}</p>
            <p><span>Environment:</span> {{ environment }}</p>
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
    return {"status": "healthy", "version": APP_VERSION}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
