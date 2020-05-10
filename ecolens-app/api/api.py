from flask import Flask
import time
import pickle
app = Flask(__name__)

@app.route('/time', methods=['GET', 'POST'])
def get_time():
    
    # GET request    
    return {'time': time.time()}        

# if __name__ == '__main__':

#     with open('../Data/homescreen_data','rb') as item_data:
#         results = pickle.load(item_data)
#         print(results)
    