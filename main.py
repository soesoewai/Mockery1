from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html")

@app.route("/readmore")
def readmore():
    return render_template("readmore.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/topics")
def topics():
    return render_template("topics.html")

if __name__ == "__main__":
    app.run(debug=True)


