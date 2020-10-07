# Arquivo para criação do algoritmo de Redes Neurais
import pandas as pd
import numpy as np


def activation_function(entry: np.array, function_type: int = 0) -> np.array:
	"""Função de ativação de uma determinada entrada.

	Args:
		entry: Array de entrada.
		function_type: Tipo da função de ativação.

	Returns: Array com o resultado de acordo com a avaliação.
	"""
	# array de retorno
	return_array = np.array([0, 0, 0])
	return_array = return_array.reshape((3, 1))
	# fazer a análise de acordo com cada entrada
	for index, line in enumerate(entry):
		if function_type == 0:
			# caso o valor contido na coluna da linha seja maior ou igual a 0
			return_array[index][0] = 1 if line[0] >= 0 else 0
	return return_array


def sum(entry: np.array) -> float:
	"""Método para cálculo do erro quadrático.

	Args:
		entry: Matriz de entrada.

	Returns: Somatório dos valores da Matriz ao quadrado.
	"""
	sum: float = 0
	for index, line in enumerate(entry):
		sum += line[0] ** 2
	return sum



def prepare_d(X: pd.DataFrame) -> np.array:
	"""Prepara o vertor de respostas dado o dataset de entrada.

	Args:
		X: Dados lidos do arquivo CSV.

	Returns: Matriz com a representação das classes.
	"""
	D: list[list[int]] = []
	for _, element in enumerate(X):
		if element == 'Iris-Setosa':
			D.append([0, 0, 1])
		elif element == 'Iris-Versicolour':
			D.append([0, 1, 0])
		elif element == 'Iris-virginica':
			D.append([1, 0, 0])
	D = np.array(D)
	return D



def perceptron(max_it: int, alpha: float, X: np.array, D: np.array) -> np.array:
	"""Método para execução do algoritmo de redes neurais.

	Args:
		max_it: Total de épocas.
		alpha: Taxa de aprendizagem.
		X: Matriz contendo as informações lidas dos arquivos.
		D: Matriz com os valores da classe de cada instância de X.

	Returns: Matriz W com os valores de treino.
	"""
	# inicializando as matrizes de peso e bias
	W: np.array = np.array([0.1, 0.2, 0.2, 0.4, 0.5, 0.4, 0.4, 0.6, 0.7, 0.4, 0.1, 0.2]).reshape((3, 4))  # peso de cada entrada para o neurônio
	b: np.array = np.array([1, 1, 1]).reshape((3, 1))  # bias do neurônio

	t: int = 1  # contador de iterações
	E: float = 1  # erro global
	e: list[float] = []  # erro por instância
	ve: list[np.array] = []  # vetor de erros

	y: np.array = []  # vetor de saída

	# como na leitura do csv temos uma instância em cada linha, preciamos transpor X
	# X = X.T

	# enquanto não atingirmos as épocas totais e o erro for maior que zero
	while t < max_it and E > 0:
		E = 0
		for index, value in enumerate(X):
			# obentenção da saída prevista de acordo com os pessos da entrada
			y.append(activation_function(W.dot(value.T) + b))
			# cálculo do erro de predição
			e.append(D[index] - y[index])
			# atualização da matrix de pesos
			W = W + (alpha * e[index].dot(value))
			# atualização do bias
			b = b + (alpha * e[index])
			# atualização do erro global
			E = E + sum(e[index])
			# adicionando o vetor de erros atual no vetor de históricos
			ve.append(e[index])
		t += 1

	return W

def main() -> None:
	"""Executa o código criado.

	Returns: None
	"""

	# lendo o arquivo csv
	dataset = pd.read_csv('data/iris_data.csv')
	# preparando os dados de D
	D = prepare_d(dataset['species'])
	# preparando os dados de X
	X = dataset.drop('species', 1)
	X = X.drop(0, 0)
	# calculando o algoritmo e obtendo W
	W = perceptron(300, 0.3, X, D)
	# exibindo
	print(f'Valor de W: {W}')


# Execução do código
main()