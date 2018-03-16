from flask import render_template, abort, redirect, url_for, flash, jsonify, request
import requests, json
from . import main

@main.route("/index")
@main.route("/")
def index():
    """主页视图"""
    return render_template("index.html")



