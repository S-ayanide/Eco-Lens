from flask import Flask, jsonify
import pickle
app = Flask(__name__)


@app.route('/products', methods=['GET', 'POST'])
def get_products():

    # GET request
    return jsonify({'test': "Product"})
