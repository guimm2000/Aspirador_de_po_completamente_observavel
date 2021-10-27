import ambiente

def limpar(amb, pos):
	amb.limpar(pos)

def direita(amb, pos):
	if(pos+1 >= amb.tam):
		noOp()
		return pos
	else:
		return pos + 1

def esquerda(amb, pos):
	if(pos-1 < 0):
		noOp()
		return pos
	else:
		return pos - 1

def noOp():
	pass