from flask import Flask

# 1. Create app/server
app = Flask(__name__)

# 2. Building route
# function binding
@app.route("/") 
def home():
    return "C4E34"

@app.route("/say-hi")
def say_hi():
    return 'Hi everyone'

@app.route("/say-hi/<name>/<age>")
def say_hi_everyone(name,age):
    return "Hi {0}, {1} years old".format(name,age)

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    result = x + y
    return str(result)  # sau return bắt buộc là string

# 3. Run server
if __name__ == "__main__": #Khi dung app co the co nhieu app ao (phuc vu nguoi dung) => Qdinh dau la app chinh
    app.run(debug = True) # Debug = True giu cho app chay ke ca khi thay doi code, ko can tat app di 