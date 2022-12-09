import os
from flask import Flask, render_template,request, flash, send_file, url_for, redirect
from display_image import show
from prediction import predict_caption

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        if "file" not in request.files:
            print("File not uploaded.")
            return
        file = request.files['file']
        image = file.read()
        caption= predict_caption(image)
        uri = show(file)


        return render_template('result.html', uri = uri, caption=caption)


if __name__ == "__main__":
#    app.run(host='127.0.0.1', port=8888)
    #http_server = WSGIServer(('127.0.0.1', 8888), app)
    #http_server.serve_forever()
    app.run()    



