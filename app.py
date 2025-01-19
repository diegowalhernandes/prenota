from flask import Flask, render_template, redirect, url_for, flash, request
from app import create_app, db
from app.models import Property
from app.models import User


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
        # Coleta os dados do formulário
        name = request.form.get("name")
        description = request.form.get("description")
        price_per_night = request.form.get("price_per_night")
        location = request.form.get("location")

        # Verifica se os campos estão preenchidos
        if not all([name, description, price_per_night, location]):
            flash("Please fill in all fields.", "danger")
            return redirect(url_for("add_property"))

        try:
            # Cria e salva a nova propriedade no banco
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
        except Exception as e:
            flash(f"Error adding property: {e}", "danger")
            return redirect(url_for("add_property"))

    return render_template("add_property.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Coleta os dados do formulário
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")

        # Verifica se os campos foram preenchidos
        if not all([first_name, last_name, email, phone_number]):
            flash("All fields are required.", "danger")
            return redirect(url_for("register"))

        # Verifica se o email ou número de telefone já existem no banco
        existing_user = User.query.filter(
            (User.email == email) | (User.phone_number == phone_number)
        ).first()
        if existing_user:
            flash("Email or phone number already exists.", "danger")
            return redirect(url_for("register"))

        # Tenta criar e salvar o novo usuário
        try:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
            )
            db.session.add(new_user)
            db.session.commit()
            flash("User registered successfully!", "success")
            return redirect(url_for("register"))
        except Exception as e:
            db.session.rollback()
            flash(f"Error saving user: {e}", "danger")
            return redirect(url_for("register"))

    return render_template("register.html")




@app.route("/view_properties")
def view_properties():
    return render_template("view_properties.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8080)
