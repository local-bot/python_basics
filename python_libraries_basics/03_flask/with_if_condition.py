from flask import Flask, render_template


app = Flask(__name__)

number = 7

@app.route('/')
def index():
    return render_template('if_condition.html', flask_variable_for_number=number) 

if __name__ == "__main__":
    app.run()
