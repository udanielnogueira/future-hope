import pygame
import random
import os

# Seta cores
branco = (255,255,255)
preta = (0,0,0)
vermelho = (198,26,49)
verde = (26,198,106)
azul = (26,141,198)

roxo = (137,44,208)

# Verifica se a Pygame está instalada
try:
	pygame.init()
except:
	print('Pygame não foi inicializado com sucesso')

# Exibe quantas operações foram sucedidas ou malsucedidas
print(pygame.init())

# Cria lista de afirmações
def get_afirmacoes():
	afirmacoes = []

	afirmacoes.append(['A COVID-19 gerou a sexta grande pandemia mundial.','V','Houve a gripe espanhola em 1918 e outras.'])
	afirmacoes.append(['Menos de 700 mil mortes foram causadas através da COVID-19.','F','No Brasil foram mais de 500 mil.'])
	afirmacoes.append(['Países iniciaram um plano de vacinação de forma idêntica.','F','Alguns países produziram antes que outros.'])
	afirmacoes.append(['O vírus da COVID-19 não se reproduzia sozinho, ele precisa de uma célula hospedeira.','V','Disso depende a infecção.'])
	afirmacoes.append(['O vírus da COVID-19 não estava presente na saliva.','F','Pode ser transmitido por tosse ou conversa.'])
	afirmacoes.append(['O COVID-19 afetava principalmente as células do pulmão e intestino.','V','Afetados sentem dificuldades para respirar'])
	afirmacoes.append(['Apenas 2,2% de toda água do mundo era água doce.','V','Temos apenas 0,3% disponível para consumo.'])
	afirmacoes.append(['O setor agrupecuário não foi o maior causador de poluição no Brasil.','F','Não foi a indústria.'])
	afirmacoes.append(['Uma tonelada de papel reciclado poupava cerca de 22 árvores.','V','Com apenas 1 árvore se produzia milhares de kilos.'])

	return afirmacoes

afirmacoes = get_afirmacoes()

# Embaralha afirmações
random.shuffle(afirmacoes)

# Inicializa módulo display
pygame.display.init()

# Inicializa módulo fonte
pygame.font.init()

# Seta tipo de fonte
minhafonte = pygame.font.SysFont('Arial', 30)

# Seta largura e altura
fundo = pygame.display.set_mode((1080,600))

# Seta nome da janela
pygame.display.set_caption('Future Hope')

# Não deixa exceder 60fps
clock = pygame.time.Clock()
clock.tick(60)

# História do jogo
historia = True
while historia:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			historia = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				historia = False

	fundo.fill(roxo)

	texto_1 = minhafonte.render('O ano é 2107 e um viajante chamado Josh voltou ao século XXI.', False, (0, 0, 0))
	texto_2 = minhafonte.render('Porque seu mundo está devastado e a única esperança sou eu.', False, (0, 0, 0))
	texto_3 = minhafonte.render('Toda informação mundial foi perdida, então decidi ajudar.', False, (0, 0, 0))
	texto_4 = minhafonte.render('Ele me disse: "You are the Future Hope".', False, (0, 0, 0))
	texto_5 = minhafonte.render('Pressione 1 para continuar...', False, (0, 0, 0))

	fundo.blit(texto_1,(30,50))
	fundo.blit(texto_2,(30,110))
	fundo.blit(texto_3,(30,170))
	fundo.blit(texto_4,(30,230))
	fundo.blit(texto_5,(30,500))

	# Atualiza parte da tela para um novo frame
	# Vai mostrar sempre que eu fizer algo novo
	pygame.display.update()


# Menu Inicial
menu = True
while menu:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_0:
				pygame.quit()
			elif event.key == pygame.K_1:
				menu = False

	fundo.fill(roxo)

	texto_menu = minhafonte.render('Menu ', False, (0, 0, 0))
	texto_jogar = minhafonte.render('1 Jogar ', False, (0, 0, 0))
	texto_sair= minhafonte.render('0 Sair ', False, (0, 0, 0))

	fundo.blit(texto_menu,(500,50))
	fundo.blit(texto_jogar,(500,110))
	fundo.blit(texto_sair,(500,170))

	# Atualiza parte da tela para um novo frame
	# Vai mostrar sempre que eu fizer algo novo
	pygame.display.update()

	# Exibe eventos capturados na janela do jogo
	# print(event)

def jogar():

	vida = 50000

	for pergunta in afirmacoes:

		pygame.event.set_blocked(pygame.MOUSEMOTION)

		#print('entrou')

		fundo.fill(roxo)

		texto_energia = minhafonte.render('Energia ', False, (0, 0, 0))
		fundo.blit(texto_energia,(25,25))
		texto_energia2 = minhafonte.render(str(vida), False, (0, 0, 0))
		fundo.blit(texto_energia2,(120,25))

		texto_pergunta = minhafonte.render(str(pergunta[0]), False, (0, 0, 0))
		fundo.blit(texto_pergunta,(25,150))

		botao_verde = pygame.draw.rect(fundo, (verde), (25,250,150,50))
		botao_vermelho = pygame.draw.rect(fundo, (vermelho), (200,250,150,50))
		botao_azul = pygame.draw.rect(fundo, (azul), (380,250,150,50))

		texto_dica = minhafonte.render('Dica', False, (0, 0, 0))
		fundo.blit(texto_dica,(430,255))
		texto_verdadeiro = minhafonte.render('Verdadeiro', False, (0, 0, 0))
		fundo.blit(texto_verdadeiro,(35,255))
		texto_falso = minhafonte.render('Falso', False, (0, 0, 0))
		fundo.blit(texto_falso,(243,255))

		pygame.display.update()

		respondido = True
		while respondido:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					pos = pygame.mouse.get_pos()

					if botao_azul.collidepoint(pos):
						vida -= 1000

						texto_menos = minhafonte.render('-1000', False, (255, 0, 0))
						fundo.blit(texto_menos,(200,25))

						dica = minhafonte.render(str(pergunta[2]), False, (0, 0, 0))
						fundo.blit(dica,(25,350))
						pygame.display.update()

					if botao_verde.collidepoint(pos):
						resposta = 'V'
						if pergunta[1] == resposta:
							vida += 1500
							respondido =  False
						else:
							vida -= 5500
							respondido =  False

					elif botao_vermelho.collidepoint(pos):
						resposta = 'F'
						if pergunta[1] == resposta:
							vida += 1500
							respondido =  False
						else:
							vida -= 5500
							respondido =  False

		# Atualiza tela 
		pygame.display.update()

	def pontuacao():

		pontuacao = True
		while pontuacao:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_0:
						pygame.quit()
					elif event.key == pygame.K_1:
						jogar()

			fundo.fill(roxo)

			texto_pontuacao = minhafonte.render('Pontuação Final: '+str(vida), False, (0, 0, 0))
			texto_menu = minhafonte.render('1 Jogar novamente ', False, (0, 0, 0))
			texto_sair= minhafonte.render('0 Sair ', False, (0, 0, 0))

			fundo.blit(texto_pontuacao,(500,50))
			fundo.blit(texto_menu,(500,110))
			fundo.blit(texto_sair,(500,170))

			# Atualiza tela
			pygame.display.update()

	pontuacao()

	# print('saiu')

# Inicia o jogo após sair do Menu Inicial
jogar()

# Sai do jogo
pygame.quit()