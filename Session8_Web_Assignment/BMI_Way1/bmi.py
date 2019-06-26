from flask import Flask

app = Flask(__name__)

@app.route("/bmi/<int:x>/<int:y>")
def bmi(x,y):
    result = x/(y*y/10000)
    if result < 16:
        condition = "Severely underweight"
    elif result < 18.5:
        condition = "Underweight"
    elif result < 25:
        condition = "Normal"
    elif result < 30:
        condition = "Overweight"
    else:
        condition = "Obese"
       
    return " Your BMI = {0}. Your condition is {1}".format(result,condition) 


if __name__ == "__main__":
    app.run(debug = True) 