from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4')
def four():
    return render_template('four.html')

@app.route('/<int:x>/<int:y>')
def display(x, y):
    return render_template('display.html', x=x, y=y)


if __name__ == "__main__":
    app.run(debug=True)