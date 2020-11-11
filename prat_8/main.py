# módulos necessárias
import math
import pandas as pd
from typing import List

# método para criar a matriz de distâncias D
def cria_tabela_probabilidades(dataset: pd.DataFrame, feromonio_inicial: float) -> List[List[float]]:
	"""Cria a tabela de probabilidades do algoritmo.

	Args:
		dataset: Dataframe com as localizações das cidades.
		feromocio_inicial: Valor entre 0 e 1 que define a taxa de feromônio
		inicial das rotas.

	Returns: Matriz com as probabilidades de cada rota.
	"""
	D: List[List[float]] = []

	for i, valor in enumerate(dataset):
		cidade_partida_objetivo = []
		for j, segundo_valor in enumerate(dataset):
			if i == j:
				cidade_partida_objetivo.append([])
			else:
				d = round(math.sqrt(((segundo_valor[1] - valor[1]) ** 2) + ((segundo_valor[2] - valor[2]) ** 2)), 3)
				tal_x_y = round(1/d, 3)
				eta_x_y = feromonio_inicial
				tal_x_y_eta_x_y = round(tal_x_y * eta_x_y, 3)
				cidade_partida_objetivo.append([d, tal_x_y, eta_x_y, tal_x_y_eta_x_y])
		D.append(cidade_partida_objetivo)

	# agora que tal_x_y_eta_x_y estão definidos podemos calcular a probabilidade de um caminho
	for x, cidade_inicial in enumerate(D):
		# começamos definindo o valor do somatório de tal_x_y_eta_x_y para uma cidade inicial
		soma_tal_x_y_eta_x_y: float = 0.0
		for y, cidade_destino in enumerate(cidade_inicial):
			# se houver cidade de destino
			if cidade_destino:
				soma_tal_x_y_eta_x_y += cidade_destino[3]
		# com esse valor definido podemos os demais valores de D
		for y, cidade_destino in enumerate(cidade_inicial):
			# se houver cidade destino
			if cidade_destino:
				p_x_y = round(cidade_destino[3]/soma_tal_x_y_eta_x_y, 3)
				D[x][y].append(p_x_y)
				D[x][y].append(round(p_x_y*100, 3))

	return D


def calcula_caminhos():
	pass


def main():
	""" Função de execução do algoritmo.
	"""
	dataset = pd.read_csv('data/colonia.csv', header=None)
	D = cria_tabela_probabilidades(dataset.to_numpy(dtype=int), 0.1)
	print(D)



main()
