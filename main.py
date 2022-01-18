# -*- coding: utf-8 -*-

from distutils.log import debug
from flask import Flask, request, render_template

from app import create_app

app = create_app()

@app.route("/")
def page_home():
    return render_template("home.html", message = "Page Home")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['name']
    processed_text = text.upper()
    return render_template("home.html" , message = processed_text )

@app.route("/1")
def page_un():
    return render_template("page1.html", message = "Page 1")

if __name__ == "__main__":
    app.run(debug=True)