from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("map.html", url = "https://plot.ly/~fhaque1/0.embed")

@app.route("/pop5")	
def population5():
	return render_template("map.html", url = "https://plot.ly/~fhaque1/10.embed")



if __name__ == '__main__':
    app.debug = True
    app.run()
