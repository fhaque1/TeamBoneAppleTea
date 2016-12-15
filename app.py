from flask import Flask, render_template, request
from utils import map

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("map.html", url = "https://plot.ly/~fhaque1/14.embed?autosize=True&link=false&modebar=false")

@app.route("/<path:censusURL>")
def renderFilteredData(censusURL):
	censusURL = censusURL.split('$')
	map.mapMaker(censusURL[1],censusURL[0])
	return render_template("map.html", url = "https://plot.ly/~fhaque1/26.embed?autosize=True&link=false&modebar=false")

if __name__ == '__main__':
    app.debug = True
    app.run()
