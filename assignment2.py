#import the flas framework
from flask import *
import os

#import pymysql module - It helps to create a connection between python flask and mysql database
import pymysql

#Below we create a web server based application
app = Flask(__name__)

#configure the location to where your products images will be saved on you app
app.config["UPLOAD_FOLDER"] ="static/images"


#create an add route
@app.route("/api/add_activewear", methods=["POST"])
# introduce a function
def add_activewear():
     if request.method=="POST":
        #extract the data entered from the phone
        name = request.form["name"]
        brand=request.form["brand"]
        size =request.form["size"]
        color =request.form["color"]
        gender =request.form["gender"]
        price = request.form["price"]
        stock =request.form["stock"]
        # for the product photo ,we shall fetch it from files as showm below
        photo = request.files["photo"]

        #extract the filename of the photo
        filename= photo.filename

         #by use of the OS module ,we can extract the path where the image is currently saved
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"],filename)

        #save the photo image into the new location
        photo.save(photo_path)


        #print them out to test whether you are receiving the details
       # print(product_name,product_description,product_cost) 
        connection =pymysql.connect(host="localhost", user="root",password="", database="online")

        #create a cursor to execute the sql queries
        cursor = connection.cursor()

        # structure an sql to insert the product details in the database 
        # The %s is a placeholder -> it stands in places of actual values
        sql="INSERT INTO active_wear(name, brand, size, color,gender, price, stock,photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        #create a tuple that will hold all the data content from the form
        data=(name, brand, size, color,gender, price, stock,filename )

        # use the cursor to execute the sqls you replace the placeholders with the actual data
        cursor.execute(sql,data)

        #commit the changes to the database
        connection.commit()

     return jsonify({"message":"active wear added successfully"})
   

# Below is the route for fetching active wear items
@app.route("/api/get_activewear")  
def get_activewear():
    #create a connection to db
    connection =pymysql.connect(host="localhost", user="root", password="", database="online")

    #create a cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    #structure the query to fetch all  the products from the table active_wear
    sql="SELECT * FROM active_wear"

    # execute the query
    cursor.execute(sql)

    # create a variable that holds the data fetched from the table
    activewear=cursor.fetchall()


    return jsonify(activewear)










#create an  supplement add route
@app.route("/api/add_fitnesssupplements", methods=["POST"])
# introduce a function
def add_fitnesssupplements():
     if request.method=="POST":
        #extract the data entered from the phone
        name = request.form["name"]
        brand=request.form["brand"]
        dosage =request.form["dosage"]
        expiry =request.form["expiry"]
        price = request.form["price"]
        stock =request.form["stock"]
        # for the product photo ,we shall fetch it from files as showm below
        photo = request.files["photo"]

        #extract the filename of the photo
        filename= photo.filename

         #by use of the OS module ,we can extract the path where the image is currently saved
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"],filename)

        #save the photo image into the new location
        photo.save(photo_path)

        #print them out to test whether you are receiving the details
       # print(product_name,product_description,product_cost) 
        connection =pymysql.connect(host="localhost", user="root",password="", database="online")

        #create a cursor to execute the sql queries
        cursor = connection.cursor()

        # structure an sql to insert the product details in the database 
        # The %s is a placeholder -> it stands in places of actual values
        sql="INSERT INTO fitnesssupplements(name, brand, dosage, expiry, price, stock, photo) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        #create a tuple that will hold all the data content from the form
        data=(name, brand, dosage,expiry ,price, stock,filename)

        # use the cursor to execute the sqls you replace the placeholders with the actual data
        cursor.execute(sql,data)

        #commit the changes to the database
        connection.commit()

     return jsonify({"message":"supplement added successfully"})



# Below is the route for fetching supplements
@app.route("/api/get_fitnesssupplements")  
def get_fitnesssupplements():
    #create a connection to db
    connection =pymysql.connect(host="localhost", user="root", password="", database="online")

    #create a cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    #structure the query to fetch all  the products from the table active_wear
    sql="SELECT * FROM fitnesssupplements"

    # execute the query
    cursor.execute(sql)

    # create a variable that holds the data fetched from the table
    fitnesssuplements=cursor.fetchall()


    return jsonify(fitnesssuplements)



#Below we run the application
app.run(debug=True)

