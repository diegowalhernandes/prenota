from flask import Flask, render_template, redirect, url_for, flash, request
from app import create_app, db
from app.models import Property

app = create_app()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/properties")
def properties():
    properties = Property.query.all()
    return render_template("properties.html", properties=properties)

@app.route("/add_property", methods=["GET", "POST"])
def add_property():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price_per_night = request.form.get("price_per_night")
        location = request.form.get("location")

        if not all([name, description, price_per_night, location]):
            flash("Please fill in all fields.", "danger")
            return redirect(url_for("add_property"))

        new_property = Property(
            name=name,
            description=description,
            price_per_night=float(price_per_night),
            location=location
        )
        db.session.add(new_property)
        db.session.commit()
        flash("Property added successfully!", "success")
        return redirect(url_for("properties"))

    return render_template("add_property.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
