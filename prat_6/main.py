import math
import random

from typing import List


def funcao_objetivo(x: float, y: float) -> float:
	"""Função objetivo de análise.

	Args:
		x: Valor x da função.
		y: Valor y da função.

	Returns: A função avaliada em x e y.
	"""
	return math.sin(x) * math.exp(math.pow(1 - math.cos(y), 2)) + \
		math.cos(y) * math.exp(math.pow(1 - math.sin(x), 2)) + math.pow(x - y, 2)


def cria_populacao(tam_populacao: int) -> List[List[float]]:
	"""Cria a população de acordo com o tamanho proposto.

	Args:
		tam_populacao: Tamanho de amostras da população

	Returns: Matriz com os elementos aleatórios criados.
	"""
	p = []
	for index in range(tam_populacao):
		x_rand = random.uniform(-10, 10)
		y_rand = random.uniform(-10, 10)
		p.append([x_rand, y_rand])
	return p


def avalia_populacao(populacao: List[List[float]]) -> List[List[float]]:
	"""Avalia a população passada como parâmetro utilizando como função fitness o
	próprio valor obtido na função objetivo.

	Args:
		populacao: População que será avaliada.

	Returns: Matriz com os elementos ordenados com o valor na função
	objetivo ordenados do menor para o maior com a adição de uma
	posição em cada indivíduo que representa a sua aptidão ao
	ambiente.
	"""

	# Ordena do menor para o maior tomando como base o valor de x e y
	#	de cada indivídio da população.
	populacao_final: List[List[float]] = []
	p_ordenado: List[List[float]] = sorted(populacao, key=lambda individual: funcao_objetivo(individual[0], individual[1]), reverse=True)
	sum_index: int = 0
	# verificando a soma total de cada índice de elementos
	for index, individual in enumerate(p_ordenado, start=1):
		sum_index += index
	# adicionando a aptidão a cada indivíduo
	for index, individual in enumerate(p_ordenado, start=1):
		individual.append(int((index/sum_index)*100))
		populacao_final.append(individual)

	return populacao_final


def seleciona_pai(populacao: List[List[float]], num_sorteado: int) -> List[float]:
	"""Seleciona dentre os elementos um possível pai de acordo com a 
	probabilidade.

	Args:
		populacao: População de elementos com a sua aptidão.
		num_sorteado: Número sorteado pela roleta.

	Returns: Elemento sorteado.
	"""
	soma_relativa: int = 0
	for index, individuo in enumerate(populacao):
		# soma relativa é igual ao intervalo da aptidão do indicíduo
		soma_relativa += individuo[2]
		# caso o número sorteado seja menor ou igual a soma relativa
		# podemos retornar o individuo atual
		if num_sorteado <= soma_relativa:
			return individuo


def main():
	p = cria_populacao(3)
	p_final = avalia_populacao(p)
	x1 = random.randint(1, 100)
	x2 = random.randint(1, 100)
	x3 = random.randint(1, 100)
	x4 = random.randint(1, 100)
	x5 = random.randint(1, 100)
	x6 = random.randint(1, 100)
	print(seleciona_pai(p_final, x1))
	print(seleciona_pai(p_final, x2))
	print(seleciona_pai(p_final, x3))
	print(seleciona_pai(p_final, x4))
	print(seleciona_pai(p_final, x5))
	print(seleciona_pai(p_final, x6))
	# print(funcao_objetivo(-8.46, 6.87))
	# print(funcao_objetivo(-7.19, 7.76))
	pass


main()
