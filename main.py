from re import L
from flask import Flask, render_template
import oyaml as yaml

app = Flask(__name__)

#set FLASK_APP - $env:FLASK_APP = "main"
#DO next step only for automatic reload
#set FLASK_ENV - $env:FLASK_ENV = "development"
#python -m flask run

@app.route("/")
def index():
    data = yaml.load(open('_config.yaml'))
    
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)