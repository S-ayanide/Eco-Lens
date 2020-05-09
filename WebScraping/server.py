from flask import Flask, jsonify, request, render_template
import pickle
app = Flask(__name__)

@app.route('/')
def starting():
    return "Server is up and running"

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

if __name__ == '__main__':

    with open('data','rb') as item_data:
        results = pickle.load(item_data)
        print(results)

    app.debug = True
    app.run(host = '127.0.0.1', port = 8000)