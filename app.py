from flask import Flask, make_response, jsonify
from model import db
app = Flask(__name__)


@app.route('/hello')
def abcd():  # put application's code here
    return 'Hello worldddddd!'
@app.route('/api/products',methods = ['GET'])
def getAllProducts():  # put application's code here
    return make_response(jsonify({"products": db}), 200)


if __name__ == '_main_':
    app.run()