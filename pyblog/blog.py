from flask import Flask, render_template, request
import sqlite3
import sqlalchemy

DB = sqlite3.connect("blog.db")
CONN = DB.cursor()
app = Flask(__name__)
@app.route("/home")
@app.route("/")
def home():

    return render_template("index.html")


@app.route("/posts")
def posts():
    DB = sqlite3.connect("blog.db")
    CONN = DB.cursor()
    Posts = CONN.fetchall()
    return render_template("posts.html",Posts=Posts)


@app.route("/add", methods=["POst"])
def add():
    DB = sqlite3.connect("blog.db")
    CONN = DB.cursor()
    title = request.form['title']
    text = request.form['text']
    url = request.files['files']
    CONN.execute("insert into post values({0},[1])",(title,text))
    if url != "":
        with open("UPLOADED_dir\\" + url ,"wb") as t:
            t.write(url)
@app.route("/form")
def Form():
    return render_template("form.html")

app.run(debug=True)
