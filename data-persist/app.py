from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
DATA_FILE = '/data/persistent_data.txt'

@app.route('/')
def index():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = file.readlines()
        last_entries = data[-10:]  # Get the last 10 entries
    else:
        last_entries = ['No data available']
    return render_template('index.html', entries=last_entries)

@app.route('/save', methods=['POST'])
def save():
    new_data = request.form['data']
    with open(DATA_FILE, 'a') as file:
        file.write(new_data + "\n")
    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs('/data', exist_ok=True)
    app.run(host='0.0.0.0', port=5000)

