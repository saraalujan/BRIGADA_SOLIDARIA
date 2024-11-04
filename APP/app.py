from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

@app.route("/about")
def about():
    render_template("about.html")

@app.route("/contact")
def contact():
    render_template("contact.html")

@app.route("/")
def index():
    render_template("index.html")

@app.route("/service")
def service():
    render_template("service.html")

@app.route("/work")
def work():
    render_template("work.html")

if __name__=="__main__":
    app.run(debug=True)