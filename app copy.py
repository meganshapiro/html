import csv
from csv import writer
from flask import Flask
from flask import render_template,request
app = Flask(__name__)

#python -m flask run
@app.route("/")
def index():
    #return "Hello, Flask!"
    return render_template("meg.html")

@app.route("/", methods=["GET", "POST"])
@app.route("/save", methods=["GET", "POST"])
def save():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        names = (fname + lname)
        print(names)
        forward = request.form['forwards']
        defense = request.form['defensemen']
        goalie = request.form['goalie']
        data = [names, forward, defense, goalie]
        print("24")

        with open('NYR.csv', 'a', newline = '') as f_object:
            print("27")
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()

            return("Submitted")
        
if __name__ == "__main__":
    app.debug = True
    app.run()

