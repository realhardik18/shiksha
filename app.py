from flask import Flask, render_template, request,redirect
from threading import Thread

app = Flask('')
app.debug=True

@app.route('/')
def home():
    return render_template("index.html")

def run():
    app.run(host='0.0.0.0')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form['topic']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

def show_site():
    t = Thread(target=run)
    t.start()


run()

