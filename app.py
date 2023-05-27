from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def form_page():
    if request.method == 'POST':
        # Xử lý dữ liệu được gửi từ form
        query = request.form['query']
        if(query=="hi"):
            return render_template('/result/true.html')
        
        else:
            return render_template('/result/false.html')
        
        
        # Thực hiện các xử lý khác...
    # Trang hiển thị form
    return render_template('/check/index.html')
