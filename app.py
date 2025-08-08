from flask import Flask, jsonify, render_template, request
import json
import os
import csv
import io


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

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    stream = io.StringIO(file.stream.read().decode('utf-8'))
    reader = csv.DictReader(stream)
    data = [row for row in reader]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
