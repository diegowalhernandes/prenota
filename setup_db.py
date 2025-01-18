from app import db, create_app

# Cria a aplicação Flask com a configuração apropriada
app = create_app()

with app.app_context():
    # Cria todas as tabelas definidas nos modelos
    db.create_all()
    print("Banco de dados e tabelas criados com sucesso!")
