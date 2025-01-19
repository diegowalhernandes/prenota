from flask import render_template, redirect, url_for, flash
from app import db, create_app
from app.models import User

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

@app.route("/dashboard/<int:user_id>")
def user_dashboard(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("dashboard.html", user=user)
