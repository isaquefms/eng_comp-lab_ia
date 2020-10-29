import math
import random

from typing import List, Tuple


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
	for indice, individuo in enumerate(populacao):
		# soma relativa é igual ao intervalo da aptidão do indicíduo
		soma_relativa += individuo[2]
		# caso o número sorteado seja menor ou igual a soma relativa
		# podemos retornar o individuo atual
		if num_sorteado <= soma_relativa:
			return individuo
	# caso nenhum número seja retornado anteriormente, retornamos o último
	return populacao[-1]


def cruzamento(pai_1: List[float], pai_2: List[float], taxa_de_cruzamento: float) -> Tuple[List[float], List[float]]:
	"""Realiza o cruzamento entre os pais passados como parâmetro
	levando em conta a taxa de cruzamento.

	Args:
		pai_1: Primeiro indivíduo pai.
		pai_2: Segundo indivíduo pai.
		taxa_de_cruzamento: Valor que informa a taxa de cruzamento.
		Valor entre 0 e 1.

	Returns: Indivíduos filhos gerados pelo cruzamento.
	"""
	# definimos um número aleatório para definirmos se iremos ter
	# cruzamento ou não
	num_aleat = random.uniform(0, 1.0)
	filho_1: List[float] = []
	filho_2: List[float] = []
	# há cruzamento
	if num_aleat <= taxa_de_cruzamento:
		# filho 1, x do pai 1 e y do pai 2
		filho_1.append(pai_1[0])
		filho_1.append(pai_2[1])
		# filho 2, x do pai 2 e y do pai 1
		filho_2.append(pai_2[0])
		filho_2.append(pai_1[1])
	# se não houver cruzamento
	else:
		# filho 1 é igual ao pai 1
		filho_1.append(pai_1[0])
		filho_1.append(pai_1[1])
		# filho 2 é igual ao pái 2
		filho_2.append(pai_2[0])
		filho_2.append(pai_2[1])
	return filho_1, filho_2


def mutacao(filho: List[float], taxa_de_mutacao: float) -> List[float]:
	"""Realiza a mutação de um filho a partir de uma determinada faixa.

	Args:
		filho: Indivíduo que irá passar pela mutação.
		taxa_de_mutacao: Número de ponto flutuante que informa a taxa
		de indivíduos que serão mutádos.

	Returns: Indivíduo resultante.
	"""
	filho_mutado: List[float] = []
	# número aleatório para avaliar se o indivíduo será mutado
	num_aleat = random.uniform(0, 1)
	# variável para selecionar qual elemento vamos mutar
	mutar_x: bool = False
	# se for mutado
	if num_aleat <= taxa_de_mutacao:
		if mutar_x:
			# muta o gene x
			filho_mutado.append(filho[0] + 0.2)
			filho_mutado.append(filho[1])
			# na próxima irá mutar y
			mutar_x = not mutar_x
		else:
			# muta o gene y
			filho_mutado.append(filho[0])
			filho_mutado.append(filho[1] - 0.3)
			# na próxima irá mutar x
			mutar_x = not mutar_x
	else:
		filho_mutado.append(filho[0])
		filho_mutado.append(filho[1])
	return filho_mutado


def main():
	p = cria_populacao(3)
	p_final = avalia_populacao(p)
	print(p_final)
	x1 = random.randint(1, 100)
	x2 = random.randint(1, 100)
	# x3 = random.randint(1, 100)
	# x4 = random.randint(1, 100)
	# x5 = random.randint(1, 100)
	# x6 = random.randint(1, 100)
	pai_1 = seleciona_pai(p_final, x1)
	pai_2 = seleciona_pai(p_final, x2)
	# print(seleciona_pai(p_final, x3))
	# print(seleciona_pai(p_final, x4))
	# print(seleciona_pai(p_final, x5))
	# print(seleciona_pai(p_final, x6))
	# print(funcao_objetivo(-4.30, -1.58))
	# print(funcao_objetivo(2.39, -5.65))
	# print(funcao_objetivo(6.56, -7.34))
	print(cruzamento(pai_1, pai_2, 1.0))
	pass


main()
