from flask import (
    Flask, 
    render_template, 
    request, 
    jsonify, 
    flash, 
    redirect, 
    url_for,
    session,
    make_response
)
import threading
import signal
import webbrowser
import os
import sys
import pandas as pd

from data_processing import process_values, validate_values


if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(__file__)

template_dir = os.path.join(base_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_data', methods=['POST'])
def process_data():
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']

    if validate_values(input1, input2, input3):
        flash('Всі поля повинні містити числа.')
        return redirect(url_for('index'))
    df = process_values(input1, input2, input3)

    session['df'] = df.to_json()
    df_records = df.to_dict('records')

    return render_template('result.html', records=df_records)


@app.route('/download_csv')
def download_csv():
    df_json = session.get('df')
    if df_json is not None:
        df = pd.read_json(df_json)
        csv_data = df.to_csv(index=False)
        response = make_response(csv_data)
        response.headers['Content-Disposition'] = 'attachment; filename="result.csv"'
        response.headers['Content-Type'] = 'text/csv'
        return response
    else:
        return "Error: No data found", 404


@app.route('/shutdown', methods=['GET'])
def shutdown():
    try:
        os.kill(os.getpid(), signal.SIGINT)
        return jsonify({'message': 'Server is shutting down...'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(port=5000, debug=False)
