from flask import Flask, render_template, request
from utils.map import urlparser

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("map.html", url = "https://plot.ly/~fhaque1/14.embed")

@app.route("/pop5")
def population5():
    return render_template("map.html", url = "https://plot.ly/~fhaque1/10.embed")

@app.route("/<path:censusURL>")
def renderFilteredData(censusURL):
    print urlparser(censusURL)

if __name__ == '__main__':
    app.debug = True
    app.run()
