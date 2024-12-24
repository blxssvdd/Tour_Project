from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/tour/")
def tour():
    return render_template("tour.html")


@app.get("/departure/")
def departure():
    return render_template("departure.html")


if __name__ =="__main__":
    app.run(debug=True)