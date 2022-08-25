

from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import Info
# Khởi tạo Flask Server Backend
app = Flask(__name__)

# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/add', methods=['POST', 'GET'] )
@cross_origin(origin='*')
def add_process():
    return "Hàm cộng" 

@app.route('/', methods=['POST', 'GET'] )
def home():
    return "Home Page" 


@app.route('/info', methods = ["GET","POST"] )
def infomation():
    
    a = {"name":Info.random_name(),"fulname":Info.random_full_name(0),"username":Info.random_username_name(0),'phone':Info.random_phone()}
    return a


# Start Backend
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port='8888',debug = True)
    app.run(port='7777')
