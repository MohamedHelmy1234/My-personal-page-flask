from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000, debug=True)
    # app.run(host = '0.0.0.0', port=5000, debug=True)