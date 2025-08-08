from flask import Flask, jsonify, render_template, request
import csv
import io
import os



app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'titanic.csv')


def parse_csv(stream):
    reader = csv.DictReader(stream)
    return [row for row in reader]


@app.route('/api/sample')
def sample():
    with open(DATA_PATH, newline='', encoding='utf-8') as f:
        return jsonify(parse_csv(f))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    stream = io.StringIO(file.stream.read().decode('utf-8'))
    return jsonify(parse_csv(stream))


if __name__ == '__main__':
    app.run(debug=True)

