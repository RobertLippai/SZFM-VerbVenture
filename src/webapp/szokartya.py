from flask import Flask, render_template

app = Flask(__name__)

@app.route('/word_cards')
def index():
    words = ["dog", "you", "did", "yes", "but", "never", "far", "apple"]
    return render_template('szokartya.html', words=words)

if __name__ == '__main__':
    app.run(debug=True)