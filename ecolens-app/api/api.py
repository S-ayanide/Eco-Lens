from flask import Flask
import time
import pickle
app = Flask(__name__)

@app.route('/time', methods=['GET', 'POST'])
def get_time():
    
    # GET request    
    return {'time': time.time()}        
    