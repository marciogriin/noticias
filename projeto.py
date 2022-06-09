def listar_categoria():		#1
	print('Lista categoria')

def	inserir_categoria():	#2
	print('Inserir categoria')

def	alterar_categoria():	#3
	print('Alterar categoria')
	
def apagar_categoria():		#4
	print('Apagar categoria')

def listar_noticia():		#5
	print('Listar noticia')
	
def inserir_noticia():		#6
	print('Inserir noticia')
	
def alterar_noticia():		#7
	print('Alterar noticia')
	
def apagar_noticia():		#8
	print('Apagar noticia')

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
	opcao = input(escolha uma opcao)
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
	