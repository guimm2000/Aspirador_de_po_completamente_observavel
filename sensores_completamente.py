import ambiente
import acoes
import random as ran

class AgenteCompletamente:
	def __init__(self, amb, pos):
		self.pos = int(pos)
		self.amb = amb
		self.pont = 0
		self.direita = False
		self.esquerda = False

	def checarSujeira(self):
		if(self.amb.salas[self.pos] == True):
			acoes.limpar(self.amb, self.pos)
			print("Limpei")
			self.pont += 1
		else:
			if(self.direita == False and self.esquerda == False):
				prob = ran.randint(0, 1)
				if(prob == 1): 
					posn = acoes.direita(self.amb, self.pos)
					if(posn == self.pos):
						print("Fiz nada")
					self.pos = posn
					self.direita = True
				else:
					posn = acoes.esquerda(self.amb, self.pos)
					if(posn == self.pos):
						print("Fiz nada")
					self.pos = posn
					self.esquerda = True

			elif(self.direita == True):
				if(acoes.direita(self.amb, self.pos) == self.pos):
					self.direita = False
					self.esquerda = True
					self.checarSujeira()
				else:
					self.pos = acoes.direita(self.amb, self.pos)
					print("Andei pra direita")
					self.pont -= 1

			elif(self.esquerda == True):
				if(acoes.esquerda(self.amb, self.pos) == self.pos):
					self.direita = True
					self.esquerda = False
					self.checarSujeira()
				else:
					self.pos = acoes.esquerda(self.amb, self.pos)
					print("Andei pra esquerda")
					self.pont-= 1