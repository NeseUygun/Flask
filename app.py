from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/path', methods=['POST'])
def operation():
    if request.method == 'POST':
        firstname = request.json["firstname"]
        lastname = request.json["lastname"]
        result = f" My full name is {firstname} {lastname}"
    return jsonify(result)

#this is for postman
@app.route('/via_postman_math', methods=['POST'])
def math_number():
    if request.method == 'POST':
        operation = request.json["operations"]
        number1=request.json["number1"]
        number2=request.json["number2"]
        if operation == "add":
            result = f"Total of two number is {number1+number2}"
        elif operation == "subtract":
            result = f"Subtraction of two number is {number1-number2}"
        elif operation == "multiply":
            result = f"Multiplication of two number is {number1*number2}"
        else:
            result = f"Divition of two number is {number1/number2}"

    return jsonify(result)

# this is for webpage
@app.route('/math', methods=['POST'])
def math_operation():
    if request.method == 'POST':
        operation = request.form["operation"]
        number1=int(request.form["number1"])
        number2=int(request.form["number2"])
        if operation == "add":
            result = f"Total of two number is {number1+number2}"
        elif operation == "subtract":
            result = f"Subtraction of two number is {number1-number2}"
        elif operation == "multiply":
            result = f"Multiplication of two number is {number1*number2}"
        else:
            result = f"Divition of two number is {number1/number2}"

    return render_template("results.html", result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)