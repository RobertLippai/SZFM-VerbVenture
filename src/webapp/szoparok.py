from flask import Flask, render_template

app = Flask(__name__)


@app.route('/wordspair')
def index():
    leftWords = ["kutya", "láb", "betű", "háború", "víz", "ló", "állat", "igazság"]
    rightWords = ["dog", "leg", "word", "war", "water", "horse", "animal", "truth"]

    return render_template('szoparosit.html', leftWords=leftWords, rightWords=rightWords)


if __name__ == '__main__':
    app.run(debug=True)
