from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb+srv://admin:admin@cluster0-d3to1.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri) 

mobiledata = client.db_mobile

mobile_collection = mobiledata["my_data_mobile"]

new_mobiles = {
        "name" : "Apple iPad 9.7 2018 (4G - Wi-Fi) 32GB",
        "price" : "10.500.000 ₫",
        "detail1" : "Màn hình : LED-backlit IPS LCD, 9.7 inches, 1536 x 2048 pixels" ,
        "detail2" : "Hệ điều hành IOS 11" ,
        "detail3" : "RAM 2GB" ,
        "detail4" : "Loại Sim Nano SIM" ,
        "detail5" : "Chip đồ họa (GPU) PowerVR Series7XT Plus (6 lõi đồ họa)" ,
        "detail6" : "Loại CPU (Chipset) Apple A10 Fusion APL1W24" ,
        "detail7" : "Camera : Camera trước 1.2MP , Camera sau 8MP" ,
        
    }

