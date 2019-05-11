from flask import Flask, render_template
from models.database import mobile_collection
from bson.objectid import ObjectId
app = Flask(__name__)


@app.route('/')
def index():
    allphone = mobile_collection.find()
    return render_template('index.html',allphone = allphone)

@app.route('/products')
def products():
    allphone = mobile_collection.find()
    return render_template('products.html',allphone = allphone)

@app.route('/products/single/<id>')
def single(id):
    detail_mobile = mobile_collection.find_one({"_id" : ObjectId(id)})
    return render_template('single.html',detail_mobile=detail_mobile)
    
if __name__ == '__main__':
 app.run(debug=True)
 