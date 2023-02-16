import sqlite3

from crypto import get_password_hashed

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

def register_cli():
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
	password = f"'{get_password_hashed(password)}'"

	fields = ["ID", "name", "CPF", "email", "password"]
	values = [id, name, cpf, email, password]

	insert_values("users", fields, values) 
	print("Usuário cadastrado com sucesso!")

def register(id,name,cpf,email,password):

	id = f"'{id}'"
	name = f"'{name}'"
	cpf = f"'{cpf}'"
	email = f"'{email}'"
	password = f"'{get_password_hashed(password)}'"
	disabled = "0"

	fields = ["ID", "name", "CPF", "email", "password", "disabled"]
	values = [id, name, cpf, email, password, disabled]

	insert_values("users", fields, values)


def login_cli():
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

def login_service(email, password):
	conn = sqlite3.connect("agendou.sqlite")
	cursor = conn.cursor()

	cursor.execute(f"""
		SELECT email,password FROM users WHERE email = "{email}";
		""")

	result = []


	try:
		for row in cursor.fetchall():
			result.append(row)

		if result[0][1] == encrypt_string(password):
			return "Login realizado com Sucesso!"
		else:
			return "Email ou Senha Inválido!"
		conn.close()
	except:
		conn.close()
		return "Email ou Senha Inválido!"


def convert_user_db_to_dict(db_row):
	user_dict = {
		"ID": None,
		"name": None,
		"CPF": None,
		"email": None,
		"password": None,
		"phone": None,
		"whatsapp": None,
		"provider_id": None,
		"disabled": None
	}

	user_dict["ID"] = db_row[0]
	user_dict["name"] = db_row[1]
	user_dict["CPF"] = db_row[2]
	user_dict["email"] = db_row[3]
	user_dict["password"] = db_row[4]
	user_dict["phone"] = db_row[5]
	user_dict["whatsapp"] = db_row[6]
	user_dict["provider_id"] = db_row[7]
	user_dict["disabled"] = db_row[8]

	return user_dict

def get_user_by_email(email):
	conn = sqlite3.connect("agendou.sqlite")
	cursor = conn.cursor()

	cursor.execute(f"""
		SELECT * FROM users WHERE email = "{email}";
		""")

	result = []

	
	try:
		for row in cursor.fetchall():
			result.append(row)

		return convert_user_db_to_dict(result[0])
	except:
		return None
