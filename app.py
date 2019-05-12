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
    allphone = mobile_collection.find()
    print(detail_mobile)
    return render_template('single.html',detail_mobile=detail_mobile,allphone=allphone)

@app.route('/products/filter/<type>')
def detail8(type):
    phone_list =[]
    filter_phone = mobile_collection.find()
    for phone in filter_phone:
        if type in phone['detail8']:
            phone_list.append(phone)
            print(phone)
    return render_template('filter.html',phone_list=phone_list)
@app.route('/contact')
def contact():
    return render_template('infor.html')
    
    
if __name__ == '__main__':
 app.run(debug=True)
 