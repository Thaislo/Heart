from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Chạy ở chế độ debug để dễ dàng chỉnh sửa
    app.run(debug=True)
