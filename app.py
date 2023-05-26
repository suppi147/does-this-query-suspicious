from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def form_page():
    if request.method == 'POST':
        # Xử lý dữ liệu được gửi từ form
        query = request.form['query']
        
        # Thực hiện các xử lý khác...
        return 'Dữ liệu đã được gửi thành công!'
    # Trang hiển thị form
    return render_template('form.html')
