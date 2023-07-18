from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = 'mink'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        csv_file = request.files['csv_file']

        # Read the CSV file
        data = pd.read_csv(csv_file, header=None, names=['action', 'state', 'reward'])

        # Save the data to a file instead of the session
        data.to_csv('data.csv')

        # Redirect to the results page
        return redirect(url_for('results'))
    return render_template('upload.html')

@app.route('/results', methods=['GET'])
def results():
    # Load the data from the file
    if os.path.exists('data.csv'):
        data = pd.read_csv('data.csv')
        # Convert DataFrame to JSON
        data = data.to_json(orient='records')
    else:
        data = pd.DataFrame()

    return render_template('results.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
