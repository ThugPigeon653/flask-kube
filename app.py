from flask import Flask, jsonify
import json

app = Flask(__name__)

# Function to read and return data from JSON file
def read_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

@app.route('/')
def single():
    data = read_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
