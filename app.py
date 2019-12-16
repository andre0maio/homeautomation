from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gate")
def gate():
    return render_template('gate.html')

@app.route("/lights")
def lights():
    return render_template('lights.html')

@app.route("/temp")
def temp():
    return render_template('temp.html')


if __name__ == '__main__':
    app.run(debug=True)
