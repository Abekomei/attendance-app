from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# 部屋番号データ
ROOM_DATA = {
    "3212": "https://example.com/attendance/3212",
    "7103": "https://example.com/attendance/7103",
}

# スマホ画面の見た目（HTML）
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>爆速出席ツール</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 50px; background: #f4f4f9; }
        input { width: 80%; padding: 15px; font-size: 20px; border-radius: 10px; border: 1px solid #ccc; }
        button { width: 85%; padding: 15px; margin-top: 20px; font-size: 20px; background: #007bff; color: white; border: none; border-radius: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <h2>部屋番号を入力</h2>
    <form action="/open" method="post">
        <input type="number" name="room" placeholder="例: 3212" required>
        <button type="submit">出席サイトを開く</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/open', methods=['POST'])
def open_url():
    room = request.form.get('room')
    if room in ROOM_DATA:
        return redirect(ROOM_DATA[room])
    return "<h1>エラー：その部屋番号は登録されていません</h1><a href='/'>戻る</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # 0.0.0.0にすると同じWi-Fi内のスマホから見れる！