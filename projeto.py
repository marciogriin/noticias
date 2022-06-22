import mysql.connector



def listar_categoria():		#1
	db_connection = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="jornal")
	cursor = db_connection.cursor()

	sql = ("SELECT id, nome FROM categorias")
	cursor.execute(sql)

	print('{:^10}|{:^10}'.format('Id', 'Nome'))
	for (id, nome) in cursor:
	  print('{:^10}|{:^10}'.format(id, nome))
	print("\n")

	cursor.close()
	db_connection.close()

def	inserir_categoria():	#2
	db_connection = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="jornal")
	cursor = db_connection.cursor()

	nome = input("Insira o nome da categoria: ")

	sql = "INSERT INTO categorias (nome) VALUES (%s)"
	values = (nome,)
	cursor.execute(sql, values)

	cursor.close()
	db_connection.commit()
	db_connection.close()

def	atualizar_categoria():	#3
	db_connection = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="jornal")
	cursor = db_connection.cursor()

	nome = input("Insira o nome da nova categoria: ")
	id = int(input("Insira o ID correspondente: "))

	sql = ("update categorias set nome = %s where id= %s")
	values = (nome, id)
	cursor.execute(sql, values)

	cursor.close()
	db_connection.commit()
	db_connection.close()
	
def apagar_categoria():		#4
	db_connection = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="jornal")
	cursor = db_connection.cursor()
	
	id = int(input("Insira o ID da categoria que deseja apagar: "))
	
	sql = ("delete from categorias where id = %s") 
	values = (id,)
	cursor.execute(sql, values)
	
	cursor.close()
	db_connection.commit()
	db_connection.close()

def listar_noticia():		#5
    db_connection = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="jornal")
    cursor = db_connection.cursor()

    #sql = ("SELECT noticias.id, noticias.nome, noticias.texto, noticias.id_categoria, categorias.nome FROM noticias join categorias on noticias.id_categoria = categorias.id;")

    sql = ("SELECT id, nome, texto, id_categoria FROM noticias")
    cursor.execute(sql)

    print('{:^30}|{:^30}|{:^30}|{:^30}'.format('ID', 'Título', 'Notícia', 'ID Categoria'))
    for (id, nome, texto, id_categoria) in cursor:
	  print('{:^30}|{:^30}|{:^30}|{:^30}'.format(id, nome, texto, id_categoria))
	print("\n")

	cursor.close()
	db_connection.close()
	
def inserir_noticia():		#6
	db_connection = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="jornal")
	cursor = db_connection.cursor()

	nome = input("Insira o Título da notícia: ")
	texto = input("Insira a notícia: ")
	id_categoria = int(input('Insira o ID da Categoria: '))
	
	sql = "INSERT INTO noticias (nome, texto, id_categoria) VALUES (%s, %s, %s)"
	values = (nome, texto, id_categoria)
	cursor.execute(sql, values)

	cursor.close()
	db_connection.commit()
	db_connection.close()
	
def atualizar_noticia():		#7
    db_connection = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="jornal")
    cursor = db_connection.cursor()

    nome = input("Insira o título da notícia: ")
    texto = input("Insira a notícia")
    id_categoria = int(input("Insira o ID da categoria: "))

    sql = ("update noticias set nome = %s, texto = %s, where id_categoria = %s")
    values = (nome, texto, id_categoria)
    cursor.execute(sql, values)

    cursor.close()
    db_connection.commit()
    db_connection.close()
	
def apagar_noticia():		#8
	db_connection = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="jornal")
	cursor = db_connection.cursor()
	
	id = int(input("Insira o ID da noticia que deseja apagar: "))
	
	sql = ("delete from noticias where id = %s") 
	values = (id,)
	cursor.execute(sql, values)
	
	cursor.close()
	db_connection.commit()
	db_connection.close()

while True:
	print('''1 Listar categorias
2 Inserir categoria
3 Atualizar categoria
4 Apagar categoria
5 Listar noticias
6 Inserir noticia
7 Atualizar noticia
8 Apagar noticia
9 Sair''')
	opcao = int(input('escolha uma opcao:'))
	if opcao == 1:
		listar_categoria()
	
	elif opcao == 2:
		inserir_categoria()
		
	elif opcao == 3:
		atualizar_categoria()
		
	elif opcao == 4:
		apagar_categoria()
		
	elif opcao == 5:
		listar_noticia()
		
	elif opcao == 6:
		inserir_noticia()

	elif opcao == 7:
		atualizar_noticia()
	
	elif opcao == 8:
		apagar_noticia()
		
	elif opcao == 9:
		break

	else:
		print('Opção inválida')
	