import sqlite3

from crypto import encrypt_string

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
	password = f"'{encrypt_string(password)}'"

	fields = ["ID", "name", "CPF", "email", "password"]
	values = [id, name, cpf, email, password]

	insert_values("users", fields, values) 
	print("Usuário cadastrado com sucesso!")

def login():
	print("Login de Usuário")
	email = input("Insira o Email:")
	password = input("Insira senha:")
	conn = sqlite3.connect("agendou.sqlite")
	cursor = conn.cursor()
	cursor.execute(f"""
		SELECT email,password FROM users WHERE email = "{email}";
		""")
	result = []
	for row in cursor.fetchall():
		result.append(row)

	try:
		if result[0][1] == encrypt_string(password):
			print("Login realizado com Sucesso!")

		else:
			print("Email ou Senha Inválido!")
	except:
		print("Email ou Senha invalido!")
