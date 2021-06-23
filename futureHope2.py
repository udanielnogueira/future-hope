import pygame
import random
import os

#Seta cores
branco = (255,255,255)
preta = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

#Verifica se a biblioteca Pygame está instalada
try:
	pygame.init()
except:
	print('Pygame não foi inicializado com sucesso')

#Exibe quantas operações foram sucedidas ou malsucedidas
print(pygame.init())

#Cria lista de afirmações
def get_afirmacoes():

	afirmacoes = []

	afirmacoes.append(['A Covid-19 foi a primeira pandemia.','F','Peste negra na França'])
	afirmacoes.append(['Muitas mortes foram causadas com a Covid-19','V','No Brasil foram mais de 500 mil'])
	afirmacoes.append(['Todos os países do mundo vacinaram-se de forma idêntica','F','Nem todos produziram vacina'])

	return afirmacoes
afirmacoes = get_afirmacoes()

#Embaralha afirmações
random.shuffle(afirmacoes)

#Inicializa o módulo display
pygame.display.init()

#Inicializa o módulo fonte
pygame.font.init()

#Seta o tipo de fonte
minhafonte = pygame.font.SysFont('Arial', 30)

#Seta largura e altura
fundo = pygame.display.set_mode((1080,600))

#Seta nome da janela
pygame.display.set_caption('Future Hope')

#Não deixa exceder 60fps
clock = pygame.time.Clock()
clock.tick(60)

#Menu Inicial
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

	fundo.fill(branco)

	texto_menu = minhafonte.render('Menu ', False, (0, 0, 0))
	texto_jogar = minhafonte.render('1 Jogar ', False, (0, 0, 0))
	texto_sair= minhafonte.render('0 Sair ', False, (0, 0, 0))

	fundo.blit(texto_menu,(500,50))
	fundo.blit(texto_jogar,(500,110))
	fundo.blit(texto_sair,(500,170))

	#Atualiza parte da tela para um novo frame, sempre que eu fizer algo novo, vai mostrar
	pygame.display.update()

	#Exibe eventos capturados na janela do jogo
	#print(event)

def jogar():

	vida = 50000

	for pergunta in afirmacoes:

		pygame.event.set_blocked(pygame.MOUSEMOTION)

		#print('entrou')

		fundo.fill(branco)

		texto_energia = minhafonte.render('Energia ', False, (0, 0, 0))
		fundo.blit(texto_energia,(25,25))
		texto_energia2 = minhafonte.render(str(vida), False, (0, 0, 0))
		fundo.blit(texto_energia2,(120,25))

		texto_pergunta = minhafonte.render(str(pergunta[0]), False, (0, 0, 0))
		fundo.blit(texto_pergunta,(25,150))

		botao_verde = pygame.draw.rect(fundo, (0,255,0), (25,250,150,50))
		botao_vermelho = pygame.draw.rect(fundo, (255,0,0), (200,250,150,50))
		botao_azul = pygame.draw.rect(fundo, (0,0,255), (380,250,150,50))

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

		#Atualiza tela 
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

			fundo.fill(branco)

			texto_pontuacao = minhafonte.render('Pontuação Final: '+str(vida), False, (0, 0, 0))
			texto_menu = minhafonte.render('1 Jogar novamente ', False, (0, 0, 0))
			texto_sair= minhafonte.render('0 Sair ', False, (0, 0, 0))

			fundo.blit(texto_pontuacao,(500,50))
			fundo.blit(texto_menu,(500,110))
			fundo.blit(texto_sair,(500,170))

			#Atualiza tela
			pygame.display.update()

	pontuacao()

	#print('saiu')

#Inicia o jogo após sair do Menu Inicial
jogar()

#Sai do jogo
pygame.quit()