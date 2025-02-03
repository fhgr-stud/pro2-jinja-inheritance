from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    langer_text = """
lakdsfkjahsdfkjha sdas
df adsf a
sdf 
asdf asdfas dfkjashdfkjahsdkjfhasdf

asd flkjahsdfkj hasjkdhfk asdf

asdfljk asdkjfh kjasdhfk asdf
kajsdhf kjahsdkjf asdf
"""
    return render_template('index.html', langer_text=langer_text)

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/produkte')
def produkte():
    return render_template('produkte.html')

@app.route('/ueberuns')
def ueberuns():
    return render_template('ueberuns.html')


app.run(debug=True, port=5001)