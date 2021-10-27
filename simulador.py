import sensores_completamente as sen
import ambiente
import acoes
import random as ran

amb = ambiente.Ambiente(2)
aspirador = sen.AgenteCompletamente(amb, ran.randint(0, 1))

for i in range(1000):
	print("Periodo de tempo #" + str(i+1) + ":")
	amb.sujar()
	aspirador.checarSujeira()

print("Pontuação global: " + str(aspirador.pont))