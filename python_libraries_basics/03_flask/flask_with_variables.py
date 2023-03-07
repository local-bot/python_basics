from flask import Flask, render_template


app = Flask(__name__)

variable_for_flask = "this is a python variable"

@app.route('/')
def index():
    return render_template('index.html') # returns templates/index.html

@app.route("/hello")
def hello():
    return "returns hello as string"

@app.route("/vars")
def vars():
    return render_template('index.html', name=variable_for_flask)

if __name__ == "__main__":
    app.run()
