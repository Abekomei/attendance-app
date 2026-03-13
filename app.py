import os
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# 千葉工大の出席システムのベースURL
BASE_URL = "https://attendance.is.it-chiba.ac.jp/attendance/class_room/"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>爆速出席ツール</title>
    <style>
        body { font-family: -apple-system, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 85%; max-width: 400px; text-align: center; }
        h2 { color: #333; margin-bottom: 20px; font-size: 1.2rem; }
        input { width: 100%; padding: 15px; font-size: 24px; border: 2px solid #ddd; border-radius: 12px; box-sizing: border-box; text-align: center; margin-bottom: 20px; }
        button { width: 100%; padding: 15px; font-size: 18px; font-weight: bold; color: white; background: #007AFF; border: none; border-radius: 12px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2>部屋番号を入力</h2>
        <form action="/open" method="post">
            <input type="number" name="room" pattern="[0-9]*" inputmode="numeric" placeholder="例: 3212" required autofocus>
            <button type="submit">出席サイトを開く</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/open', methods=['POST'])
def open_url():
    room = request.form.get('room')
    if room:
        return redirect(f"{BASE_URL}{room}")
    return redirect('/')

if __name__ == '__main__':
    # 念のためローカルでも動くように設定
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
