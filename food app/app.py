from flask import Flask , render_template

app = Flask(__name__)

all_foods = [
    {
        "title": "Bun dau",
        "description": "Delicious",
        "type": "food",
        "link": "https://andemdanang.com/wp-content/uploads/2018/09/b%C3%BAn-%C4%91%E1%BA%ADu-m%E1%BA%AFm-t%C3%B4m-%C4%91n.jpg"    
    },
    {
        "title": "Rau xao",
        "description": "Familiar",
        "type": "food",
        "link": "http://sotaynauan.com/wp-content/uploads/2013/04/Rau-bi-xao-toi-Sotaynauan.com-5.jpg"    
    },
    {
        "title": "Com chien",
        "description": "Cheap",
        "type": "drink",
        "link": "https://kenh14cdn.com/2017/comchien-1490353048077.jpg"    
    }
]

@app.route("/foods")
def home():  
    return render_template("all_food.html",ALL_FOODS = all_foods)

@app.route("/foods/<int:index>")
def food_detail(index):
    food = all_foods[index]
    return render_template("food_detail.html", FOOD = food)

if __name__ == "__main__":
    app.run(debug = True)