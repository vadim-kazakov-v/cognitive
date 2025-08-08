from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'biases.json')

def load_biases():
    with open(DATA_PATH) as f:
        return json.load(f)

@app.route('/api/biases')
def biases():
    return jsonify(load_biases())

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
