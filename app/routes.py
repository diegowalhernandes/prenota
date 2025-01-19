from flask import render_template, redirect, url_for, flash
from app import db, create_app

app = create_app()

@app.route("/")
def home():
    return render_template("home.html")  # Página inicial

@app.route("/properties")
def properties():
    return render_template("properties.html")  # Listagem de propriedades

@app.route("/property/<int:id>")
def property_details(id):
    return render_template("property_details.html", id=id)  # Detalhes de uma propriedade
