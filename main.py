from unittest import result
from flask import Flask, render_template,request



app = Flask(__name__)
@app.route("/")

def msg():
    return render_template("index.html")
@app.route("/summarize", methods=['POST','GET'])
def output():
    result="Virat Kohli is one of the world's most famous athletes and has been ranked as one of the world's most influential people by ESPN, Time magazine and Forbes, among others, in the years 2016 and 2018 respectively, as well as being ranked 66th in Forbes list of the top 100 highest-paid athletes in the world for the year 2020 with estimated earnings of over $26 million."
    return render_template('summary.html',result=result)
if __name__ =="__main__":
    app.run(debug=True,port=8800)