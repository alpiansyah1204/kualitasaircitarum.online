from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lat = request.form['lat']
        lng = request.form['lng']
        return render_template('index.html', lat=lat, lng=lng)
    return render_template('index.html')
