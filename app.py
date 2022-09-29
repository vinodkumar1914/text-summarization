import os
from unittest import result
from flask import Flask, render_template,request

from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from transformers import pipeline
model_name = "google/pegasus-xsum"
pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)
pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

app = Flask(__name__)
picFolderr=os.path.join('static','pics')
app.config['UPLOAD_FOLDER']=picFolderr
@app.route("/")
def msg():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'model.jpg')
    return render_template("index.html",model_img=pic1)
@app.route("/summarize", methods=['POST','GET'])
def getSummary():
    body=request.form['data']
    text=body.split()
    cnt=0
    for i in text:
        cnt+=1
    summarizer = pipeline(
        "summarization", 
        model=model_name, 
        tokenizer=pegasus_tokenizer, 
        framework="pt"
    )
    summary = summarizer(body, min_length=100, max_length=450)
    result=summary[0]["summary_text"]
    return render_template('summary.html',result=result)

if __name__ =="__main__":
    app.run(debug=True,port=8000)