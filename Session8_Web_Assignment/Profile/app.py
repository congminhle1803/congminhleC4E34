from flask import Flask, render_template, redirect

app = Flask(__name__)

profile = {
    "name" : "Minh Le",
    "work" : "Officer",
    "school" : "FTU",
    "hobbies" : "Basketball",
    "crush" : "404 Not found"
}

@app.route("/about-me")
def about_me():
    return render_template("about_me.html", PROFILE = profile)

@app.route("/school")
def school():
    return redirect("http://techkids.vn")


if __name__ == "__main__":
    app.run(debug = True)

