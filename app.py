from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('index')

@app.route('/index')
def index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5005)