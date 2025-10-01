from flask import Flask

app = Flask(__name__)

@app.route('/output')
def greetings():
    return "I love Flask web development using Python! - Josh Subido"

if __name__ == '__main__':
    app.run(debug=True)