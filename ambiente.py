import random as ran

class Ambiente:
	salas = []
	def __init__(self, tamanho):
		self.tam = tamanho
		for i in range(self.tam):
			self.salas.append(False)

	def sujar(self):
		sala = ran.randint(0, self.tam-1)
		probabilidade_de_sujar = ran.randint(0, 1)
		if(probabilidade_de_sujar == 1):
			self.salas[sala] = True

	def limpar(self, pos):
		self.salas[pos] = False