import mysql.connector



def listar_categoria():		#1
	db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="jornal")
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
	db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="jornal")
	cursor = db_connection.cursor()

	nome = input("inserir nome:")

	sql = "INSERT INTO categorias (nome) VALUES (%s)"
	values = (nome,)
	cursor.execute(sql, values)

	cursor.close()
	db_connection.commit()
	db_connection.close()

def	alterar_categoria():	#3
	print('\n Alterar categoria \n')
	
def apagar_categoria():		#4
	print('\n Apagar categoria \n')

def listar_noticia():		#5
	print('\n Listar noticia \n')
	
def inserir_noticia():		#6
	print('\n Inserir noticia \n')
	
def alterar_noticia():		#7
	print('\n Alterar noticia \n')
	
def apagar_noticia():		#8
	print('\n Apagar noticia \n')

while True:
	print('''1 Listar categorias
2 Inserir categoria
3 Alterar categoria
4 Apagar categoria
5 Listar noticias
6 Inserir noticia
7 Alterar noticia
8 Apagar noticia
9 Sair''')
	opcao = int(input('escolha uma opcao:'))
	if opcao == 1:
		listar_categoria()
	
	elif opcao == 2:
		inserir_categoria()
		
	elif opcao == 3:
		alterar_categoria()
		
	elif opcao == 4:
		apagar_categoria()
		
	elif opcao == 5:
		listar_noticia()
		
	elif opcao == 6:
		inserir_noticia()

	elif opcao == 7:
		alterar_noticia()
	
	elif opcao == 8:
		apagar_noticia()
		
	elif opcao == 9:
		break

	else:
		print('Opção inválida')
	