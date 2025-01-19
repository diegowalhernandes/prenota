from sqlalchemy import create_engine, text

# Conexão com o banco de dados SQLite
engine = create_engine("sqlite:///instance/stayhub.db")
conn = engine.connect()

# Consulta para buscar todos os usuários
result = conn.execute(text("SELECT * FROM user;"))

# Exibe os resultados
print("Usuários registrados no banco de dados:")
for row in result:
    print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Email: {row[3]}, Phone: {row[4]}, Username: {row[5]}")

# Fecha a conexão
conn.close()
