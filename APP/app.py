from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("abnut.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/work")
def work():
    return render_template("work.html")

if __name__=="__main__":
    app.run(debug=True,port=8080)