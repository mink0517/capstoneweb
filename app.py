from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_input', methods=['POST'])
def save_input():
    input_data = request.form.to_dict()

    with open('input_data.json', 'w') as file:
        json.dump(input_data, file)

    return 'Input data saved.'

if __name__ == '__main__':
    app.run(debug=True)

