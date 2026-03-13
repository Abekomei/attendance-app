import os
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# 千葉工大の出席システムのベースURL
BASE_URL = "https://attendance.is.it-chiba.ac.jp/attendance/class_room/"

# スマホのホーム画面用アイコン（CITのロゴ画像など、好きな画像のURLに変えてもOK！）
ICON_URL = "https://www.it-chiba.ac.jp/apple-touch-icon.png"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CIT爆速出席</title>
    
    <link rel="apple-touch-icon" href="{{ icon_url }}">
    
    <style>
        body { font-family: -apple-system, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 35px; border-radius: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); width: 85%; max-width: 400px; text-align: center; }
        h2 { color: #333; margin-bottom: 25px; font-size: 1.4rem; font-weight: 800; }
        input { width: 100%; padding: 18px; font-size: 28px; border: 2px solid #eee; border-radius: 15px; box-sizing: border-box; text-align: center; margin-bottom: 25px; background: #fafafa; }
        input:focus { border-color: #007AFF; outline: none; background: #fff; }
        button { width: 100%; padding: 18px; font-size: 18px; font-weight: bold; color: white; background: #007AFF; border: none; border-radius: 15px; cursor: pointer; transition: 0.2s; }
        button:active { transform: scale(0.98); background: #0056b3; }
        .footer { margin-top: 20px; font-size: 12px; color: #bbb; }
    </style>
</head>
<body>
    <div class="card">
        <h2>部屋番号を入力</h2>
        <form action="/open" method="post">
            <input type="number" name="room" inputmode="numeric" pattern="[0-9]*" placeholder="例: 3212" required autofocus>
            <button type="submit">出席サイトへ爆速ジャンプ</button>
        </form>
        <div class="footer">Chiba Institute of Technology</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, icon_url=ICON_URL)

@app.route('/open', methods=['POST'])
def open_url():
    room = request.form.get('room')
    if room:
        # 入力された番号を末尾にくっつけてリダイレクト
        return redirect(f"{BASE_URL}{room}")
    return redirect('/')

if __name__ == '__main__':
    # Renderの環境変数PORTを読み込む（これがないとエラーになる）
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
