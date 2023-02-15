import sqlite3

def get_entity_records_by_table_name(table_name):
	conn = sqlite3.connect("agendou.sqlite")
	cursor = conn.cursor()

	query_result = []

	cursor.execute(f"""
			SELECT * FROM {table_name}
		""")

	for line in cursor.fetchall():
		query_result.append(line)
	
	conn.close()
	
	return query_result

def insert_values(table_name, fields, values):
	conn = sqlite3.connect("agendou.sqlite")
	cursor = conn.cursor()

	fields_edited = " ,".join(fields)
	values_edited = " ,".join(values)

	cursor.execute(f"""
		INSERT INTO {table_name} ( {fields_edited} ) VALUES ( {values_edited} ); 
		""")

	conn.commit()
	conn.close()

def register():
	print("Cadastro de usuário")
	name = input("Insira o nome do usuário: ")
	id = input("Insira o id do usuário: ")
	cpf = input("Insira o cpf do usuário: ")
	email = input("Insira o email do usuário: ")
	password = input("Insira o password do usuário: ")
	password_check = input("Insira o password do usuário novamente: ")

	while not(password == password_check):
		print("ERRO: As senhas devem ser iguais!!")
		password = input("Insira o password do usuário: ")
		password_check = input("Insira o password do usuário novamente: ")

	id = f"'{id}'"
	name = f"'{name}'"
	cpf = f"'{cpf}'"
	email = f"'{email}'"
	password = f"'{password}'"

	fields = ["ID", "name", "CPF", "email", "password"]
	values = [id, name, cpf, email, password]

	insert_values("users", fields, values) 
	print("Usuário cadastrado com sucesso!")


register()

users = get_entity_records_by_table_name("users")

for user in users:
	print(user)
