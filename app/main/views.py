# encoding: utf-8
from flask import render_template, abort, redirect, url_for, flash, jsonify, request
import requests, json
from . import main

@main.route("/index")
@main.route("/")
def index():
    """主页视图"""
    return render_template("index.html")

@main.route("/about")
def about():
    """主页视图"""
    return render_template("about.html")

@main.route("/photos")
def photos():
    """主页视图"""
    return render_template("photos.html")

@main.route("/contact")
def contact():
    """主页视图"""
    return render_template("contact.html")


