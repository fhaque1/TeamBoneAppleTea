from flask import Flask, render_template, request
from utils import map

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("map.html", url = "https://plot.ly/~fhaque1/14.embed")

@app.route("/pop5")
def population5():
    return render_template("map.html", url = "https://plot.ly/~fhaque1/10.embed")

@app.route("/<path:censusURL>")
def renderFilteredData(censusURL):
    map.mapMaker(censusURL)

if __name__ == '__main__':
    app.debug = True
    app.run()
