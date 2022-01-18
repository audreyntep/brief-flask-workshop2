from flask import Flask, request, render_template

def create_app():
    app = Flask(__name__)
    return app