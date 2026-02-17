#import the flas framework
from flask import *


#Below we create a web server based application
app = Flask(__name__)

#Below we create the home rout.
#Routing : This is mapping /connecting didfferent resources to different functions.We do this by the help of a decarotor.
@app.route("/api/home")
def home():
    return jsonify({"message": "Home Route accessed"})

#Below is the products route
@app.route("/api/products")
def products():
    return jsonify({"message" : "Welcome to the products route"})

#Below is a route for addition
@app.route("/api/calc" , methods=["POST"])
def calculator():
    if request.method == "POST":
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        sum = int(number1) + int(number2)

        return jsonify({"The answer is ": sum})
    
# create a route that is able to calculate the simple interest given the pricipal as 20000, rate as 7% and time as 8 years.

@app.route('/calculate-interest', methods=['POST'])
def calculate_interest():
    # Extracts the JSON data from the Postman request body
    data = request.get_json()
    
    # Extract values with provided defaults
    p = float(data.get('principal', 20000))
    r = float(data.get('rate', 7)) / 100
    t = float(data.get('time', 8))
    
    interest = p * r * t
    total = p + interest
    
    return jsonify({
        "principal": p,
        "rate_percentage": r * 100,
        "time_years": t,
        "simple_interest": interest,
        "total_amount": total
    })

if __name__ == '__main__':
    app.run(debug=True)


#Below we run the application
app.run(debug=True)